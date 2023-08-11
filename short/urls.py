from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('<slug:key>',views.router)
]
