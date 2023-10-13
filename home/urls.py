from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("Events/", views.Events, name="Events"),
    path("chvl_hof/", views.Chvls, name="chvls")
]