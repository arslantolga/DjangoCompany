from django.urls import path
from .views import *

urlpatterns = [
    path("", home_view, name='home'),
    path("about/", about_view, name='about'),
    path("vision/", vision_view, name='vision'),
    path("contact/", contact_view, name='contact'),
]