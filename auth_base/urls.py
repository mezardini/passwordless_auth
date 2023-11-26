from django.urls import path
from .views import SessionAPIView, EmailValidatorandMailSender, CodeVerification

urlpatterns = [
    path('api/session/', SessionAPIView.as_view(), name='session-api'),
    path('api/validate-email/', EmailValidatorandMailSender.as_view(),
         name='validate-email'),
    path('api/verify-code/', CodeVerification.as_view(),
         name='verify-code')
]
