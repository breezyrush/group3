<<<<<<< HEAD
from django.shortcuts import render
from django.http import *
from django.views.generic import View
from django.contrib import auth
from musixscore.models import *
from musixscore.forms import *
import json
from django.utils import timezone
import datetime
from django.db import connection
# Create your views here.


#To do: Select Performer - Obtain Performer work records 
# - return performer work records - display all cd's or other works

def Cd_name(request):
	Performers_name = performer.objects.filter(createdby=request.user.id)
    return render_to_response('App/view_event.html', {'event': event})
    return render_to_response('App/view_event.html', {'cd's: event})



=======
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
>>>>>>> bbfc054bae8a20ebb7011618290c65909833971c
