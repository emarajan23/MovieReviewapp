from django.db import models



class Movie(models.Model):


    
    genre_choices = [   ('Action', 'Action'),  ('Comedy', 'Comedy'), 
                        ('Drama', 'Drama'), ('Crime', 'Crime'), 
                        ('Thriller', 'Thriller'),  ('Horror', 'Horror'), 
                        ('Adventure', 'Adventure'), ('Romance', 'Romance'),
                        ('Mystery', 'Mystery'),('Animation', 'Animation') ]

    year_choices= [(year, str(year)) for year in range(2015, 2025)]

   
    movie_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, choices=genre_choices, default='Drama')
    release_date = models.DateField(null=True, blank=True)
    actor = models.CharField(max_length=100, blank=True, null=True)
    year = models.PositiveIntegerField(choices=year_choices, default=2020)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):

        return self.movie_title

class Review(models.Model):
    movie= models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.PositiveIntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.movie.movie_title}'