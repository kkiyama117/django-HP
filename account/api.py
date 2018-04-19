from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import User
from .serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = UserSerializer

    def get_queryset(self):
        """ スーパーユーザーかによって判断

        Returns:
            クエリセット
        """
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.all_for_instance(self.request.user)
