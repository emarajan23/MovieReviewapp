from django.urls import path
from . import views
from .views import show_media_root



urlpatterns = [

    path('add_movie/', views.add_movie, name='add_movie'),
    path('list_movie/', views.list_movie, name='list_movie'),
    path('media_root/', views.show_media_root),
    path('edit_movie/<int:movie_id>/',views.edit_movie, name='edit_movie'),
    path('delete_movie/<int:movie_id>/',views.delete_movie, name='delete_movie'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movies/', views.search_movies, name='search_movies'),
    
    
    ]