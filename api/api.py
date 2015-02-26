from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from models import Book, BookRegistry

class BookRegistrySerializer(serializers.RelatedField):
    class Meta:
        model = BookRegistry

# Serializers define the API representation.
class BookSerializer(serializers.ModelSerializer):
    
    # this doesnt work for some reason
    #events = BookRegistrySerializer(many=True, read_only=True)
    
    class Meta:
        model = Book
        #fields = ('title', 'description', 'motivation', 'events')

# ViewSets define the view behavior.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Routers provide an easy way of automatically determining the URL conf.
book_router = routers.DefaultRouter()
book_router.register(r'book', BookViewSet)

