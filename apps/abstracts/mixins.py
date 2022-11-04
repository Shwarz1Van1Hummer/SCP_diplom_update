from typing import Any

from rest_framework.response import Response
from django.db.models import QuerySet

from abstracts.validations import APIValidator


class ResponseMixin:
    """ResponseMixin."""

    def get_json_response(
        self,
        data: dict[Any, Any],

    ) -> Response:

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
