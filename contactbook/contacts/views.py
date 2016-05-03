from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Contact

# Create your views here.
def index(request):
    context = {
        'heading': 'Welcome to A Contact Book',
        'content': 'Must <a href="/login/">login</a> to use the application.',
        'title': 'A Contact Book'
    }
    #return HttpResponse(html)
    return render(request, 'contacts/index.html', context)
