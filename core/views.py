from .models import List, Item
from .serializers import ListSerializer
from rest_framework import viewsets
from rest_framework import permissions


class ListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]
    