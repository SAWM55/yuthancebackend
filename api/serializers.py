# from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     pass
    # email = serializers.EmailField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )
    # username = serializers.CharField(
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )
    # phone_number = serializers.CharField(
    #     required=True,
    #     min_length=9,
    #     validators=[UniqueValidator(queryset=User.objects.all())],
    # )
    # password = serializers.CharField(min_length=8)

    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         validated_data['username'],
    #         validated_data['email'],
    #         validated_data['phone_number'],
    #         validated_data['password']
    #     )
    #     return user

    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'email', 'phone_number', 'password')