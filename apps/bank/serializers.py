from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    IntegerField,
    DateField,
    FloatField,
    DecimalField
)
from bank.models import Account, Transactions, Card


class AccountSerializer(ModelSerializer):
    owner = CharField(required=False)
    number = IntegerField(required=False)
    date = DateField(required=False)
    balance = FloatField(required=False)

    class Meta:
        model = Account
        fields = (
            '__all__'
        )


class TransactionsSerializer(ModelSerializer):
    sender = CharField(required=False)
    receiver = CharField(required=False)
    date = DateField(required=False)
    status = CharField(required=False)
    amount = CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(TransactionsSerializer, self).__init__(*args, **kwargs)
        if 'request' in self.context:
            self.fields['account'].queryset = self.fields['account'] \
                .queryset.filter(user=self.context['view'].request.user)

    class Meta:
        model = Transactions
        fields = (
            '__all__'
        )


class CardSerializer(ModelSerializer):
    account = CharField(required=False)
    number = IntegerField(required=False)
    cvv_code = CharField(required=False)
    expirations_date = DateField(required=False)
    balance = FloatField(required=False)

    class Meta:
        model = Card
        fields = (
            '__all__'
        )
