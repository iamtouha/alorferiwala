from django.shortcuts import render,redirect, get_object_or_404
from .models import UserProfile
from products.models import Product
from orders.models import Order
from orders.views import fraction
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
        owned_books = Product.objects.order_by('-updated_at').filter(current_owner = request.user )
        ordered_books = Order.objects.order_by('-time').filter(ordered_by = request.user, is_confirmed=False )
        for books in owned_books:
            books.buying_price = int(books.init_price * fraction ** (books.sold_count - 1))
        context = {
            'profile': profile,
            'owned_books' : owned_books,
            'ordered_books' : ordered_books,
        }
        return render(request, 'profiles/profile.html', context)
    else:
        return redirect('login')

def user_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile = UserProfile.objects.get(user__id=user_id)
    if not profile.profile_img:
        profile.profile_img = None
    context = {
        'name' : f"{user.first_name} {user.last_name}",
        'phone' : f"+880{profile.phone}",
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
            first_name, last_name = name
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

            if password != repeat_password:
                messages.error(request, "passwords do not match")
                return redirect('register')

            elif len(password)<8:
                messages.error(request, "password must be at least 8 characters")
                return redirect('register')
            else:
                user_obj = User.objects
                if user_obj.filter(username = username).exists():
                    messages.error(request, "Username is taken")
                    return redirect('register')

                elif user_obj.filter(email = email).exists():
                    messages.error(request, "Email already exists")
                    return redirect('register')
                
                elif UserProfile.objects.filter(phone = phone_no).exists():
                    messages.error(request, "Phone No. already exists")
                    return redirect('register')

                else:
                    user = user_obj.create_user(
                        username = username, 
                        password = password,
                        first_name = first_name, 
                        last_name = last_name,
                        email = email
                        )
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
                messages.error(request, "Invalid Form Submission")
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