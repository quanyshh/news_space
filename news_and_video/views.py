from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic.base import TemplateResponseMixin,View
from news_and_video.models import Video
from django.views import View
from django.http import Http404
from django.db.models import Count

class VideoDetailView(TemplateResponseMixin, View):
    template_name = 'post/video_detail.html'

    def get(self, request, id):
        video = get_object_or_404(Video, id=id)
        video.views += 1
        video.save()
        return self.render_to_response({'video': video, 'id': id })
