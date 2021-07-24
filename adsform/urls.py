from django.urls.conf import path
from . import views

urlpatterns = [
    path('',views.Home,name="home"),
]