from django.http import HttpRequest
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def by_category(request: HttpRequest, category: str):
    return JsonResponse({"Status": 501, "Message": "Not implemented"})


@require_http_methods(["GET"])
def advertisement(request: HttpRequest, ad_id: int):
    return JsonResponse({"Status": 501, "Message": "Not implemented"})


@require_http_methods(["GET", "POST"])
def add_advertisement(request: HttpRequest):
    return JsonResponse({"Status": 501, "Message": "Not implemented"})


@require_http_methods(["GET"])
def user(request: HttpRequest, user_id: int):
    return JsonResponse({"Status": 501, "Message": "Not implemented"})

