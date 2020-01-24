from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
import json
# Create your views here.

@csrf_exempt
def test(request):
    print(request.is_ajax())
    print(request)
    json_text = json.loads(request.body)
    print(request.method)
    print(json_text)
    return HttpResponse("Request Recieved!")