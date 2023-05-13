from django.urls import path
from u_auth import views

urlpatterns = [
    path('sign-in/',views.sign_in,name='sign-in'),
    path('',views.dashboard,name='dashboard'),
]