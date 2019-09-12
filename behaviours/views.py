from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from behaviours.models import Behaviour
from behaviours.serializers import BehaviourSerializer

import random

@api_view(['GET', 'POST'])
def behaviour_list(request, format=None):
    """
    List all behaviours, or create a new behaviour
    """
    if request.method == 'GET':
        behaviours = Behaviour.objects.all()
        serializer = BehaviourSerializer(behaviours, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BehaviourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def behaviour_detail(request, pk, format=None):
    """
    Retrieve, update or delete a behaviour
    """
    try:
        behaviour = Behaviour.objects.get(pk=pk)
    except Behaviour.DoesNotExist:
        return Response(status=status_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BehaviourSerializer(behaviour)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BehaviourSerializer(behaviour, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        behaviour.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def sequence_detail(request, length, seed=None, format=None):
    """
    Retrieve, update or delete a behaviour
    """
    # TODO Add exception handler when for length being larger than total tricks.
    if request.method == 'GET':
        if seed is not None:
            random.seed(seed)
        behaviours = random.sample(list(Behaviour.objects.all()), length)

        serializer = BehaviourSerializer(behaviours, many=True)
        return Response(serializer.data)
