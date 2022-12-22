from rest_framework.permissions import AllowAny
from abstracts.mixins import ValidationMixin, ResponseMixin
from django.db.models import QuerySet
from rest_framework.viewsets import ViewSet
from .models import News
from .serializers import SerializerNews
from abstracts.paginators import AbstractPageNumberPaginator
from typing import Any, Type, Tuple, Optional
from urllib.request import Request


class NewsViewSet(ValidationMixin, ResponseMixin, ViewSet):

    queryset: QuerySet = News.objects.all()

    permission_classes = (
        AllowAny,
    )

    serializer_class = SerializerNews

    pagination_class: Type[AbstractPageNumberPaginator] = \
        AbstractPageNumberPaginator

    def list(self, request: Request):
        paginator: AbstractPageNumberPaginator = \
            self.pagination_class()

        objects: list[Any] = paginator.paginate_queryset(
            self.queryset,
            request
        )
        serializer: SerializerNews = \
            SerializerNews(
                objects,
                many=True
            )
        return self.get_json_response(
            serializer.data,
            paginator
        )

    def create(self, request: Request):
        serializer = SerializerNews(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return self.get_json_response(
            {
                'message': 'Объект был добавлен',
                'payload': request.data
            }
        )
