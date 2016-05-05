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
def login_view(request):
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
                        'heading': 'Address Book',
                        'title': 'An all-in-one address book manager',
                        'content': 'Created by Zack Brown & Ben Skogen.',
                    }
                    return render(request, 'contacts/index.html', context)
                else:
                    errors.append('This account has been disabled.')
            else:
                errors.append('Invalid username or password.')

        context['errors'] = errors
        return render(request, 'contacts/login.html', context)
    else:
        login(request)
def viewContacts(request):

    cont = Contact.objects.all()
    context = {'title': 'List of all Contacts',
                'heading': "List of all Contacts",
                'contacts_list': cont,
               }
    return render(request, 'contacts/contacts.html', context)

def saveContact(request, contact_id=None):
    errors = []
    if request.method == 'POST':
        # handle data posted from the from
        if not request.POST.get('first_name', ''):
            errors.append('Enter first name.')
        if not request.POST.get('last_name'):
            errors.append('Enter last name.')
        if not request.POST.get('phone', ''):
            errors.append('Enter Phone')
        if not request.POST.get('email', ''):
            errors.append('Enter Email')

        data = {'heading': 'Thank You!',
                'content': 'Your data has been saved!',
                'errors': errors,
            }
        if errors:
            data['heading'] = 'Add New Contact'
            data['content'] = 'Fill in the following information:'
            return render(request, 'contacts/edit_contact.html', data)
        else:
            if contact_id:
                contact = Contact.objects.get(pk=contact_id)
            else:
                contact = Contact()
            contact.first_name = request.POST.get('first_name')
            contact.last_name = request.POST.get('last_name')
            contact.test1 = request.POST.get('phone')
            contact.test2 = request.POST.get('email')
            contact.save()
            data['heading'] = 'Success'
            data['content'] = 'Contact edited successfully!'
            data['contact'] = contact
            return render(request, 'contacts/edit_contact.html', data)
    else:
        if not contact_id:
            # must be a get method to enter new grade info so render the form for user to enter
            # data
            data = {
                'heading': 'Add New Contact',
                'content': 'Fill in the following information',
                'errors': errors,
            }
        else:
            # edit existing student
            student = Contact.objects.get(pk=contact_id)
            #student = get_object_or_404(Contact, pk=contact_id)
            data = {
                'heading': 'Edit Contact',
                'content': 'Update the following information',
                'errors': errors,
                'contact': contact,
            }

        return render(request, 'contacts/edit_contact.html', data)

def deleteContact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    contact.delete()
    return viewContacts(request, "/contacts/contacts.html")
def contactUs(request):
    context = {
        'heading': 'Address Book Contact Page',
        'content': 'Ben Skogen- Phone Number: 555-555-5555',
        'content2':  'Zack Brown- Phone Number: 999-999-9999'
    }
    return render(request, 'contacts/contactus.html', context)
def logout_view(request):
    logout(request)
    context = {
        'heading': 'Goodbye!',
        'content': '<a class="colorTag" href="/login/">Log back in again</a>',
        'title': 'Logout Successful!'
    }
    return render(request, 'contacts/index.html', context)
