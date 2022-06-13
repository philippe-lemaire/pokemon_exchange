from django.shortcuts import render
from django.views import generic
from .models import Offer, Request

# Create your views here.


class IndexView(generic.ListView):
    model = Offer
    template_name = "mercato/index.html"
