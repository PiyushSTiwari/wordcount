from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name='home'),
    path('count/',views.count, name='count'),
    path('About_Me/', views.about, name='About_Me'),
]
