class PuzzleBase:
    """
    Base class for all puzzles.

    Attributes:
        name (str): The name of the puzzle.
    """

    def __init__(self, name):
        """
        Initializes the base puzzle.

        Args:
            name (str): The name of the puzzle.
        """
        self.name = name

    def display_instructions(self):
        """
        Display puzzle instructions to the player.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def solve(self):
        """
        Logic for solving the puzzle.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError("Subclasses must implement this method.")
