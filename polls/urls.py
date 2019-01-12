from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allPlayers', views.allplayers, name='allplayers'),
    path('allTeams', views.allteams, name='allteams'),
    path('search', views.search, name='search'),
    path('player/<str:pk>/', views.player, name='player'),
    path('team/<str:team_id>/<int:year_id>/', views.team, name='team')
]