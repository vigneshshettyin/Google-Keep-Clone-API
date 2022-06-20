import http

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

class RegisterAPIView(APIView):
    serializer_class = UserRegisterSerializer

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = self.get_tokens_for_user(user)
            return Response(response_data, status=http.HTTPStatus.CREATED)
        return Response(serializer.errors, status=http.HTTPStatus.BAD_REQUEST)


class LogoutAPIView(APIView):
## Use of breakpoint()
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=http.HTTPStatus.OK)
        except Exception as e:
            return Response(status=http.HTTPStatus.BAD_REQUEST)
