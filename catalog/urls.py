from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('races/', views.RaceListView.as_view(), name='races'),
    path('race/<int:pk>', views.RaceDetailView.as_view(), name='race-detail'),
    path('athletes/', views.AthleteListView.as_view(), name='athletes'),
    path('athlete/<int:pk>', views.AthleteDetailView.as_view(), name='athlete-detail'),
    path('race/<int:pk>/update/', views.RaceUpdateView.as_view(), name='race-update'),
    path('race/<int:pk>/delete/', views.RaceDeleteView.as_view(), name='race-delete'),
    path('race/create/', views.RaceCreateView.as_view(), name='race-create'),
]

