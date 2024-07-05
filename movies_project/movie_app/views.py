from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.db.models import Avg
from .models import Movie,Review
from .forms import MovieForm,ReviewForm

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_movie')
    else:
        form = MovieForm()
    return render(request, 'movie_app/add_movies.html', {'form': form})

def list_movie(request):
    movies = Movie.objects.all()
    return render(request, 'movie_app/list_movies.html', {'movies': movies})


def show_media_root(request):
    return HttpResponse(f'MEDIA_ROOT is: {settings.MEDIA_ROOT}')


def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('list_movie')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie_app/edit_movies.html', {'form': form, 'movie': movie})

def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('list_movie')
    return render(request, 'movie_app/delete_movies.html', {'movie': movie})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = movie.reviews.all()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = ReviewForm()
    return render(request, 'movie_app/movie_detail.html', {'movie': movie, 'reviews': reviews, 'form': form,'average_rating':average_rating })
    
  
def search_movies(request):
    query = request.GET.get('search')
    if query:
        movies = Movie.objects.filter(movie_title__icontains=query)
    else:
        movies = Movie.objects.all()
    return render(request, 'movie_app/list_movies.html', {'movies': movies})


