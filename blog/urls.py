from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('edit/<slug:slug>/', views.edit_blog, name='edit_blog'),
    path('delete/<slug:slug>/', views.delete_blog, name='delete_blog'),
]
