from django.contrib import admin
from django.urls import path, include
from .settings import FORCE_SCRIPT_NAME

urlpatterns = [
    path(FORCE_SCRIPT_NAME, include("backend.urls")),
    path(FORCE_SCRIPT_NAME+'users/', include("users.urls")),
    path(FORCE_SCRIPT_NAME+'admin/', admin.site.urls),
]
