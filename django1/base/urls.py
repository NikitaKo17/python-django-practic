from django.urls import path
from . import views
import base

urlpatterns=[path('',views.index,name)]