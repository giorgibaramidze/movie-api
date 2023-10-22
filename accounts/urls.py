from accounts import views
from django.urls import path


urlpatterns = [
    path('login/', views.LoginAPI.as_view(), name="login")
]
