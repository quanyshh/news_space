from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
app_name = 'news_and_video'

urlpatterns =[
	path('video/<int:id>/', views.VideoDetailView.as_view(), name='video_detail'),
]