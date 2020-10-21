from django.urls import path
from . import views


urlpatterns = [
    path('', views.page_index, name='index'),
    path('add-post/', views.page_add_post, name='add-post'),
]

 