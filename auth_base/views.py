from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
import re
from django.core.mail import send_mail
from django.http import HttpResponse
from .serializers import EmailSerializer, CodeVerificationSerializer, SessionSerializer
import random
import string
import jwt
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.conf import settings
from .generate_token import generate_access_token
# Create your views here.



class EmailValidatorandMailSender(APIView):
    verification_code = ''.join(random.choices(string.ascii_lowercase, k=5))
    def validate_email(self, email):
        # Step 1: Check email format with regex
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        if not re.match(email_pattern, email):
            return False
        
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            is_valid = self.validate_email(email)
            if is_valid:
                send_mail(
                    'New Visitor',
                    'This is the verification code' + EmailValidatorandMailSender.verification_code,
                    'settings.EMAIL_HOST_USER',
                    [email],
                    fail_silently=False,
                )
                CodeVerification.verify_code(
                    request, EmailValidatorandMailSender.verification_code, email)
            else:
                return Response({'message': f'{email} is not a valid email address.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    pass

class CodeVerification(APIView):
    def verify_code(self, request, verification_code, email):
        serializer = CodeVerificationSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data.get('code')
            if code == verification_code:
                user_token = generate_access_token(email)
                response = Response()
                response.set_cookie(key='access_token',
                                    value=user_token, httponly=True)
                response.data = {
                    'access_token': user_token
                }
                return Response({'message': f'User is verified.'}, response, status=status.HTTP_200_OK)
            else:
                return Response({'message': f'User is not verified.'}, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


