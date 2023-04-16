from django.urls import path
from . import views

# URL_Conf
urlpatterns = [
    path('hello/',views.say_nicki)
]