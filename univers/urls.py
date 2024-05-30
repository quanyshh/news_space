from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
app_name = 'univers'

urlpatterns =[
	path('univers/<int:id>/', views.UniversDetailView.as_view(), name='univers_detail'),
	path('list/', views.UniversListView.as_view(), name='univers_list'),
]