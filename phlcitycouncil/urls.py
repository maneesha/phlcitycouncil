from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('person/', views.PersonView.as_view(), name='person'),
    path('person/<int:pk>', views.PersonDetailView.as_view(), name = 'person-detail'),
    path('election/', views.ElectionView.as_view(), name = 'election' ),
    path('election/<int:pk>', views.ElectionDetailView.as_view(), name = "election-detail"),
    path('term/', views.TermView.as_view(), name="term"),
    path('api/election/', views.ElectionListAPI.as_view(), name='election_list_api'),
    path('api/election/<int:pk>/', views.ElectionDetailAPI.as_view(), name='election_detail_api'),
    path('api/person/', views.PersonListAPI.as_view(), name='person_list_api'),
    path('api/person/<int:pk>', views.PersonDetailAPI.as_view(), name='person_detail_api'),
    path('api/candidate/', views.CandidateListAPI.as_view(), name='candidate_list_api'),
    path('api/candidate/<int:pk>', views.CandidateDetailAPI.as_view(), name='candidate_detail_api'),
    path('api/', views.api_root)

]