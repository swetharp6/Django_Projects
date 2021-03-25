from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SignupView.as_view(),name="signup"),
    path('',views.HomePage.as_view(),name="home"),
]