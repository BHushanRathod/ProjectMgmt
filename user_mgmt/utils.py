# import json
# import re
#
# import requests
# import sys
# import random
# from django.contrib.auth.models import User
# from django.utils import timezone
# from rest_framework import pagination, exceptions
# from rest_framework.response import Response
#
# from .authentication import JSONWebTokenAuthentication
# from .models import UserProfile, Follower
#
#
#
# class CustomPagination(pagination.PageNumberPagination):
#     """
#    discription : Pagination settings
#    """
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 100
#
#     def __init__(self, page_size=20):
#         self.page_size = page_size
#
#     def get_paginated_response(self, data):
#         return Response({
#             'next': self.get_next_link(),
#             'previous': self.get_previous_link(),
#             'count': self.page.paginator.count,
#             'pages': self.page.paginator.num_pages,
#             'results': data
#         })
#
#     def get_paginate_result(self, data):
#         return ({
#             'next': self.get_next_link(),
#             'previous': self.get_previous_link(),
#             'count': self.page.paginator.count,
#             'pages': self.page.paginator.num_pages,
#             'results': data
#         })
#
#
# def return_paginated_response(request, page_size, serializer_name, query_set):
#     pagination_class = CustomPagination
#     paginator = pagination_class(page_size)
#     page = paginator.paginate_queryset(query_set, request)
#     serializer = serializer_name(page, many=True)
#     return paginator.get_paginated_response(serializer.data)
#
#
# def return_paginated_result(request, page_size, serializer_name, query_set):
#     pagination_class = CustomPagination
#     paginator = pagination_class(page_size)
#     page = paginator.paginate_queryset(query_set, request)
#     serializer = serializer_name(page, many=True)
#     return paginator.get_paginate_result(serializer.data)
#
#
# def return_paginated_response_with_context(request, page_size, serializer_name, query_set, context):
#     pagination_class = CustomPagination
#     paginator = pagination_class(page_size)
#     page = paginator.paginate_queryset(query_set, request)
#     serializer = serializer_name(page, context=context, many=True)
#     return paginator.get_paginated_response(serializer.data)
#
#
# def return_user_obj(request, uname):
#     token = JSONWebTokenAuthentication.jwt_token_encode(request, uname)
#     uid, profile = get_user_userprofile_object(uname)
#     user_data = {
#         'token': token,
#         'userName': uid.username,
#         'fullName': profile.fullname,
#         'user_pic': profile.user_pic,
#         'stepCount': profile.step_complete
#     }
#     uid.last_login = timezone.now()
#     uid.save()
#     return user_data
#
#
import random
import re

from django.contrib.auth.models import User


def create_username(name):
    try:
        if '@' in name:
            username = name.split('@')[0]
            username1 = re.sub(r'[^a-zA-Z0-9-]', r'', username)
            username = username1.replace(" ", "")

            if is_username_exists(username):
                return str(username + random.randint(111, 999))
            else:
                return str(username)
        else:
            username1 = re.sub(r'[^a-zA-Z0-9-]', r'', name)
            username = username1.replace(" ", "")
            if is_username_exists(username):
                return str(username + random.randint(111, 999))
            else:
                return str(username)

    except Exception as e:
        print({"Exception in create_username/utils/accounts": e})
        return str(name)


def is_username_exists(name):
    if User.objects.filter(username=name).exists():
        return True
    else:
        return False
#
#
#
#
# def get_user_userprofile_object(username):
#     try:
#         user = User.objects.get(username=username)
#         userprofile = UserProfile.objects.get(userid=user)
#         return user, userprofile
#     except (User.DoesNotExist, UserProfile.DoesNotExist):
#         raise exceptions.NotFound
#
#
# def get_user_role(username):
#     try:
#         user, userprofile = get_user_userprofile_object(username)
#         return userprofile.role
#     except (User.DoesNotExist, UserProfile.DoesNotExist):
#         raise exceptions.NotFound
#
