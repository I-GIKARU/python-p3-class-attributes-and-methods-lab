#!/usr/bin/env python3

class Song:
    count = 0
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment total count
        Song.count += 1

        # Update genre_count dictionary
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Update artist_count dictionary
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

    @property
    def genres(cls):
        # Return the list of genres (keys of genre_count)
        return list(cls.genre_count.keys())

    @property
    def artists(cls):
        # Return the list of artists (keys of artist_count)
        return list(cls.artist_count.keys())

    # To make genres and artists class properties, override __getattr__ or use descriptor
    # But better: define as class properties using metaclass or descriptor
    # For simplicity, we'll do this:

# Patch class-level properties manually (Python 3.9+ needed for classproperty decorator, or use a workaround)
def classproperty(func):
    class Descriptor:
        def __get__(self, instance, owner):
            return func(owner)
    return Descriptor()

Song.genres = classproperty(lambda cls: list(cls.genre_count.keys()))
Song.artists = classproperty(lambda cls: list(cls.artist_count.keys()))
