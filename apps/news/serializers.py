from rest_framework.serializers import (
    CharField,
    ModelSerializer
)
from .models import News


class SerializerNews(ModelSerializer):
    title_news = CharField(required=False)
    descriptions = CharField(required=False)
    date = CharField(required=False)

    class Meta:
        models = News
        fields = '__all__'
