from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Device
from .serializer import UserSerializer
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .decorators import require_api_key

# Create your views here.

@csrf_exempt
@require_api_key
@api_view(['POST'])
def register_device(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@require_api_key
@api_view(['GET', 'PATCH', 'DELETE'])
def device(request, pk):
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(device)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = UserSerializer(device, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    