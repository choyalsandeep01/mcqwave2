from django.contrib import admin
from django.urls import path, include
from accounts.views import sign_up, log_in, activate_email,password_reset_request,password_reset_confirm
from home.views import home_view

urlpatterns = [
    path('', sign_up, name='signup' ),
    path('login/', log_in, name='login' ),
    path('accounts/activate/<email_token>/' , activate_email , name="activate_email"),
    path('<uuid:uuid>/', home_view, name='go_to_home'),
    path('login/password-reset/', password_reset_request, name='password_reset_request'),
    path('password-reset-confirm/<str:token>/', password_reset_confirm, name='password_reset_confirm'),
]
