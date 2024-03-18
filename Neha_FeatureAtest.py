import unittest

def calculate_velocity(points_completed):
    if not isinstance(points_completed, list) or not all(isinstance(x, int) for x in points_completed):
        raise TypeError("Input Integers")

    return sum(points_completed) / len(points_completed) if points_completed else 0.0

class TestVelocityCalculator(unittest.TestCase):

    def test_calculate_velocity_valid(self):

        valid_points_completed = [5, 8, 10]
        expected_velocity = (5 + 8 + 10) / 3.0
        self.assertAlmostEqual(expected_velocity, calculate_velocity(valid_points_completed), places=3)

    def test_calculate_velocity_empty(self):

        empty_points_completed = []
        self.assertEqual(0.0, calculate_velocity(empty_points_completed))

    def test_calculate_velocity_negative(self):

        negative_points_completed = [-5, -3, -8]
        expected_velocity = (-5 - 3 - 8) / 3.0
        self.assertAlmostEqual(expected_velocity, calculate_velocity(negative_points_completed), places=3)

    def test_calculate_velocity_zero_division(self):

        zero_points_completed = []
        self.assertEqual(0.0, calculate_velocity(zero_points_completed))


        zero_points_sprints = [5, 0, 8, 10]
        expected_velocity = (5 + 0 + 8 + 10) / 4.0
        self.assertAlmostEqual(expected_velocity, calculate_velocity(zero_points_sprints), places=3)

    def test_calculate_velocity_invalid_input(self):

        invalid_points_completed = ["a", "b", "c"]
        with self.assertRaises(TypeError):
            calculate_velocity(invalid_points_completed)


        non_numeric_points_completed = [5, "b", 10]
        with self.assertRaises(TypeError):
            calculate_velocity(non_numeric_points_completed)

if __name__ == '__main__':
    unittest.main()
