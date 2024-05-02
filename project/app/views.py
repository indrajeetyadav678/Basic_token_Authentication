from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import BasicAuthentication

class TicketViewSet(viewsets.ModelViewSet):
	authentication_classes = [BasicAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = TicketModel.objects.all()
	serializer_class = Ticketserializer