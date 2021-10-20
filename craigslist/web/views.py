from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, 'craigslist_app/base.html')


