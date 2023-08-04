from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                # Redirect to a page after successful login
                return redirect('dashboard')
            else:
                form.add_error(None, 'Invalid credentials. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required()
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


@login_required
def sign_out(request):
    logout(request)
    return redirect('login')  # Replace 'login' with the URL name for your login page