from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import user
from .serializer import UserSerializer
# Create your views here.
# ---------------------------------------------
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# ------------------------Testing--------------
@api_view(['GET','PUT','DELETE'])
def get_users(request,pk):
    try:
        User=user.objects.get(pk=pk)
    except user.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = UserSerializer(User)
        return Response(serializer.data)
    if request.method=='PUT':
        serializer = UserSerializer(User,data=request.data)
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        User.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)