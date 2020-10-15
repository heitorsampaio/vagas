from rest_framework import serializers
from users.models import User
from validate_docbr import CPF


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'cpf', 'password', 'username', 'name']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_username(validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_cpf(self, value):
        cpf_validator = CPF()

        if not cpf_validator.validate(value):
            raise serializers.ValidationError('Invalid CPF.')
        return value
