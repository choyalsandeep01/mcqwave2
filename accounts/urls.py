from django.contrib import admin
from django.urls import path, include
from accounts.views import sign_up, log_in, activate_email
from home.views import home_view

urlpatterns = [
    path('', sign_up, name='signup' ),
    path('login/', log_in, name='login' ),
    path('accounts/activate/<email_token>/' , activate_email , name="activate_email"),
    path('<uuid:uuid>/', home_view, name='go_to_home')
    
]
