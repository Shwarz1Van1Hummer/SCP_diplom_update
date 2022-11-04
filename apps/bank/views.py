from django.db.models import QuerySet
from urllib.request import Request
from rest_framework.response import Response

from rest_framework.viewsets import ViewSet

from abstracts.mixins import ValidationMixin, ResponseMixin

from .serializers import (
    AccountSerializer,
    CardSerializer,
    TransactionsSerializer
)

from .models import (
    Card,
    Account,
    Transactions
)

from abstracts.permossions import AccountPermissions
from scp_base.views import ScpSafeViewSet


class AccountViewSet(ScpSafeViewSet):

    queryset: QuerySet = Account.objects.all()

    permission_classes = AccountPermissions

    serializer_class = AccountSerializer

    def list(self, request: Request):
        serializer: AccountSerializer
        return super(AccountViewSet, self).list(
            request
        )

    def create(self, request: Request):
        serializer = AccountSerializer(data=request.data)
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
        return super(AccountViewSet, self).retrieve(
            request, pk
        )

    def update(self, request: Request, pk: str) -> Response:
        return super(AccountViewSet, self).update(
            request, pk
        )

    def destroy(self, request: Request, pk: str) -> Response:
        return super(AccountViewSet, self).destroy(
            request, pk
        )


class CardViewSet(ScpSafeViewSet):

    queryset: QuerySet = Card.objects.all()

    permission_classes = AccountPermissions

    serializer_class = CardSerializer

    def list(self, request: Request):
        serializer: CardSerializer
        return super(CardViewSet, self).list(
            request
        )

    def create(self, request: Request):
        serializer = CardSerializer(data=request.data)
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
        return super(CardViewSet, self).retrieve(
            request, pk
        )

    def update(self, request: Request, pk: str) -> Response:
        return super(CardViewSet, self).update(
            request, pk
        )

    def destroy(self, request: Request, pk: str) -> Response:
        return super(CardViewSet, self).destroy(
            request, pk
        )


class TransactionViewSet(ScpSafeViewSet):

    queryset: QuerySet = Transactions.objects.all()

    permission_classes = AccountPermissions

    serializer_class = TransactionsSerializer

    def list(self, request: Request):
        serializer: TransactionsSerializer
        return super(TransactionViewSet, self).list(
            request
        )

    def create(self, request: Request):
        serializer = TransactionsSerializer(data=request.data)
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
        return super(TransactionViewSet, self).retrieve(
            request, pk
        )

    def update(self, request: Request, pk: str) -> Response:
        return super(TransactionViewSet, self).update(
            request, pk
        )

    def destroy(self, request: Request, pk: str) -> Response:
        return super(TransactionViewSet, self).destroy(
            request, pk
        )
