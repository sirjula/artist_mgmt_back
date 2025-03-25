from rest_framework import serializers

class MusicSerializer(serializers.Serializer):
    artist_id = serializers.IntegerField()  # Foreign key reference to Artist
    title = serializers.CharField(max_length=255)
    album_name = serializers.CharField(max_length=255)
    genre = serializers.ChoiceField(choices=['rnb', 'country', 'classic', 'rock', 'jazz'])

class MusicUpdateSerializer(serializers.Serializer):
    artist_id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    album_name = serializers.CharField(max_length=255)
    genre = serializers.ChoiceField(choices=['rnb', 'country', 'classic', 'rock', 'jazz'])
