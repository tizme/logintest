from django.shortcuts import render, redirect
from django.contrib import messages
from models import User

# Create your views here.
def index(request):
    context = { 'users' : User.objects.all()}
    return render(request,'login/index.html', context)

def register(request):
    email_validate = User.objects.validate_email(request.POST['email'])
    password_validate = User.objects.validate_password(request.POST['password'], request.POST['pwconfirm'])
    fname_validate = User.objects.validate_firstname(request.POST['first_name'])
    lname_validate = User.objects.validate_lastname(request.POST['last_name'])

def create(request):
    if request.method == 'POST':
        print request.POST
        new_user = User.objects.validate_User(request.POST)
        if 'errors' in new_user:
            for validation_error in new_user['errors']:
                messages.error(request, 'validated_user["errors"]')
        if 'the_user' in new_user:
            messages.success(request, 'User Added')
        return redirect ('/')

def login(request):
    import bcrypt
    email = request.POST['e-mail']
    password = User.objects.get(email=email).password.encode()
    chkpw = request.POST['password'].encode()
    if bcrypt.checkpw(chkpw, password):
        print 'Welcome User'
        request.session['name'] = User.objects.get(email=email).first_name
        return render(request, 'login/success.html')
    else:
        print 'invalid login'
        return redirect ('/')
