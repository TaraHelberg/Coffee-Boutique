from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('copyright/', views.copyright, name='copyright'),
    path('faq/', views.faq, name='faq'),
]
