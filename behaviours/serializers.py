from rest_framework import serializers
from behaviours.models import Behaviour

class BehaviourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Behaviour
        fields = ('title', 'acquired')
