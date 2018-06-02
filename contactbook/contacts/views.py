from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Contact

# Create your views here.
def index(request):
    context = {
        'heading': 'Address Book',
        'title': 'An all-in-one address book manager',
        'content': 'Created by Zack Brown',
    }
    return render(request, 'contacts/index.html', context)
def about(request):
    context = {
        'heading': 'About Our Address Book',
        'content': 'Address Book is a django-based web server \n allowing users to manage their contacts in an \n all-inclusive and easy to use package.',
    }
    return render(request, 'contacts/about.html', context)
def login_view(request):
    context = {
        'heading': 'Please Sign In',
        'title': 'Login',
    }
    return render(request, 'contacts/login.html', context)
@login_required()
def searchProcessFName(request):
    errors = []
    if request.method == 'POST':
        searchEntry = request.POST.get('searchEntry')
    con = Contact.objects.filter(first_name__icontains=searchEntry)
    if con.exists():
        content = {
            'heading': 'Returned results:',
            'contacts_list': con
        }
    else:
        con = Contact.objects.all()
        content = {
            'heading': 'LIST OF ALL CONTACTS',
            'update': 'No contacts found using given search',
            'contacts_list': con
        }

    return render(request, 'contacts/contacts.html', content)
@login_required()
def searchProcessLName(request):
    errors = []
    if request.method == 'POST':
        searchEntry = request.POST.get('searchEntry')
    con = Contact.objects.filter(last_name__icontains=searchEntry)
    if con.exists():
        content = {
            'heading': 'Results Found Successfully!',
            'contacts_list': con
        }
    else:
        con = Contact.objects.all()
        content = {
            'heading': 'LIST OF ALL CONTACTS',
            'update': 'No contacts found using given search',
            'contacts_list': con
        }

    return render(request, 'contacts/contacts.html', content)
@login_required()
def searchProcessPNumber(request):
    errors = []
    if request.method == 'POST':
        searchEntry = request.POST.get('searchEntry')
    con = Contact.objects.filter(phone__icontains=searchEntry)
    if con.exists():
        content = {
            'heading': 'Results Found Successfully!',
            'contacts_list': con
        }
    else:
        con = Contact.objects.all()
        content = {
            'heading': 'LIST OF ALL CONTACTS',
            'update': 'No contacts found using given search',
            'contacts_list': con
        }

    return render(request, 'contacts/contacts.html', content)
@login_required()
def searchProcessEmail(request):
    errors = []
    if request.method == 'POST':
        searchEntry = request.POST.get('searchEntry')
    con = Contact.objects.filter(email__icontains=searchEntry)
    if con.exists():
        content = {
            'heading': 'Results Found Successfully!',
            'contacts_list': con
        }
    else:
        con = Contact.objects.all()
        content = {
            'heading': 'LIST OF ALL CONTACTS',
            'update': 'No contacts found using given search',
            'contacts_list': con
        }

    return render(request, 'contacts/contacts.html', content)


def loginProcess(request):
    errors = []
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
                        'content': 'Successfully logged in as ' + user.username
                    }
                    return render(request, 'contacts/index.html', context)
                else:
                    errors.append('This account has been disabled.')
            else:
                errors.append('Invalid username or password.')
        context = {
            'heading': 'Please Sign In',
        }
        context['errors'] = errors
        return render(request, 'contacts/login.html', context)
    else:
        login(request)

@login_required()
def searchByFName(request):
    context = {
        'title': 'Enter First Name to Search',
        'placeholder': 'FirstName',
        'fname': "fname"
    }
    return render(request, 'contacts/searchcontact.html', context)
@login_required()
def searchByLName(request):
    context = {
        'title': 'Enter Last Name to Search',
        'placeholder': 'LastName',
        'lname': "lname"
    }
    return render(request, 'contacts/searchcontact.html', context)
@login_required()
def searchByPNumber(request):
    context = {
        'title': 'Enter Phone Number to Search',
        'placeholder': 'PhoneNumber',
        'pnumber': "pnumber"
    }
    return render(request, 'contacts/searchcontact.html', context)
@login_required()
def searchByEmail(request):
    context = {
        'title': 'Enter Email to Search',
        'placeholder': 'Email',
        'email': "email"
    }
    return render(request, 'contacts/searchcontact.html', context)
@login_required()
def viewContactsByEmail(request):
    cont = Contact.objects.order_by('email')
    context = {'title': 'List of all Contacts',
               'heading': "List of all Contacts",
               'contacts_list': cont,
               }
    return render(request, 'contacts/contacts.html', context)
@login_required()
def viewContactsByPNumber(request):
    cont = Contact.objects.order_by('phone')
    context = {'title': 'List of all Contacts',
               'heading': "List of all Contacts",
               'contacts_list': cont,
               }
    return render(request, 'contacts/contacts.html', context)
@login_required()
def viewContactsByLName(request):
    cont = Contact.objects.order_by('last_name')
    context = {'title': 'List of all Contacts',
               'heading': "List of all Contacts",
               'contacts_list': cont,
               }
    return render(request, 'contacts/contacts.html', context)
@login_required()
def viewContactsByFName(request):
    cont = Contact.objects.order_by('first_name')
    context = {'title': 'List of all Contacts',
               'heading': "List of all Contacts",
               'contacts_list': cont,
               }
    return render(request, 'contacts/contacts.html', context)
@login_required()
def viewContacts(request):

    cont = Contact.objects.all()
    context = {'title': 'List of all Contacts',
                'heading': "List of all Contacts",
                'contacts_list': cont,
               }
    return render(request, 'contacts/contacts.html', context)
@login_required()
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

        if contact_id:
            contact = Contact.objects.get(pk=contact_id)
        else:
            contact = Contact()
        contact.first_name = request.POST.get('first_name')
        contact.last_name = request.POST.get('last_name')
        contact.phone = request.POST.get('phone')
        contact.email = request.POST.get('email')
        data = {'heading': 'Thank You!',
                'content': 'Your data has been saved!',
                'errors': errors,
                }
        if errors:
            data['heading'] = 'Add New Contact'
            data['content'] = 'Fill in the following information:'
            return render(request, 'contacts/edit_contact.html', data)
        else:
            contact.first_name = request.POST.get('first_name')
            contact.last_name = request.POST.get('last_name')
            contact.phone = request.POST.get('phone')
            contact.email = request.POST.get('email')
            contact.save()
            contacts_list = Contact.objects.all()
            content = {'update': 'Contact updated successfully',
                       'contacts_list': contacts_list,
                       'heading': 'LIST OF ALL CONTACTS'
                        }
            return render(request, 'contacts/contacts.html', content)
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
            contact = Contact.objects.get(pk=contact_id)
            data = {
                'heading': 'Edit Contact',
                'content': 'Update the following information',
                'errors': errors,
                'contact': contact,
            }

        return render(request, 'contacts/edit_contact.html', data)
@login_required(login_url='/login/')
def deleteContact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    return viewContacts(request)
def logout_view(request):
    logout(request)
    context = {
        'heading': 'Goodbye!',
        'content': '<a class="colorTag" href="/login/">Log back in again</a>',
        'title': 'Logout Successful!'
    }
    return render(request, 'contacts/index.html', context)
def contactUs(request):
    context = {
        'heading': 'Address Book Contact Page',
        'content2': 'John Doe- Phone Number: 555-555-5555',
        'content':  'Zack Brown- Phone Number: 999-999-9999'
    }
    return render(request, 'contacts/contactus.html', context)

