from rest_framework import serializers
from hospital.models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username','name','first_name','last_name','email','password','role')
    
    def validate(self,attrs):
        username = attrs['username']
        email = attrs['email']
        password = attrs['password']
        if Users.objects.filter(username =username).exists():
            return serializers.ValidationError('Username already exist')
        if Users.objects.filter(email =email).exists():
            return serializers.ValidationError('Email already used')
        
        if len(password)<6:
            return serializers.ValidationError('Password length must be atleast 6 character')

        return attrs
    def create(self,validated_data):
        user = Users.objects.create(
            username = validated_data['username'],
            role = validated_data['role'],
            email = validated_data['email'],
            name = validated_data['name'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user