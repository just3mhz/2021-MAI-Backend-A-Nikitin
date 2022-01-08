from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


@login_required
@require_http_methods(["GET"])
def index(request: HttpRequest):
    print(request.user.email)
    return render(request, 'web/index.html')


@require_http_methods(["GET"])
def login_view(request: HttpRequest):
    return render(request, 'web/login.html')


@login_required
@require_http_methods(["GET"])
def advertisement(request: HttpRequest, advertisement_id: int):
    print(request.user.pk)
    return render(request, 'web/advertisement.html',
                  {"advertisement_id": advertisement_id,
                   "user": request.user})


@require_http_methods(["GET"])
@login_required
def add_advertisement(request: HttpRequest):
    return render(request, 'web/advertisement_form.html', {'user': request.user})


@require_http_methods(["GET"])
@login_required
def search_view(request: HttpRequest):
    return render(request, 'web/search_advertisements.html')
