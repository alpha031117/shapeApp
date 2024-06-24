from django.urls import path
from . import views

app_name = "userPortal"

urlpatterns = [
    path("", views.userHome, name="user_home"),
]
