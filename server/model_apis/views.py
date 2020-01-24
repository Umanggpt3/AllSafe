from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
# Create your views here.

@csrf_exempt
def test(request):
    text = request.POST.get("html_doc")
    print(request.method)
    print(text)
    return HttpResponse("Request Recieved!")