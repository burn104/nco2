from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('auth/', views.OTPView.as_view()),
    path('confirm/', views.OTPConfirmView.as_view()),
]
