<<<<<<< HEAD
from django.shortcuts import render
from django.shortcuts import render,render_to_response, get_object_or_404 
from django.core.context_processors import csrf 
# Create your views here.



def view_genre(request):
	genre_name =  request.POST.get(genre_name)
    return render_to_response('music/genre.html'csrf,(request))	



=======
from django.shortcuts import render, render_to_response
from django.forms import ModelForm
from .models import Genre
# Create your views here.

    

def view_performer(request):
	return render_to_response('music/performer.html',(csrf(request)))
>>>>>>> 16d42800e552f2319e04750c0a413ebc8b1f8269
