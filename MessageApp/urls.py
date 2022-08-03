#from django.conf.urls import url
from django.urls import path
from MessageApp import views


urlpatterns = [
    path('messages/', views.message_api),
    path('messages/<int:id>', views.message_details)
]