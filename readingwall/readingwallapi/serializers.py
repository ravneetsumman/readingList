from rest_framework import serializers
from .models import Wallposts
from .models import Connections

class WallpostsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Wallposts
        fields = ('id', 'owner', 'blog_url', 'wall_context', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class ConnectionsSerializer(serializers.ModelSerializer):
    friendreq_by = serializers.ReadOnlyField(source='friendreq_by.username')
    
    class Meta:
        model =  Connections
        fields = ('id', 'friendreq_by', 'friendreq_to')
        read_only_fields = ('date_created', 'date_modified')
