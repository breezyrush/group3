from django.shortcuts import render
from django.shortcuts import render,render_to_response, get_object_or_404 
from django.core.context_processors import csrf 
# Create your views here.



def view_genre(request):
	genre_name =  request.POST.get(genre_name)
    return render_to_response('music/genre.html'csrf,(request))	



