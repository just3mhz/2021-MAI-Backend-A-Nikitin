from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, 'web/index.html')


@require_http_methods(["GET"])
def advertisement(request: HttpRequest, advertisement_id: int):
    return render(request, 'web/advertisement.html', {"advertisement_id": advertisement_id})


@require_http_methods(["GET"])
def add_advertisement(request: HttpRequest):
    return render(request, 'web/advertisement_form.html')
