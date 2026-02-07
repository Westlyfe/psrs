from django.shortcuts import render
from hospital.serializer import UsersSerializer,InquirySerializer,DoctorSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from hospital.permission import IsAdmin,IsDoctor,IsPatient
# Create your views here.

@api_view(['POST'])
@permission_classes([IsDoctor])
def create_user(request):
    serializer = UsersSerializer(data = request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(
            {
                "message":"User created successfully",
                "data":UsersSerializer(user).data
            },
            status = status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors,status = status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None and password is None:
        return Response(
            {
                "message":"Username or password is required"
            },
            status = status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(username = username,password =password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "access_token":str(refresh.access_token),
                "refresh_token":str(refresh)
            },
            status = status.HTTP_200_OK
        )
    return Response(
        {
            "Details":"Incorrect username or password"
        },
        status = status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
def create_inquiries(request):
    serializer = InquirySerializer(data = request.data)
    if serializer.is_valid():
        inquiry = serializer.save()
        return Response(
            {
                "message":"Inquiry created successfully",
                "data":InquirySerializer(inquiry).data
            },
            status = status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors,status = status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
@permission_classes([IsAdmin])
def create_doctor(request):
    serializer = DoctorSerializer(data = request.data)
    if serializer.is_valid():
        doctor = serializer.save()
        return Response(
            {
                "message":"Doctor created successfully",
                "data":DoctorSerializer(doctor).data
            },
            status = status.HTTP_201_CREATED
        )
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAdmin,IsDoctor])
def doctor_availability(request):
    doctor = Doctor.objects.all()
    return Response(
        {
            "data":DoctorSeriliazer(doctor).data
        },
        status = status.HTTP_200_OK

    )