from .puzzle_base import PuzzleBase
import random

class GeometricPuzzle(PuzzleBase):
    """
    A puzzle where players align geometric shapes to match a target pattern.

    Attributes:
        target_pattern (list[list[int]]): The randomly generated target pattern.
        player_pattern (list[list[int]]): The player's current pattern.
    """

    def __init__(self):
        """
        Initializes the GeometricPuzzle with a random target pattern.
        """
        super().__init__("Geometric Puzzle")
        self.target_pattern = self.generate_target_pattern()
        self.player_pattern = [[0] * len(self.target_pattern) for _ in range(len(self.target_pattern))]

    def generate_target_pattern(self):
        """
        Generates a random target pattern for the puzzle.

        Returns:
            list[list[int]]: A 2D list representing the target pattern.
        """
        size = random.randint(3, 5)  # Puzzle size: 3x3 to 5x5
        return [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]

    def display_instructions(self):
        """
        Displays instructions for solving the geometric puzzle.
        """
        print("Align the geometric shapes to match the target pattern!")

    def display_patterns(self):
        """
        Displays both the target pattern and the player's current pattern.
        """
        print("\nTarget Pattern:")
        for row in self.target_pattern:
            print(" ".join(str(x) for x in row))
        print("\nYour Pattern:")
        for row in self.player_pattern:
            print(" ".join(str(x) for x in row))

    def update_pattern(self, x, y):
        """
        Toggles the state of a position in the player's pattern.

        Args:
            x (int): The row index to toggle.
            y (int): The column index to toggle.
        """
        if 0 <= x < len(self.player_pattern) and 0 <= y < len(self.player_pattern):
            self.player_pattern[x][y] = 1 - self.player_pattern[x][y]  # Toggle 0/1

    def is_solved(self):
        """
        Checks if the player's pattern matches the target pattern.

        Returns:
            bool: True if the patterns match, False otherwise.
        """
        return self.player_pattern == self.target_pattern

    def solve(self):
        """
        Runs the main logic for solving the puzzle, allowing the player to interactively toggle positions.
        """
        self.display_instructions()
        while not self.is_solved():
            self.display_patterns()
            try:
                x, y = map(int, input("Enter the coordinates to toggle (row col): ").split())
                self.update_pattern(x, y)
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
        print("Congratulations! You solved the puzzle!")
