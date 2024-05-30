from django.shortcuts import render, redirect,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView,ListView
from .models import Univers
from django.views.generic.base import TemplateResponseMixin,View

class UniversListView(ListView):
    model = Univers
    template_name = 'univers/univers_list.html'
    context_object_name = 'univers'
    paginate_by = 5 

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class UniversDetailView(TemplateResponseMixin, View):
    template_name = 'univers/univers_detail.html'

    def get(self, request, id):
        post = get_object_or_404(Univers, id=id)
        post.views += 1
        post.save()
        return self.render_to_response({'post': post, 'id': id})
