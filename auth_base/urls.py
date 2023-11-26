from django.urls import path
from .views import SessionAPIView, EmailValidatorandMailSender

urlpatterns = [
    path('api/session/', SessionAPIView.as_view(), name='session-api'),
    path('api/emailvalidator/', EmailValidatorandMailSender.as_view(), name='email_validator')

]
