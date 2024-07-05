from django import forms
from .models import Movie
from.models import Review


class MovieForm(forms.ModelForm):
    
    class Meta:
        model = Movie
        fields = ['movie_title','genre','release_date','actor','year','poster']  
        widgets = {'release_date' : forms.DateInput(attrs={'type':'date'})}
        

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ 'text', 'rating']