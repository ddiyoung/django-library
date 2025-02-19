from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import GenericAPIView, CreateAPIView
from django.contrib.auth import login, authenticate
from rest_framework.response import Response

from users.serializer import SignInSerializer, SignUpSerializer


# Create your views here.


class SignInView(GenericAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = SignInSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if not user:
            raise AuthenticationFailed("아이디 또는 비밀번호가 일치하지 않습니다.")

        login(request, user)
        return Response()


class SignUpView(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = SignUpSerializer
