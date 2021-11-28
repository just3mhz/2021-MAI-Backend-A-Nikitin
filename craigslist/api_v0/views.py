from django.http import HttpRequest
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import User
from .models import Category
from .models import Advertisement

from .forms import AdvertisementForm


@require_http_methods(["GET"])
def by_category(request: HttpRequest, category_id: int):
    try:
        category = Category.objects.get(category_id=category_id)
    except Category.DoesNotExist:
        return JsonResponse({"message": "No such category"}, status=404)

    advertisements = Advertisement.objects.filter(category=category_id)
    advertisements = advertisements.order_by('-pub_date')

    return JsonResponse({
        "category": category.category,
        "advertisements": [{"advertisement_id": adv.advertisement_id, "title": adv.title} for adv in advertisements]
    })


@require_http_methods(["GET"])
def advertisement(request: HttpRequest, ad_id: int):
    try:
        adv = Advertisement.objects.get(advertisement_id=ad_id)
    except Advertisement.DoesNotExist:
        return JsonResponse({"message": "Not found"}, status=404)

    return JsonResponse({
        "title": adv.title,
        "description": adv.description,
        "price": adv.price,
        "pub_date": adv.pub_date,
        "published": adv.published,
        "user_id": adv.user.user_id,
        "category_id": adv.category.category_id
    })


@require_http_methods(["GET", "POST"])
def add_advertisement(request: HttpRequest):
    if request.method != 'POST':
        return render(request, 'craigslist_app/adv_form.html', {'form': AdvertisementForm()})

    form = AdvertisementForm(request.POST)
    if not form.is_valid():
        return render(request, 'craigslist_app/adv_form.html', {'form': form})

    try:
        u = User.objects.get(user_id=form.cleaned_data["user_id"])
    except User.DoesNotExist:
        return render(request, 'craigslist_app/adv_form.html', {'form': form})

    try:
        category = Category.objects.get(category_id=form.cleaned_data["category_id"])
    except Category.DoesNotExist:
        return render(request, 'craigslist_app/adv_form.html', {'form': form})

    adv = Advertisement.objects.create(
        title=form.cleaned_data["title"],
        description=form.cleaned_data["description"],
        price=form.cleaned_data["price"],
        pub_date=form.cleaned_data["pub_date"],
        published=form.cleaned_data["published"],
        category=category,
        user=u
    )

    adv.save()
    return HttpResponseRedirect(f'/api/v0/advertisement/{adv.advertisement_id}')


@require_http_methods(["GET"])
def user(request: HttpRequest, user_id: int) -> JsonResponse:
    try:
        u = User.objects.get(user_id=user_id)
        return JsonResponse({
            "first_name": u.first_name,
            "second_name": u.second_name,
            "phone": u.phone,
            "reg_date": u.reg_date
        })
    except User.DoesNotExist:
        return JsonResponse({"message": "Not found"}, status=404)

