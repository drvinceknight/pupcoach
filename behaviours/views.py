from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from behaviours.models import Behaviour
from behaviours.serializers import BehaviourSerializer

import random

@csrf_exempt
def behaviour_list(request):
    """
    List all behaviours, or create a new behaviour
    """
    if request.method == 'GET':
        behaviours = Behaviour.objects.all()
        serializer = BehaviourSerializer(behaviours, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BehaviourSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)

@csrf_exempt
def behaviour_detail(request, pk):
    """
    Retrieve, update or delete a behaviour
    """
    try:
        behaviour = Behaviour.objects.get(pk=pk)
    except Behaviour.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BehaviourSerializer(behaviour)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BehaviourSerializer(behaviour, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        behaviour.delete()
        return HttpResponse(status=204)

@csrf_exempt
def sequence_detail(request, length, seed=None):
    """
    Retrieve, update or delete a behaviour
    """
    # TODO Add exception handler when for length being larger than total tricks.
    if request.method == 'GET':
        if seed is not None:
            random.seed(seed)
        behaviours = random.sample(list(Behaviour.objects.all()), length)

        serializer = BehaviourSerializer(behaviours, many=True)
        return JsonResponse(serializer.data, safe=False)
