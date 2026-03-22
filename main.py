"""
Driver script demonstrating the complete Music Track hierarchy.

Run:
    python main.py

Expected output
---------------
Before sorting:
(Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017, duration: 03:40
(Alanis Morissette, Alternative) Jagged Little Pill active = False,  debut year: 1995, duration: 04:05
(Joe Rogan, Comedy) The Joe Rogan Experience active = True,  debut year: 2009, duration: 02:30:00 is explicit: True
(Sarah Koenig, Journalism) Serial active = False,  debut year: 2014, duration: 01:30:00 is explicit: False

After sorting:
(Alanis Morissette, Alternative) Jagged Little Pill active = False,  debut year: 1995, duration: 04:05
(Joe Rogan, Comedy) The Joe Rogan Experience active = True,  debut year: 2009, duration: 02:30:00 is explicit: True
(Sarah Koenig, Journalism) Serial active = False,  debut year: 2014, duration: 01:30:00 is explicit: False
(Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017, duration: 03:40
"""
from artist import Artist
from album import Album
from song import Song
from podcast import Podcast
from playlist import Playlist

def main():
    kendrick = Song(Artist("Kendrick Lamar","Hip-Hop"),
           Album("DAMN.",True,list(range(2017,2018))),
           220)
    
    alanis = Song(Artist("Alanis Morissette","Alternative"),
           Album("Jagged Little Pill",False,list(range(1995,1996))),
           245)
    
    joe = Podcast(Artist("Joe Rogan","Comedy"),
           Album("The Joe Rogan Experience",True,list(range(2009,2010))),
           9000, True)
    
    sarah = Podcast(Artist("Sarah Koenig","Journalism"),
           Album("Serial",False,list(range(2014,2015))),
           5400)
    
    p = Playlist()
    p.add_track(kendrick)
    p.add_track(alanis)
    p.add_track(joe)
    p.add_track(sarah)

    print("Before sorting:")
    print(p)
    p.sort_by_release_year()
    print("\nAfter sorting:")
    print(p)

if __name__ == "__main__":
    main()