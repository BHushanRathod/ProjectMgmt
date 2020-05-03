"""Task Manager URL Configuration

"""
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views
app_name = 'user_mgmt'

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('signup/', views.Signup.as_view(), name='signup'),

    # path('logout/', views.logout, name='logout'),
]
