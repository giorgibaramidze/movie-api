from accounts import views
from django.urls import path



urlpatterns = [
    path('jwt/create/', views.CustomTokenObtainPairView.as_view()),
    path('jwt/refresh/', views.CustomTokenRefreshView.as_view()),
    path('jwt/verify/', views.CustomTokenVerifyView.as_view()),
    path('logout/', views.LogoutView.as_view()),
]
