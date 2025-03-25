from django.db import connection

class MusicModel:
    @staticmethod
    def create_music(artist_id, title, album_name, genre):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO music (artist_id, title, album_name, genre, created_at, updated_at)
                VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) RETURNING id
                """,
                [artist_id, title, album_name, genre]
            )
            return cursor.fetchone()[0]

    @staticmethod
    def get_all_music():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM music")
            return cursor.fetchall()

    @staticmethod
    def get_music_by_id(music_id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM music WHERE id = %s", [music_id])
            return cursor.fetchone()

    @staticmethod
    def update_music(music_id, artist_id, title, album_name, genre):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE music 
                SET artist_id = %s, title = %s, album_name = %s, genre = %s, updated_at = CURRENT_TIMESTAMP
                WHERE id = %s
                """,
                [artist_id, title, album_name, genre, music_id]
            )
            return cursor.rowcount  # Returns the number of affected rows

    @staticmethod
    def delete_music(music_id):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM music WHERE id = %s", [music_id])
            return cursor.rowcount
