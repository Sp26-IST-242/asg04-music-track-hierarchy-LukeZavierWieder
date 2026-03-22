"""
Concrete subclass of MusicTrack representing a podcast episode.

Podcast differs from Song in two ways:
  1. It has one extra field: is_explicit (bool), defaulting to False.
     The default value replaces Java-style constructor overloading — one
     __init__ handles both the explicit and non-explicit cases.
  2. play_time_formatted() returns 'HH:MM:SS' instead of 'MM:SS', because
     podcast episodes are typically longer than an hour.

    Return the duration as 'HH:MM:SS' (all parts zero-padded).

        Examples
        --------
        9000 seconds → '02:30:00'
        5400 seconds → '01:30:00'
        3661 seconds → '01:01:01'

 3. Override __str__ for a human-readable representation.
        Return '(<artist>) <album>, duration: <HH:MM:SS> is explicit: <bool>'.

        Example:
            (Joe Rogan, Comedy) The Joe Rogan Experience active = True,
             debut year: 2009, duration: 02:30:00 is explicit: True
"""
from music_track import MusicTrack
from artist import Artist
from album import Album

class Podcast(MusicTrack):
   # constructor
   def __init__(
         self, artist: Artist, album: Album,
         duration_seconds: int, is_explicit: bool = False):
      super().__init__(artist, album, duration_seconds)
      # Set If explicit
      self._is_explicit = is_explicit

   # Getters
   @property
   def is_explicit(self):
      # Returns if explicit
      return self._is_explicit
   @property
   def release_year(self):
       return self.album.debut_year
   @property
   def duration_seconds(self):
       return self._duration_seconds

   # Format playtime
   def play_time_formatted(self):
      time = int(self._duration_seconds)
      hours = time // 3600
      minutes = (time % 3600) // 60
      seconds = time % 60
      return f"{hours:02}:{minutes:02}:{seconds:02}"
   
   def __str__(self):
      return f'({self._artist}) {self._album} duration: {self.play_time_formatted()} is explicit: {self._is_explicit}'