from rest_framework.authtoken.models import Token


def get_user(request):
    if request.META.get('HTTP_AUTHORIZATION', None):
        token = Token.objects.get(key=request.META.get('HTTP_AUTHORIZATION')[6:])
        return token.user_id
