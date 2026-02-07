from rest_framework import serializers
from hospital.models import Users,Inquries,Doctor

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


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquries
        fields = '__all__' 
    

    def validate(self,attrs):
        inquiry_details = attrs['inquiries_details']
        if len(inquiry_details)<50:# for learning purpose
            return serializers.ValidationError('Inquiries details should be atleast 50 characters')

        return attrs
    
    def create(self,validated_data):
        inquries = Inquries.objects.create(
            patient_name = validated_data['patient_name'],
            location = validated_data['location'],
            inquiries_details = validated_data['inquiries_details'],
            status = validated_data['status']
        )
        
        return inquries

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
    
    def validate(self,attrs):
        user_id = attrs['user_id']
        if Doctor.objects.filter(user_id = user_id).exists():
            return serializers.ValidationError('Doctor already exists')
        
        if  Users.objects.filter(id = user_id).first() is None:
            return serializers.ValidationError('User does not exists')
        

        return attrs
    
    def create(self,validated_data):
        doctor = Doctor.objects.create(
            name = validated_data['name'],
            user_id = validated_data['user_id'],
            availability = validated_data['availability'],
            specialization = validated_data['specialization']
        )

        return doctor