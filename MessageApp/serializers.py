from rest_framework import serializers
from MessageApp.models import Messages

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields=('Id', 'Content')