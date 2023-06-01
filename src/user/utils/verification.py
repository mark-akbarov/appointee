from random import randint
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from core.utils.email import send_email
from ..models import VerifyUser, BaseUser


def send_user_verify_code(user, is_forgot_password=False):
    code = randint(100_000, 999_999)
    if is_forgot_password is False:
        VerifyUser.objects.create(
            user=user,
            code=f'verify_username_{code}',
            is_active=False
        )
    elif is_forgot_password is True:
        VerifyUser.objects.create(
            user=user,
            code=f'forgot_password_{code}',
            is_active=False
        )
    send_email(user.email, code)


def check_verify_signup_code(email, code):
    check = VerifyUser.objects.filter(
        user__email=email,
        code=f'verify_username_{code}',
        is_active=False
    )
    if check.exists():
        verify = check.first()
        verify.is_active = True
        verify.save()
        user = verify.user
        user.is_active = True
        user.save()

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'detail': 'invalid code'}, status=status.HTTP_400_BAD_REQUEST)



def check_verify_forgot_password_code(email, code):
    check = VerifyUser.objects.filter(
        user__email=email,
        code=f'forgot_password_{code}',
        is_active=False
    )
    return check.exists()


def re_send_verify_user_code(email):
    try:
        user = BaseUser.objects.get(email=email)
        send_user_verify_code(user)
        return Response({'detail': 'successfully send new code'})
    except BaseUser.DoesNotExist:
        return Response({'detail': 'username does not exist'}, status=status.HTTP_400_BAD_REQUEST)
