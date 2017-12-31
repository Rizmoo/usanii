from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:photo_id>/', views.detail, name='detail'),
    path('add', views.add, name='add'),
]
