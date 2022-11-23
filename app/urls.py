from django.urls import path
from .views import index,grafic
urlpatterns = [
    path('',index, name="index"),
    path('grafic', grafic, name = "grafic"),
]