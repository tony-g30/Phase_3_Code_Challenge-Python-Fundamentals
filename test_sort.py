import unittest
from sort_by_age import sort_by_age  # Adjust the import based on your file structure

class TestSortByAge(unittest.TestCase):

    def test_sort_by_age(self):
        # Test case 1: Regular list of tuples
        input_data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
        expected_output = [("Bob", 25), ("Alice", 30), ("Charlie", 35)]
        self.assertEqual(sort_by_age(input_data), expected_output)

        # Test case 2: List with same ages
        input_data = [("Alice", 30), ("Bob", 30), ("Charlie", 30)]
        expected_output = [("Alice", 30), ("Bob", 30), ("Charlie", 30)]
        self.assertEqual(sort_by_age(input_data), expected_output)

        # Test case 3: Empty list
        input_data = []
        expected_output = []
        self.assertEqual(sort_by_age(input_data), expected_output)

        # Test case 4: Single element list
        input_data = [("Alice", 30)]
        expected_output = [("Alice", 30)]
        self.assertEqual(sort_by_age(input_data), expected_output)

        # Test case 5: Negative ages
        input_data = [("Alice", -30), ("Bob", -25), ("Charlie", -35)]
        expected_output = [("Charlie", -35), ("Alice", -30), ("Bob", -25)]
        self.assertEqual(sort_by_age(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()
