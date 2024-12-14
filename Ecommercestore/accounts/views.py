from django.shortcuts import render
from django.shortcuts import render

from django.http import HttpResponse

def accounttest(request):
    return HttpResponse(" account app is connected")

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Signup Function
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            messages.success(request, "Registration successful!")
            return redirect('dashboard')  # Redirect to the dashboard after signup
        else:
            messages.error(request, "Error during registration. Please try again.")
    else:
        form = UserCreationForm()
       

    return render(request, 'accounts/signup.html', {'form': form})


# Login Function
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, "Login successful!")
                return redirect('dashboard')  # Redirect to the dashboard after login
            else:
                messages.error(request, "Invalid credentials. Please try again.")
        else:
            messages.error(request, "Invalid credentials. Please try again.")
    else:
        form = AuthenticationForm()
       

    return render(request, 'accounts/login.html', {'form': form})
