from .puzzle_base import PuzzleBase
import random

class GeometricPuzzle(PuzzleBase):
    """
    A puzzle where players align geometric shapes to complete a pattern.
    """
    def __init__(self):
        super().__init__("Geometric Puzzle")
        self.target_pattern = self.generate_target_pattern()
        self.player_pattern = [[0] * len(self.target_pattern) for _ in range(len(self.target_pattern))]

    def generate_target_pattern(self):
        """Generate a random target pattern."""
        size = random.randint(3, 5)  # Puzzle size: 3x3 to 5x5
        return [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]

    def display_instructions(self):
        print("Align the geometric shapes to match the target pattern!")

    def display_patterns(self):
        """Display both player and target patterns."""
        print("\nTarget Pattern:")
        for row in self.target_pattern:
            print(" ".join(str(x) for x in row))
        print("\nYour Pattern:")
        for row in self.player_pattern:
            print(" ".join(str(x) for x in row))

    def update_pattern(self, x, y):
        """Toggle the state of a position in the player's pattern."""
        if 0 <= x < len(self.player_pattern) and 0 <= y < len(self.player_pattern):
            self.player_pattern[x][y] = 1 - self.player_pattern[x][y]  # Toggle 0/1

    def is_solved(self):
        """Check if the player pattern matches the target pattern."""
        return self.player_pattern == self.target_pattern

    def solve(self):
        """Main logic for solving the puzzle."""
        self.display_instructions()
        while not self.is_solved():
            self.display_patterns()
            try:
                x, y = map(int, input("Enter the coordinates to toggle (row col): ").split())
                self.update_pattern(x, y)
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
        print("Congratulations! You solved the puzzle!")
