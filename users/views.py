import datetime
import random
import secrets

from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import OTPCode

@api_view(['GET'])
def test(request):
    return Response(data={'message': 'Hello!!!'})


class OTPView(APIView):
    def post(self, request):
        phone = request.data['phone']
        try:
            user = User.objects.get(username=phone)
        except:
            user = User.objects.create_user(
                username=phone,
                password=str(secrets.token_bytes(10)),
                email='a@n.ru',
                is_active=False
        )
        OTPCode.objects.create(
            user=user,
            code=str(random.randint(1000,9999)),
            valid_until=datetime.datetime.now()+datetime.timedelta(minutes=2)
        )
        return Response(data={'message': 'code created!!!'})


class OTPConfirmView(APIView):
    def post(self, request):
        code = request.data['code']
        otp_list = OTPCode.objects.filter(
            code=code,
            valid_until__gte=datetime.datetime.now()
        )
        if otp_list.count()>0:
            try:
                token = Token.objects.get(user=otp_list[0].user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=otp_list[0].user)
            return Response(data={'key': token.key})
        else:
            return Response(data={'message': 'Invalid code'})