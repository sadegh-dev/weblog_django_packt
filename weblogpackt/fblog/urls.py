from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.page_index, name='index'),
    path('add-post/', views.page_add_post, name='add-post'),
]

