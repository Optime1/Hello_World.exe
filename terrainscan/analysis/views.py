from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def analysis_page(request):
    return HttpResponse("<h4>тут должна быть страничка с анализом снимка<h4>")