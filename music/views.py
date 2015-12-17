from django.shortcuts import render, render_to_response
from django.forms import ModelForm
from .models import Genre
# Create your views here.

    

def view_performer(request):
	return render_to_response('music/performer.html',(csrf(request)))