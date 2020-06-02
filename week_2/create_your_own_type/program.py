
class WordplayStr(str):
    """A string that can report whether it has interesting properties."""


    def same_part_and_end(self):
        """ (WordplayStr) --> bool
        Precondition: len(self) != 0
        
        Return whether self starts and ends with the same letter.
        
        >>> s = WordplayStr('abracadabra')
        >>> s.same_part_and_end()
        True
        >>> s = WordplayStr('canoe')
        >>> s.same_part_and_end()
        False
        """

        return self[0] == self[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
