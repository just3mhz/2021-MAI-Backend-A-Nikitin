from sys import stderr

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def connect(request):
    response = {
        'result': {
            'user': 'some_user'
        }
    }
    return JsonResponse(response)


@csrf_exempt
def publish(request):
    response = {
        'result': {}
    }
    return JsonResponse(response)


@csrf_exempt
def subscribe(request):
    response = {
        'result': {}
    }
    return JsonResponse(response)
