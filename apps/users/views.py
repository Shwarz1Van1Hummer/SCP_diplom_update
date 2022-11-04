from django.db.models import QuerySet
from urllib.request import Request

from rest_framework.viewsets import ViewSet

from abstracts.mixins import ValidationMixin, ResponseMixin
from .serializers import RegistrationSerializer
from .models import CustomUser
from abstracts.permissions import UserPermissions


class RegistrationAPIView(ValidationMixin, ResponseMixin, ViewSet):
    queryset: QuerySet = CustomUser.objects.all()

    permission_classes = (
        UserPermissions,
    )
    serializer_class = RegistrationSerializer

    def list(self, request: Request):
        serializer: RegistrationSerializer = RegistrationSerializer(
            self.queryset,
            many=True
        )
        return self.get_json_response(
            serializer.data
        )

    def create(self, request: Request):
        serializer: RegistrationSerializer = \
            RegistrationSerializer(
                data=request.data
            )

        if not serializer.is_valid():
            return self.get_json_response(
                {
                    'message': 'Объект: не был создан',
                    'playload': {}
                }
            )
        serializer.save()

        return self.get_json_response(
            {
                'message': 'Объект был создан',
            }
        )


