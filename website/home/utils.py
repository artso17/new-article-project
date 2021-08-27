from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

import six
import random
import string


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(user.is_active))


def code_generator(size=5, char=string.ascii_letters+string.digits):
    return ''.join(random.sample(char, size))


def check_code(instance):
    code = code_generator()
    qs_exist = instance.__class__.objects.filter(shortcode=code).exists()
    if qs_exist:
        return check_code()
    return code
