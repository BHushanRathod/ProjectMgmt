from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import utils
from rest_framework.authtoken.models import Token

from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    logout as _logout,login as _login, authenticate, REDIRECT_FIELD_NAME, get_user_model,
)
from django.contrib import messages
from django.views.decorators.http import require_http_methods


class Signup(APIView):
    @staticmethod
    def post(request):
        """
        @author       :BHushan Rathod<abhushanprathod@gmail.com>
        Description   :API for User Registration.
        API URL       :'https://<domain>.co/signup/'
        Method        :'POST'
        :param request:'email', 'username', 'password', 'fullName', 'gender', 'phone', 'bdate'
        :return       : {'success': False, 'message': 'Username already exists'}
                        {'success': False, 'message': 'Email already exists'}
                        {'success': True, 'message': 'User added successfully'}
                        {'success': False, 'message': 'Exception in User add.'}
        """

        print("In post Signup/accounts")
        try:
            # email = request.query_params.get('email')
            # uname = request.query_params.get('username')
            # password = request.query_params.get('password')

            email = request.data['email']
            uname = request.data['username']
            password = request.data['password']

            if User.objects.filter(username=uname).exists():
                return Response({'success': False, 'message': 'Username already exists'})
            elif User.objects.filter(email=email).exists():
                return Response({'success': False, 'message': 'Email already exists'})
            else:
                username = utils.create_username(uname)
                userid = User(username=username, password=make_password(password, salt=None), email=email)
                userid.save()
                token = Token.objects.create(user=userid)
                return Response({'success': True, 'message': 'User added successfully', 'Token': token.key},
                                status=status.HTTP_201_CREATED)
        except Exception as e:
            print({"Exception in Signup/account ": e})
            raise exceptions.bad_request({'success': False, 'message': 'Exception in User add.'})


# class Login(APIView):
#     @staticmethod
#     def get(request):
#         """
#         Call for Manual Login.
#         :param request: 'username', 'password'
#         :return:    {'success': False, 'message': 'Your account is blocked. Please contact admin'}
#                     {'success': True, 'data': user_data}
#                     {'success': False, 'message': 'Please check your username & password'}
#         """
#         print("In Login post/accounts")
#         try:
#             # uname = request.query_params.get('username', None)
#             # pswrd = request.query_params.get('password')
#
#             uname = request.META.get('HTTP_USERNAME')
#             pswrd = request.META.get('HTTP_PASSWORD')
#
#             uid = User.objects.get(Q(username=uname) | Q(email=uname))
#
#             if uid.check_password(pswrd):
#                 return Response({'success': True, 'data': uname}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'success': False, 'message': 'Please check your username & password'}, status=status.HTTP_400_BAD_REQUEST)
#
#         except Exception as e:
#             print({'exception in login/accounts': e})
#             raise exceptions.AuthenticationFailed({'success': False, 'message': 'Invalid parameters'})