"""
Represents a music album or podcast series, including the years it was active.

Key concepts to implement:
  • Input validation in __init__ (fail-fast with a clear ValueError).
  • Defensive copy on both input and output so external code cannot corrupt
    the internal years list.
  • A *derived* property (debut_year) that computes its value from stored data
    rather than keeping a second field in sync.
"""

class Album:
    '''
    Creates the Album class.
    '''
    
    # Constructer
    def __init__(self, title : str, active : bool, years : list[int]):
        # Error for empty list
        if not years:
            raise ValueError("Years list must not be empty.")
        # Name of album
        self._title = title
        # Is the album active 
        self._active = active
        # Years the album was released
        self._years = list(years)

    # Properties (getters)
    @property
    def title(self):
        '''
        returns the title
        
        Parameter:
            self: 
        '''
        return self._title
    @property
    def active(self):
        '''
        returns the activity
        
        Parameter:
            self: 
        '''
        return self._active
    @property
    def years(self):
        '''
        returns the activity
        
        Parameter:
            self: 
        '''
        return list(self._years)
    @property
    def debut_year(self):
        '''
        Calculates the debut year for the album
        '''
        return self._years[0]
    
    def __str__(self):
        '''
        Prints out the Artist object
        '''
        return f"{self._title} active = {self._active}, debut year: {self._years[0]}"