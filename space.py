class Space:
    """
    Stores the value of a space as well as whether or not it is
    marked, hidden, or a bomb.
    """
    is_marked = False
    def __init__(self, value = 0, is_marked = False, is_bomb = False, is_hidden = True):
        """
        Constructor for the Space class.

        :param value: The value of the space
        :type value: int
        :param is_marked: Whether or not the space is marked
        :type is_marked: bool
        :param is_bomb: Whether or not the space is a bomb
        :type is_bomb: bool
        :param is_hidden: Whether or not the space is hidden
        :type is_hidden: bool
        """
        self.value = value
        self.is_marked = is_marked
        self.is_bomb = is_bomb
        self.is_hidden = is_hidden

    def mark_space(self):
        """
        Marks a space.

        If the space is already marked, this function will unmark it.
        :return: void
        """
        if self.is_marked:
            self.is_marked = False
        else:
            self.is_marked = True

    def __str__(self):
        """
        Defines string casting for the Space class.

        Returns "M" if the space is marked, "*" if it is hidden, and the value of the space otherwise.
        """
        if self.is_marked:
            return "M"
        elif self.is_hidden:
            return "*"
        else:
            return str(self.value)