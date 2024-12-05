import unittest
from puzzles.geometric_shapes import GeometricPuzzle

class TestGeometricPuzzle(unittest.TestCase):
    def setUp(self):
        """Set up the puzzle instance for testing."""
        self.puzzle = GeometricPuzzle()

    def test_initial_player_pattern(self):
        """Test if the player's pattern is initialized with all zeros."""
        for row in self.puzzle.player_pattern:
            self.assertTrue(all(cell == 0 for cell in row))

    def test_toggle_pattern(self):
        """Test if toggling a cell updates the player's pattern correctly."""
        self.puzzle.update_pattern(1, 1)  # Toggle the cell at (1, 1)
        self.assertEqual(self.puzzle.player_pattern[1][1], 1)

        self.puzzle.update_pattern(1, 1)  # Toggle it back
        self.assertEqual(self.puzzle.player_pattern[1][1], 0)

    def test_is_solved(self):
        """Test if the puzzle detects a solved state."""
        self.puzzle.player_pattern = self.puzzle.target_pattern[:]  # Match patterns
        self.assertTrue(self.puzzle.is_solved())

if __name__ == "__main__":
    unittest.main()
