from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('person/', views.PersonView.as_view(), name='person'),
    path('person/<int:pk>', views.PersonDetailView.as_view(), name = 'person-detail'),
    path('election/', views.ElectionView.as_view(), name = 'election' ),
    path('election/<int:pk>', views.ElectionDetailView.as_view(), name = "election-detail"),
    path('term/', views.TermView.as_view(), name="term"),
    path('api/election/', views.ElectionListAPI.as_view()),
    path('api/election/<int:pk>/', views.ElectionDetailAPI.as_view()),


]