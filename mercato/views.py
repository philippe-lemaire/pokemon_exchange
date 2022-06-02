from django.shortcuts import render
from django.views import generic

# Create your views here.
from django.http import HttpResponse


class IndexView(generic.TemplateView):
    template_name = "mercato/index.html"


def index_view(request):
    return HttpResponse("Hello, world. You're at the mercato index.")
