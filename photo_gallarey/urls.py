from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
app_name = 'photo_gallarey'

urlpatterns =[
	path('list/', views.GallareyListView.as_view(), name='gallarey_list'),
]