from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Contact

# Create your views here.
def index(request):
    context = {
        'heading': 'Address Book',
        'title': 'An all-in-one address book manager',
        'content': 'Created by Zack Brown & Ben Skogen.',
    }
    return render(request, 'contacts/index.html', context)
def about(request):
    context = {
        'heading': 'About Our Address Book'
        'content' 'Address Book is a collaborative django-based web server \n allowing users to manage their contacts in an all-inclusive and easy to use package.'
    }
    return render(request, 'contacts/about.html', context)
def login(request):
    context = {
        'heading': 'Login',
        'title': 'Login',
    }
    return render(request, 'contacts/login.html', context)

def loginProcess(request):
    errors = []
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if not username:
            errors.append('Username is required')
        if not password:
            errors.append('Password is required')

        if not errors:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    context = {
                        'heading': 'Welcome to A Grade Book.',
                        'title': 'A Grade Book',
                    }
                    return render(request, 'grades/index.html', context)
                else:
                    errors.append('This account has been disabled.')
            else:
                errors.append('Invalid username or password.')

        context['errors'] = errors
        return render(request, 'grades/login.html', context)
    else:
        login(request)
def viewContacts(request):

    contacts = Contact.objects.all()
    context = {'title': 'List of all Contacts',
                'heading': "List of all Contacts",
                'contacts_list': contacts,
               }
    return render(request, 'contacts/contacts.html', context)


