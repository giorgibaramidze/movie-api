from rest_framework import serializers
from .models import Account


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = Account
        fields = ["email", "first_name", "last_name", "password", "password2"]
        
    
    def validate(self, data):
        password1 = data.get('password')
        password2 = data.get('password2')

        if password1 != password2:
            raise serializers.ValidationError('Passwords do not match.')
        if len(password1) < 7 or len(password2) < 7:
            raise serializers.ValidationError("Passwords must contain at least 8 characters")
        return data

    def create(self, validated_data):
        user = Account.objects.create(email=validated_data['email'],
                                       first_name=validated_data['first_name'],
                                       last_name=validated_data['last_name']
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user