from django.urls import path
from .views import SignUpView
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('', SignUpView.as_view(), name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
]
