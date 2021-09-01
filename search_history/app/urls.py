from django.urls import path

from django.conf.urls import include, url

from . import views
from .views import *


urlpatterns = [
    path('', views.search, name="asearch"),
    

    
    # path('update-status/<int:pk>/event/', UpdateEventStatusView.as_view(), name='update-event-status'),


]
