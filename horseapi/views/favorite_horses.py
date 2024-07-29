#favorite_horses.py
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from horseapi.models import FavoriteHorse, Horse
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class FavoriteHorseSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for favorite horses"""
    class Meta:
        model = FavoriteHorse
        url = serializers.HyperlinkedIdentityField(
            view_name='favoritehorse-detail',
            lookup_field='id'
        )
        fields = ('id', 'url', 'user', 'horse')

class FavoriteHorseViewSet(ViewSet):
    """Favorite Horses management"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        """Handle POST operations"""
        horse_id = request.data["horse"]
        try:
            horse = Horse.objects.get(pk=horse_id)
        except Horse.DoesNotExist:
            return Response({'message': 'Horse not found'}, status=status.HTTP_404_NOT_FOUND)
        
        new_favorite_horse = FavoriteHorse()
        new_favorite_horse.user = request.user
        new_favorite_horse.horse = horse
        new_favorite_horse.save()

        serializer = FavoriteHorseSerializer(new_favorite_horse, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single favorite horse"""
        try:
            favorite_horse = FavoriteHorse.objects.get(pk=pk)
            serializer = FavoriteHorseSerializer(favorite_horse, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a favorite horse"""
        try:
            favorite_horse = FavoriteHorse.objects.get(pk=pk)
            horse_id = request.data["horse"]
            horse = Horse.objects.get(pk=horse_id)
            favorite_horse.horse = horse
            favorite_horse.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except FavoriteHorse.DoesNotExist:
            return Response({'message': 'FavoriteHorse not found'}, status=status.HTTP_404_NOT_FOUND)
        except Horse.DoesNotExist:
            return Response({'message': 'Horse not found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single favorite horse"""
        try:
            favorite_horse = FavoriteHorse.objects.get(pk=pk)
            favorite_horse.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except FavoriteHorse.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to list all favorite horses"""
        favorite_horses = FavoriteHorse.objects.all()
        serializer = FavoriteHorseSerializer(
            favorite_horses, many=True, context={'request': request})
        return Response(serializer.data)
