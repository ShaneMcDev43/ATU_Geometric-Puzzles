import unittest
from puzzles.puzzle_base import PuzzleBase

class TestPuzzleBase(unittest.TestCase):
    def setUp(self):
        """Set up a subclass to test PuzzleBase."""
        # Create a mock subclass of PuzzleBase for testing
        class MockPuzzle(PuzzleBase):
            def display_instructions(self):
                return "Mock instructions"

            def solve(self):
                return "Mock solve logic"

        self.mock_puzzle = MockPuzzle("Mock Puzzle")

    def test_initialization(self):
        """Test that a PuzzleBase subclass initializes correctly."""
        self.assertEqual(self.mock_puzzle.name, "Mock Puzzle")

    def test_display_instructions_not_implemented(self):
        """Test that the base class raises NotImplementedError for display_instructions."""
        with self.assertRaises(NotImplementedError):
            PuzzleBase("Base Puzzle").display_instructions()

    def test_solve_not_implemented(self):
        """Test that the base class raises NotImplementedError for solve."""
        with self.assertRaises(NotImplementedError):
            PuzzleBase("Base Puzzle").solve()

    def test_mock_display_instructions(self):
        """Test that the subclass implements display_instructions."""
        self.assertEqual(self.mock_puzzle.display_instructions(), "Mock instructions")

    def test_mock_solve(self):
        """Test that the subclass implements solve."""
        self.assertEqual(self.mock_puzzle.solve(), "Mock solve logic")


if __name__ == "__main__":
    unittest.main()
