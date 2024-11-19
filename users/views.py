from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serliazers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny, )

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


# class UserSetView(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     permission_classes = CustomPagination
#     permission_classes = (IsAuthenticated, )
