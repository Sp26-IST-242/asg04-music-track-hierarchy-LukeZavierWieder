"""
Concrete subclass of MusicTrack representing a standard music track.

Song adds no new fields beyond what MusicTrack already stores.  Its only
responsibility is to:
  1. Call super().__init__() to let MusicTrack do the storage work.
  2. Implement play_time_formatted() in MM:SS format.
     Return the duration as 'MM:SS' (both parts zero-padded).

        Examples
        --------
        220 seconds → '03:40'
        65  seconds → '01:05'
        
  3. Override __str__ for a human-readable representation.
     Return '(<artist>) <album>, duration: <MM:SS>'.

        Example:
            (Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017,
            duration: 03:40
"""
from music_track import MusicTrack
from artist import Artist
from album import Album

class Song(MusicTrack):
    '''
    Creates the Song class
    '''
    # Constructor
    def __init__(self, artist : Artist,
                album : Album, duration: int):
        super().__init__(artist, album, duration)
    
    # Getters
    def play_time_formatted(self, duration : int):
      minutes = duration // 60
      seconds = duration % 60
      formatted = f"{minutes:02f}:{seconds:02f}"
      return formatted
    
    # Print Song info
    def __str__(self, formatted):
       return f"({self._name}, {self._genre}) {self._title}. active = {self._active},"
       f"debut year: {self._years[0]}, duration: {formatted}"