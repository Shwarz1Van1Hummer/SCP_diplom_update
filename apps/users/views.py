from django.db.models import QuerySet
from urllib.request import Request

from rest_framework.viewsets import ViewSet

from abstracts.mixins import ValidationMixin, ResponseMixin
from .serializers import RegistrationSerializer
from .models import CustomUser
from abstracts.permissions import UserPermissions
from typing import Any, Type, Tuple
from abstracts.paginators import AbstractPageNumberPaginator


class RegistrationAPIView(ValidationMixin, ResponseMixin, ViewSet):
    queryset: QuerySet = CustomUser.objects.all()

    serializer_class = RegistrationSerializer

    pagination_class: Type[AbstractPageNumberPaginator] = \
        AbstractPageNumberPaginator

    def list(self, request: Request):
        paginator: AbstractPageNumberPaginator = \
            self.pagination_class()

        objects: list[Any] = paginator.paginate_queryset(
            self.queryset,
            request
        )
        serializer: RegistrationSerializer = RegistrationSerializer(
            objects,
            many=True
        )
        return self.get_json_response(
            serializer.data,
            paginator
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


