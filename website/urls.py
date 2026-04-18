from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name="contact"),
    path('pricing', views.pricing, name='pricing'),
    path('service', views.service, name='service'),
    path('blog', views.blog, name='blog'),
    path('blog_details', views.blog_details, name='blog_details'),
    path("blog_details/<int:id>/", views.blog_details, name ="blog_details"),
]
