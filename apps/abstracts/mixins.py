from typing import Any

from rest_framework.response import Response
from django.db.models import QuerySet
from typing import Union, Optional


from abstracts.validations import APIValidator
from abstracts.paginators import AbstractPageNumberPaginator, AbstractLimitOffsetPaginator


class ResponseMixin:
    """ResponseMixin."""

    def get_json_response(
        self,
        data: dict[Any, Any],
        paginator: Optional[
            Union[
                AbstractPageNumberPaginator,
                AbstractLimitOffsetPaginator
            ]
        ] = None
    ) -> Response:

        if paginator:
            return paginator.get_paginated_response(
                data
            )
        return Response(
            {
                'results': data
            }
        )


class ValidationMixin:
    """ValidationMixin"""

    def get_obj_or_raise(
        self,
        queryset: QuerySet,
        p_key: str
    ) -> None:

        obj: Any = queryset.get_obj(
            p_key
        )
        if not obj:
            raise APIValidator(
                f'Объект не найден: {p_key}',
                'error',
                '404'
            )
        return obj
