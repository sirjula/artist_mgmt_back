from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ArtistModel
from .serializers import ArtistSerializer, ArtistUpdateSerializer
# from .authentication import JWTHandler
# from rest_framework.permissions import IsAuthenticated

class ArtistListView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        """Create a new artist (Only Artist Managers)"""
        # if request.user.role != "artist_manager":
        #     return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            artist_id = ArtistModel.create_artist(
                data["name"], data["dob"], data["gender"], data["address"], data["first_release_year"], data["no_of_albums_released"]
            )
            return Response({"message": "Artist created successfully", "artist_id": artist_id}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """List all artists"""
        artists = ArtistModel.get_all_artists()
        artist_list = [
            {
                "id": a[0],
                "name": a[1],
                "dob": a[2],
                "gender": a[3],
                "address": a[4],
                "first_release_year": a[5],
                "no_of_albums_released": a[6],
            }
            for a in artists
        ]
        return Response({"artists": artist_list}, status=status.HTTP_200_OK)

class ArtistDetailView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, artist_id):
        """Retrieve details of a specific artist"""
        artist = ArtistModel.get_artist_by_id(artist_id)
        if artist:
            artist_data = {
                "id": artist[0],
                "name": artist[1],
                "dob": artist[2],
                "gender": artist[3],
                "address": artist[4],
                "first_release_year": artist[5],
                "no_of_albums_released": artist[6],
            }
            return Response(artist_data, status=status.HTTP_200_OK)
        return Response({"error": "Artist not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, artist_id):
        """Update an artist (Only Artist Managers)"""
        # if request.user.role != "artist_manager":
        #     return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

        serializer = ArtistUpdateSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            rows_affected = ArtistModel.update_artist(
                artist_id,  
                data["name"], 
                data["dob"], 
                data["gender"], 
                data["address"], 
                data["first_release_year"], 
                data["no_of_albums_released"]
            )

            if rows_affected:
                return Response({"message": "Artist updated successfully"}, status=status.HTTP_200_OK)
            return Response({"error": "Artist not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, artist_id):
        """Delete an artist (Only Artist Managers)"""
        # if request.user.role != "artist_manager":
        #     return Response({"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN)

        rows_affected = ArtistModel.delete_artist(artist_id)
        if rows_affected:
            return Response({"message": "Artist deleted successfully"}, status=status.HTTP_200_OK)

        return Response({"error": "Artist not found"}, status=status.HTTP_404_NOT_FOUND)