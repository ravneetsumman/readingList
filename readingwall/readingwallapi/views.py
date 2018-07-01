from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import WallpostsSerializer, ConnectionsSerializer
from .models import Wallposts, Connections
from .permissions import IsOwner
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class WallpostCreate(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Wallposts.objects.all()
    serializer_class = WallpostsSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new wallpost."""
        serializer.save(owner=self.request.user)

class WallpostDetail(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Wallposts.objects.all()
    serializer_class = WallpostsSerializer

class Friends(APIView):
    """ This class adds connections"""
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        connections = Connections.objects.all()
        serializer = ConnectionsSerializer(connections, many=True)
        permission_classes = (permissions.IsAuthenticated,)
        #print (serializer.data)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ConnectionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(friendreq_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
