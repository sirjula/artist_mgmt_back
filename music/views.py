from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MusicModel
from .serializers import MusicSerializer, MusicUpdateSerializer

class MusicListView(APIView):
    """Create new music or list all music"""
    
    def post(self, request):
        """Create new music"""
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            music_id = MusicModel.create_music(
                data["artist_id"], data["title"], data["album_name"], data["genre"]
            )
            return Response({"message": "Music created successfully", "music_id": music_id}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """List all music"""
        music = MusicModel.get_all_music()
        music_list = [
            {
                "id": m[0],
                "artist_id": m[1],
                "title": m[2],
                "album_name": m[3],
                "genre": m[4],
            }
            for m in music
        ]
        return Response({"music": music_list}, status=status.HTTP_200_OK)

class MusicDetailView(APIView):
    """Retrieve, update, or delete a specific music entry"""

    def get(self, request, music_id):
        """Retrieve details of a specific music"""
        music = MusicModel.get_music_by_id(music_id)
        if music:
            music_data = {
                "id": music[0],
                "artist_id": music[1],
                "title": music[2],
                "album_name": music[3],
                "genre": music[4]
            }
            return Response(music_data, status=status.HTTP_200_OK)
        return Response({"error": "Music not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, music_id):
        """Update a specific music"""
        serializer = MusicUpdateSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            rows_affected = MusicModel.update_music(
                music_id, 
                data["artist_id"], 
                data["title"], 
                data["album_name"], 
                data["genre"]
            )
            if rows_affected:
                return Response({"message": "Music updated successfully"}, status=status.HTTP_200_OK)
            return Response({"error": "Music not found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, music_id):
        """Delete a specific music"""
        rows_affected = MusicModel.delete_music(music_id)
        if rows_affected:
            return Response({"message": "Music deleted successfully"}, status=status.HTTP_200_OK)

        return Response({"error": "Music not found"}, status=status.HTTP_404_NOT_FOUND)
