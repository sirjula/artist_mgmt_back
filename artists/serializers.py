from rest_framework import serializers

class ArtistSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    dob = serializers.DateField()
    gender = serializers.ChoiceField(choices=["m", "f", "o"])
    address = serializers.CharField(max_length=255)
    first_release_year = serializers.DateField()  
    no_of_albums_released = serializers.IntegerField()

class ArtistUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    dob = serializers.DateField()
    gender = serializers.ChoiceField(choices=["m", "f", "o"])
    address = serializers.CharField(max_length=255)
    first_release_year = serializers.DateField() 
    no_of_albums_released = serializers.IntegerField()
