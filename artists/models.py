from django.db import connection

class ArtistModel:
    @staticmethod
    def create_artist(name,dob,gender,address,first_release_year,no_of_albums_released):
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO artist (name,dob,gender,address,first_release_year,no_of_albums_released,created_at, updated_at) "
                "VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) RETURNING id",
                [name,dob,gender,address,first_release_year,no_of_albums_released]
            )
            return cursor.fetchone()[0]

    @staticmethod
    def get_all_artists():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM artist")
            return cursor.fetchall()

    @staticmethod
    def get_artist_by_id(artist_id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM artist WHERE id = %s", [artist_id])
            return cursor.fetchone()

    @staticmethod
    def update_artist(artist_id, name, dob, gender, address, first_release_year, no_of_albums_released):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE artist 
                SET name = %s, dob = %s, gender = %s, address = %s, 
                    first_release_year = %s, no_of_albums_released = %s, 
                    updated_at = CURRENT_TIMESTAMP 
                WHERE id = %s
                """,
                [name, dob, gender, address, first_release_year, no_of_albums_released, artist_id]  # artist_id should be at the end
            )
            return cursor.rowcount  # Returns the number of affected rows


    @staticmethod
    def delete_artist(artist_id):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM artist WHERE id = %s", [artist_id])
            return cursor.rowcount
