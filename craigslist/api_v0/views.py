import json

from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView

from elasticsearch_dsl import Q

from django.core.cache import cache

from .models import User
from .models import Category
from .models import Advertisement

from .serializers import UserSerializer
from .serializers import CategorySerializer
from .serializers import AdvertisementSerializer

from .documents import AdvertisementDocument

from .forms import AdvertisementForm

from craigslist.settings import DEFAULT_CACHE_TTL


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        ads = Advertisement.objects.filter(category_id=pk).order_by('-pub_date')
        serializer = AdvertisementSerializer(ads, many=True)
        return Response(serializer.data)


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all().order_by('-pub_date')
    serializer_class = AdvertisementSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        if cache.has_key(request.path):
            data = cache.get(request.path)
            return Response(json.loads(data), status=200)
        try:
            advertisement = Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            return Response('Not found', status=404)

        serializer = AdvertisementSerializer(advertisement)
        cache.set(request.path, json.dumps(serializer.data), timeout=DEFAULT_CACHE_TTL)

        return Response(serializer.data, status=200)

    def update(self, request, pk=None, *args, **kwargs):
        cache.delete(request.path)
        return super().update(request, pk=pk, *args, **kwargs)

    def partial_update(self, request, pk=None, *args, **kwargs):
        cache.delete(request.path)
        return super().partial_update(request, pk=pk, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        cache.delete(request.path)
        return super().partial_update(request, pk=pk, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        advertisement_form = AdvertisementForm(request.data)

        if not advertisement_form.is_valid():
            return Response({"errors": advertisement_form.errors}, status=400)

        adv = Advertisement.objects.create(
            title=advertisement_form.cleaned_data["title"],
            description=advertisement_form.cleaned_data["description"],
            price=advertisement_form.cleaned_data["price"],
            pub_date=advertisement_form.cleaned_data["pub_date"],
            published=advertisement_form.cleaned_data["published"],
            category=advertisement_form.cleaned_data["category"],
            user=advertisement_form.cleaned_data["user"]
        )

        return Response({"advertisement_id": adv.advertisement_id}, status=200)


class SearchAdvertisements(APIView):
    @staticmethod
    def q_expression(query):
        return Q('multi_match', query=query,
                 fields=[
                    'title',
                    'description',
                 ], fuzziness='auto')

    def get(self, request, query):
        try:
            q = self.q_expression(query)
            search = AdvertisementDocument.search().query(q)
            response = search.to_queryset()
            serializer = AdvertisementSerializer(response, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response(str(e), status=500)
