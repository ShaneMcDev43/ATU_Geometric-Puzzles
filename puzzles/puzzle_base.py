class PuzzleBase:
    """
    Base class for all puzzles. Defines the interface that all puzzles must implement.
    """
    def __init__(self, name):
        self.name = name

    def display_instructions(self):
        """Display puzzle instructions to the player."""
        raise NotImplementedError("Subclasses must implement this method.")

    def solve(self):
        """Logic for solving the puzzle."""
        raise NotImplementedError("Subclasses must implement this method.")
