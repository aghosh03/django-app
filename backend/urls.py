from django.urls import path, re_path, include
from rest_framework import routers
from .api import *
from . import views
from main.settings import FORCE_SCRIPT_NAME

app_name = "backend"
router = routers.DefaultRouter()
router.register(r'records', RecordViewSet, 'records')
router.register(r'users', UserViewSet, 'users')

urlpatterns = [
     path(FORCE_SCRIPT_NAME,views.index, name="index"),
     path(FORCE_SCRIPT_NAME+'settings/',views.settings, name="settings"),
     re_path(FORCE_SCRIPT_NAME+'data/', include((router.urls)))
]
