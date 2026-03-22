"""
Abstract base class for all music tracks (Songs and Podcasts).

Design decisions to implement:
  • ABC makes it impossible to instantiate MusicTrack directly — you can only
    create concrete subclasses that implement every @abstractmethod.
  • Common fields (artist, album, duration_seconds) live here so that Song and
    Podcast do not each need to repeat them.
  • release_year is a *derived* property delegating to Album.debut_year; the
    year is not stored a second time.
  • play_time_formatted() is abstract because Song and Podcast format time
    differently (MM:SS vs HH:MM:SS).
  • total_play_time() is concrete because the calculation is identical for all
    track types: duration × number of plays.
  • @functools.total_ordering generates <=, >, >= automatically from __eq__ and
    __lt__, giving us full comparison support with minimal code.
  • __hash__ is defined to stay consistent with __eq__ (Python sets __hash__ to
    None when you define __eq__, making objects unhashable unless you fix it).
"""
from abc import ABC, abstractmethod
from functools import total_ordering # Sorting purposes
from artist import Artist
from album import Album

class MusicTrack(ABC):
    '''
    Creates the abstract class for music tracks
    '''
    # Constructor
    def __init__(self, artist: Artist, album: Album,
                 duration: int):
        self._artist = artist
        self._album = album
        self._duration = duration
    
    # Getters
    @property
    def artist(self):
        return self._artist
    
    @property
    def album(self):
        return self._album
    
    @property
    def duration(self):
        return self._duration
    
    # Abstract method
    @abstractmethod
    def play_time_formatted(self, duration : int):
        ...
    
    # Concrete method
    def total_play_time(self, num_plays: int, duration):
        # Returns total play time of track
        num_plays = input()
        return num_plays * duration
