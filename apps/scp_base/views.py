
from django.db.models import QuerySet
from urllib.request import Request

from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework import status

from typing import Any, Type, Tuple
from abstracts.paginators import AbstractPageNumberPaginator
from rest_framework.viewsets import ViewSet
from typing import Union, Optional

from abstracts.mixins import ValidationMixin, ResponseMixin
from .serializers import (
    ScpSafeSerializer,
    ScpEuclidSerializer,
    ScpKeterSerializer,
    ScpThaumielSerializer,
    ScpAllSerializer,
    NewsSCPSerializer
)
from .models import (
    SCPSafe,
    SCPEuclid,
    SCPKeter,
    SCPThaumiel,
    SCPAllClasses,
    NewsSCP
)
from abstracts.permissions import ScpBasePermissons


class ScpSafeViewSet(ValidationMixin, ResponseMixin, ViewSet):

    queryset: QuerySet = SCPSafe.objects.all()

    permission_classes = (
        ScpBasePermissons,
        # AllowAny,
    )
    serializer_class = ScpSafeSerializer

    pagination_class: Type[AbstractPageNumberPaginator] = \
        AbstractPageNumberPaginator

    def list(self, request: Request):
        paginator: AbstractPageNumberPaginator = \
            self.pagination_class()

        objects: list[Any] = paginator.paginate_queryset(
            self.queryset,
            request
        )
        serializer: ScpSafeSerializer = \
            ScpSafeSerializer(
                objects,
                many=True
            )
        return self.get_json_response(
            serializer.data,
            paginator
        )

    def create(self, request: Request):
        serializer = ScpSafeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        request.data.pop('image')
        return self.get_json_response(
            {
                'message': 'Объект был добавлен',
                'payload': request.data
            }
        )

    def retrieve(self, request: Request, pk: str) -> Response:

        obj: Optional[SCPSafe] = None

        try:
            obj = self.queryset.get(id=pk)
        except SCPSafe.DoesNotExist:
            return self.get_json_response(
                {
                    'message': 'Объект не найден',
                    'payload': {
                        'invalid_obj_id': f'{pk}'
                    }
                }
            )

        serializer: ScpSafeSerializer = \
            ScpSafeSerializer(
                obj
            )
        request.data.pop('image')
        return self.get_json_response(
            serializer.data
        )

    def update(self, request: Request, pk: str) -> Response:

        obj: SCPSafe = self.get_obj_or_raise(
            p_key=pk, queryset=self.queryset
        )
        serializer: ScpSafeSerializer = \
            ScpSafeSerializer(
                obj,
                data=request.data
            )
        request.data['obj_id'] = obj.pk

        if not serializer.is_valid():
            return self.get_json_response(
                {
                    'message': 'Объект не был обновлен',
                    'payload': request.data
                }
            )

        serializer.save()
        request.data.pop('image')
        return self.get_json_response(
            {
                'message': 'Объект был обновлен',
                'payload': request.data
            }
        )

    def partial_update(self, request: Request, pk: str) -> Response:

        obj: SCPSafe = self.get_obj_or_raise(
            p_key=pk, queryset=self.queryset
        )
        serializer: ScpSafeSerializer = \
            ScpSafeSerializer(
                obj,
                data=request.data,
                partial=True
            )
        request.data['obj_id'] = obj.id

        if not serializer.is_valid():
            return self.get_obj_or_raise(
                {
                    'message': 'Объект не был частично-обновлен',
                    'payload': request.data
                }
            )

        serializer.save()
        request.data.pop('image')
        return self.get_json_response(
            {
                'message': 'Объект был частично-обновлен',
                'payload': request.data
            }
        )

    def destroy(self, request: Request, pk: str) -> Response:

        obj: SCPSafe = self.get_obj_or_raise(
            self.queryset,
            pk
        )

        obj.delete()

        return self.get_json_response(
            {
                'message': 'Объект был удален',
                'payload': {
                    'obj_id': f'{obj.id}',
                    'obj_deleted': f'{obj.datetime_deleted}',
                }
            }
        )


class SCPEuclidViewSet(ScpSafeViewSet):
    queryset: QuerySet = SCPEuclid.objects.all()

    permission_classes = (
        ScpBasePermissons,
        # AllowAny,
    )
    serializer_class = ScpEuclidSerializer

    pagination_class: Type[AbstractPageNumberPaginator] = \
        AbstractPageNumberPaginator

    def list(self, request: Request):
        paginator: AbstractPageNumberPaginator = \
            self.pagination_class()

        objects: list[Any] = paginator.paginate_queryset(
            self.queryset,
            request
        )
        serializer: ScpEuclidSerializer
        return super(SCPEuclidViewSet, self).list(
            request
        )

    def create(self, request: Request):
        serializer = ScpEuclidSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        request.data.pop('image')
        return self.get_json_response(
            {
                'message': 'Объект был добавлен',
                'payload': request.data
            }
        )

    def retrieve(self, request: Request, pk: str) -> Response:
        return super(SCPEuclidViewSet, self).retrieve(
            request, pk
        )

    def update(self, request: Request, pk: str) -> Response:
        return super(SCPEuclidViewSet, self).update(
            request, pk
        )

    def destroy(self, request: Request, pk: str) -> Response:
        return super(SCPEuclidViewSet, self).destroy(
            request, pk
        )


class ScpKeterViewSet(ScpSafeViewSet):
    queryset: QuerySet = SCPKeter.objects.all()

    permission_classes = (
        ScpBasePermissons,
        # AllowAny,
    )
    serializer_class = ScpKeterSerializer

    pagination_class: Type[AbstractPageNumberPaginator] = \
        AbstractPageNumberPaginator

    def list(self, request: Request):
        paginator: AbstractPageNumberPaginator = \
            self.pagination_class()

        objects: list[Any] = paginator.paginate_queryset(
            self.queryset,
            request
        )
        serializer: ScpEuclidSerializer
        return super(ScpKeterViewSet, self).list(
            request
        )

    def create(self, request: Request):
        serializer = ScpKeterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        request.data.pop('image')
        return self.get_json_response(
            {
                'message': 'Объект был добавлен',
                'payload': request.data
            }
        )

    def retrieve(self, request: Request, pk: str) -> Response:
        return super(ScpKeterViewSet, self).retrieve(
            request, pk
        )

    def update(self, request: Request, pk: str) -> Response:
        return super(ScpKeterViewSet, self).update(
            request, pk
        )

    def destroy(self, request: Request, pk: str) -> Response:
        return super(ScpKeterViewSet, self).destroy(
            request, pk
        )


class ScpThaumielViewSet(ScpSafeViewSet):

    queryset = SCPThaumiel.objects.all()

    permission_classes = ScpBasePermissons,

    pagination_class: Type[AbstractPageNumberPaginator] = \
        AbstractPageNumberPaginator

    def list(self, request: Request):
        paginator: AbstractPageNumberPaginator = \
            self.pagination_class()

        objects: list[Any] = paginator.paginate_queryset(
            self.queryset,
            request
        )
        serializer: ScpThaumielSerializer
        return super(ScpThaumielViewSet, self).list(
            request
        )

    def create(self, request: Request):
        serializer = ScpThaumielSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        request.data.pop('image')
        return self.get_json_response(
                {
                    'message': 'Объект был добавлен',
                    'payload': request.data
                }
            )

    def retrieve(self, request: Request, pk: str) -> Response:
        return super(ScpThaumielViewSet, self).retrieve(
            request, pk
        )

    def update(self, request: Request, pk: str) -> Response:
        return super(ScpThaumielViewSet, self).update(
            request, pk
        )

    def destroy(self, request: Request, pk: str) -> Response:
        return super(ScpThaumielViewSet, self).destroy(
            request, pk
        )


class NewsSCPApiView(ValidationMixin, ResponseMixin, ViewSet):
    queryset: QuerySet = NewsSCP.objects.all()

    serializer_class = NewsSCPSerializer

    pagination_class: Type[AbstractPageNumberPaginator] = \
        AbstractPageNumberPaginator

    def list(self, request: Request):
        paginator: AbstractPageNumberPaginator = \
            self.pagination_class()

        objects: list[Any] = paginator.paginate_queryset(
            self.queryset,
            request
        )
        serializer: NewsSCPSerializer = NewsSCPSerializer(
            objects,
            many=True
        )
        return self.get_json_response(
            serializer.data,
            paginator
        )


class TemV(TemplateView):
    template_name = 'html/index.html'
