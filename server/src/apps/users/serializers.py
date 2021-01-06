from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            name=validated_data['name'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# class CustomUserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ['id', 'name', 'username', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User(
#             name=validated_data['name'],
#             username=validated_data['username'],
#         )
#         user.set_password(validated_data['password'])
#         user.id = validated_data['id']
#         user.save()
#         return user
