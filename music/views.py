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



