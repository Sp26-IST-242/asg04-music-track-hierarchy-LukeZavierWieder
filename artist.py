"""
Represents a musical artist or podcast creator.

This is the simplest class in the hierarchy — no dependencies, no validation.
It introduces two core Python OOP conventions:
  1. The single leading-underscore (_name) signals a non-public attribute.
  2. @property exposes a clean public getter without allowing direct mutation.
"""

class Artist:
    '''
    Creates the Artist class.
    '''
    
    # Constructer
    def __init__(self, name : str, genre : str):
        # Name of artist
        self._name = name
        # Genre of the artist
        self._genre = genre

    # Properties (getters)
    @property
    def name(self):
        '''
        returns the name
        
        Parameter:
            self: 
        '''
        return self._name
    @property
    def genre(self):
        '''
        returns the genre
        
        Parameter:
            self: 
        '''
        return self._genre
    
    def __str__(self):
        '''
        Prints out the Artist object
        '''
        return f"{self._name}, {self._genre}"