#from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from django.http.response import JsonResponse

from MessageApp.models import Messages
from MessageApp.serializers import MessageSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def message_api(request):
    if request.method == 'GET':
        messages = Messages.objects.all()
        serializer = MessageSerializer(messages, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def message_details(request, id):

    try:
        message = Messages.objects.get(pk=id)
    except Messages.DoesNotExist:
        return Response(Status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MessageSerializer(message)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


