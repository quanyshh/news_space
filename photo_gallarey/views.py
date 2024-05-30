from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic.base import TemplateResponseMixin,View
from django.views.generic import DetailView,ListView
from .models import Gallarey

class GallareyListView(ListView):
    model = Gallarey
    template_name = 'gallarey/gallarey_list.html'
    context_object_name = 'posts'
