from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RecordSerializer


@api_view(["POST"])
def record_list(request):
    serializer = RecordSerializer(data=request.data)
    if serializer.is_valid():
        return Response(request.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)