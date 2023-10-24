from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Account
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "You have successfully registered"})


class LoginAPI(APIView):
    
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data['email']
            password = serializer.data['password']
            
            user = authenticate(email=email, password=password)
            
            if user is None:
                return Response({
                'status': 400,
                'message' : 'invalid password',
                'data': {}
                })

            refresh = RefreshToken.for_user(user)
            
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
            
        return Response({
            'status': 400,
            'message' : 'something went wrong',
            'data': serializer.errors
        })