from django.shortcuts import render,redirect, get_object_or_404
from .models import UserProfile
from .forms import RegisterForm, LoginForm
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user_id=request.user.id)
        context = {
            'profile': profile
        }
        return render(request, 'profiles/profile.html', context)
    else:
        return redirect('login')

def user_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile = UserProfile.objects.get(user__id=user_id)
    context = {
        'name' : user.first_name + ' ' + user.last_name,
        'phone' : '+880' + str(profile.phone),
        'address' : profile.address,
        'photo' : profile.profile_img,
    }
    return render(request, 'profiles/user_profile.html', context)
    
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            name = full_name.split(" ", 1)
            username = form.cleaned_data['username']
            address = form.cleaned_data['address']
            phone_no = form.cleaned_data['phone_no']
            if 'picture' in request.FILES:
                photo = request.FILES['picture']
            else:
                photo = ''
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']

            if password == repeat_password:
                if User.objects.filter(username = username).exists():
                    messages.error(request, "Username is taken")
                    return redirect('register')
                else:
                    if User.objects.filter(email = email).exists():
                        messages.error(request, "Email already exists")
                        return redirect('register')
                    else:
                        user = User.objects.create_user(
                            username = username, 
                            password = password,
                            first_name = name[0], 
                            last_name = name[1],
                            email = email)
                        user.save()
                        profile = UserProfile(
                            user = user,
                            address  = address,
                            phone = phone_no,
                            profile_img = photo
                        )
                        profile.save()
                        messages.success(request, 'You are now registered and can login')
                        return redirect('login')
            else:
                messages.error(request, "passwords do not match")
                return redirect('register')
        else:
            return redirect('register')
    else:        
        if request.user.is_authenticated:
            return redirect('index')
        else:
            context = {
                'form': RegisterForm
            }
            return render(request, 'profiles/register.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username = username, password = password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('index')
                else:
                    return redirect('login')
                    messages.error(request, "Invalid Credentials")
            else:
                return redirect('login')
        else:
            context = {
                'form': LoginForm
            }
            return render(request, 'profiles/login.html', context)

def logOut(request):
    logout(request)
    messages.success(request, 'You are now logged Out')
    return redirect('login')