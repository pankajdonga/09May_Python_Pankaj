from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.login),
    path('index/',views.index),
    path('signup/',views.signup),
    path('verifyotp/',views.verifyotp),
    path('invoice/',views.invoice),
    path('notice/',views.notice),
    path('event/',views.event),
    path('societymember/',views.societymember),
    path('watchman/',views.watchman),
    path('profile/',views.profile),
]