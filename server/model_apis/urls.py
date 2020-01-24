from django.urls import path
from . import views
urlpatterns = [
    path('offensive/',views.test,name="offensive"),
]