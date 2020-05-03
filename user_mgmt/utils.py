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
