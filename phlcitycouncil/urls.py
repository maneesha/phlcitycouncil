from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('person/', views.PersonView.as_view(), name='person')
]