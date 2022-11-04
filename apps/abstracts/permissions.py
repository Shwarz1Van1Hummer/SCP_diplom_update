from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class UserPermissions(BasePermission):
    """TempPermissions."""

    def __init__(self) -> None:
        self._admin: bool = False
        self._user: bool = False

    def _init_permissions(self, request: Request) -> None:

        self._user = (
            request.user and
            request.user.is_active
        )
        self._admin = self._user and (
            request.user.is_staff and
            request.user.is_superuser
        )

    def has_permission(self, request: Request, view: 'RegistrationAPIView') -> bool:

        self._init_permissions(request)

        basic_endpoints: list[str] = [
            'list',
        ]
        advanced_endpoints: list[str] = [
            'create',
        ]
        if view.action in basic_endpoints:
            return self._user

        if view.action in advanced_endpoints:
            return self._admin

        return False


class ScpBasePermissons(BasePermission):
    def __init__(self) -> None:
        self._admin: bool = False
        self._user: bool = False

    def _init_permissions(self, request: Request) -> None:

        self._user = (
            request.user and
            request.user.is_active
        )
        self._admin = self._user and (
            request.user.is_staff and
            request.user.is_superuser
        )

    def has_permission(self, request: Request, view: 'ScpSafeViewSet') -> bool:

        self._init_permissions(request)

        basic_endpoints: list[str] = [
            'list',
        ]
        advanced_endpoints: list[str] = [
            'create',
            'update',
            'retrieve',
            'destroy',
            'partial_update',
        ]
        if view.action in basic_endpoints:
            return self._user

        if view.action in advanced_endpoints:
            return self._admin

        return False


class AccountPermissions(ScpBasePermissons):

    def has_permission(self, request: Request, view: 'AccountViewSet') -> bool:
        return False
