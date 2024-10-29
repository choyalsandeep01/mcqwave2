from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .models import Profile
from django.urls import reverse

def sign_up(request):
    if request.user.is_authenticated:
        # Redirect to the mcq page with the UUID
        user_uuid = request.user.profile.email_token
        return redirect(reverse('go_to_home', kwargs={'uuid': user_uuid})) 
        
    # if request.user.is_authenticated:
    #     messages.warning(request, 'You are already logged in. Do you want to log out?')
    #     return redirect('/home')

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = username)
        if first_name=='' or last_name=='' or username=='' or email=='' or password=='':
            messages.warning(request, 'Please enter all the details.')
            return HttpResponseRedirect(request.path_info)
        if user_obj.exists():
            messages.warning(request, 'Username is already taken.')
            return HttpResponseRedirect(request.path_info)
        if User.objects.filter(email = email):
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)
        

        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = username)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)
    return render(request, 'accounts/signup.html')


def log_in(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = username)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)

        
        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)


        

        user_obj = authenticate(username = username , password= password)
        if user_obj:
            login(request , user_obj)
            print(user_obj)
            user_uuid = user_obj.profile.email_token
            print(user_uuid)
            return redirect(reverse('go_to_home', kwargs={'uuid': user_uuid}))
            
            
            
        

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)
    return render(request, 'accounts/login.html')


def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')