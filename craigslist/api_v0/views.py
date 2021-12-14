from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from .models import User
from .models import Category
from .models import Advertisement

from .serializers import UserSerializer
from .serializers import CategorySerializer
from .serializers import AdvertisementSerializer

from .forms import AdvertisementForm


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-reg_date')
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
