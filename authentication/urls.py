from django.urls import path
from .views import CompletePasswordReset, LoginView, LogoutView, RegisterView, RequestPasswordResetEmail, UsernameValidationView,EmailValidationView,VerificationView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path('validate-username',csrf_exempt(UsernameValidationView.as_view()),name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),name='validate_email'),
    path('activate/<uidb64>/<token>',VerificationView.as_view(), name='activate'),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('request-reset-link',RequestPasswordResetEmail.as_view(), name="request-password"),
    path('set-new-password/<uidb64>/<token>',CompletePasswordReset.as_view(), name="reset-user-password")
]