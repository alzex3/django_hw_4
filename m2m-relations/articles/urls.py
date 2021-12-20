from django.urls import path
from django.conf import settings
from .views import articles_list

urlpatterns = [
    path('', articles_list, name='articles'),
]
