from rest_framework import serializers
from .models import*

class Ticketserializer(serializers.ModelSerializer):
    class Meta:
        model=TicketModel
        fields='__all__'