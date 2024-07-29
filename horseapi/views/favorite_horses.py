from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from horseapi.models.favoritehorse import FavoriteHorse, Horse

class FavoriteHorseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteHorse
        fields = ('id', 'user', 'horse')

class FavoriteHorseViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request):
        horse_id = request.data["horse"]
        try:
            horse = Horse.objects.get(pk=horse_id)
        except Horse.DoesNotExist:
            return Response({'message': 'Horse not found'}, status=status.HTTP_404_NOT_FOUND)
        
        favorite_horse = FavoriteHorse(user=request.user, horse=horse)
        favorite_horse.save()
        
        serializer = FavoriteHorseSerializer(favorite_horse)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        favorite_horses = FavoriteHorse.objects.filter(user=request.user)
        serializer = FavoriteHorseSerializer(favorite_horses, many=True)
        return Response(serializer.data)
