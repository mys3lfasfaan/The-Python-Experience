from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def function_based_view(request):
    return HttpResponse("Hello MKL")

class ClassBasedView(View):
    def get(self, request):
        return HttpResponse("Hello MKL 2")
    