from rest_framework import serializers

from users.models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(
        max_length=100,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = CustomUser
        fields = (
            '__all__'
        )

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
