#horses.py
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from horseapi.models import Horse
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class HorseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horse
        fields = ['id', 'name', 'date_of_birth', 'total_races', 'total_earnings', 'user']

class Horses(ViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        new_horse = Horse()
        new_horse.name = request.data["name"]
        new_horse.date_of_birth = request.data["date_of_birth"]
        new_horse.total_races = request.data["total_races"]
        new_horse.total_earnings = request.data["total_earnings"]
        new_horse.user = request.user
        new_horse.save()

        serializer = HorseSerializer(new_horse, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        try:
            horse = Horse.objects.get(pk=pk)
            serializer = HorseSerializer(horse, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        horse = Horse.objects.get(pk=pk)
        horse.name = request.data["name"]
        horse.date_of_birth = request.data["date_of_birth"]
        horse.total_races = request.data["total_races"]
        horse.total_earnings = request.data["total_earnings"]
        horse.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            horse = Horse.objects.get(pk=pk)
            horse.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Horse.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        horses = Horse.objects.all()
        serializer = HorseSerializer(
            horses, many=True, context={'request': request})
        return Response(serializer.data)
