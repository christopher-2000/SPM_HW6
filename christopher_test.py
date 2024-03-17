import unittest
import pandas as pd
import sys
sys.path.append('./Feature A')
sys.path.append('./Feature B')

from velocity_calculator import calculate_velocity
from individualeffort import calculate_individual_effort_capacity
from teameffort import calculate_team_effort_capacity

# Feature A Testing
class TestCalculateVelocity(unittest.TestCase):

    def test_no_points_completed(self):
        self.assertEqual(calculate_velocity([]), 0)

    def test_single_point_completed(self):
        self.assertEqual(calculate_velocity([5]), 5)

    def test_multiple_points_completed(self):
        self.assertEqual(calculate_velocity([10, 20, 30]), 20)

    def test_zero_velocity(self):
        self.assertEqual(calculate_velocity([0, 0, 0]), 0)

    def test_negative_velocity(self):
        self.assertEqual(calculate_velocity([-10, -20, -30]), -20)

class TestCalculateIndividualEffortCapacity(unittest.TestCase):

    def test_no_pto_no_ceremonies(self):
        member_data = {
            'PTO Hours': 0,
            'Ceremony Hours': 0,
            'Available Hours/Day': 6.1
        }
        sprint_days = 10
        result = calculate_individual_effort_capacity(member_data, sprint_days)
        self.assertEqual(result, 61)

    def test_with_pto_no_ceremonies(self):
        member_data = {
            'PTO Hours': 2,
            'Ceremony Hours': 0,
            'Available Hours/Day': 7.3
        }
        sprint_days = 10
        result = calculate_individual_effort_capacity(member_data, sprint_days)
        self.assertEqual(result, 71)

    def test_no_pto_with_ceremonies(self):
        member_data = {
            'PTO Hours': 0,
            'Ceremony Hours': 4,
            'Available Hours/Day': 5.7
        }
        sprint_days = 10
        result = calculate_individual_effort_capacity(member_data, sprint_days)
        self.assertEqual(result, 17)

    def test_with_pto_and_ceremonies(self):
        member_data = {
            'PTO Hours': 1,
            'Ceremony Hours': 3,
            'Available Hours/Day': 6.2
        }
        sprint_days = 10
        result = calculate_individual_effort_capacity(member_data, sprint_days)
        self.assertEqual(result, 31)

class TestCalculateTeamEffortCapacity(unittest.TestCase):

    def test_no_pto_no_ceremonies(self):
        team_data = pd.DataFrame({
            'PTO Hours': [0, 0, 0],
            'Ceremony Hours': [0, 0, 0],
            'Available Hours/Day': [6.1, 7.3, 5.5]
        })
        sprint_days = 10
        result = calculate_team_effort_capacity(team_data, sprint_days)
        self.assertEqual(result, 189)

    def test_with_pto_no_ceremonies(self):
        team_data = pd.DataFrame({
            'PTO Hours': [2, 2, 1],
            'Ceremony Hours': [0, 0, 0],
            'Available Hours/Day': [7.3, 6.4, 6.2]
        })
        sprint_days = 10
        result = calculate_team_effort_capacity(team_data, sprint_days)
        self.assertEqual(result, 194)

    def test_no_pto_with_ceremonies(self):
        team_data = pd.DataFrame({
            'PTO Hours': [0, 0, 0],
            'Ceremony Hours': [4, 3, 2],
            'Available Hours/Day': [5.7, 6.2, 7.5]
        })
        sprint_days = 10
        result = calculate_team_effort_capacity(team_data, sprint_days)
        self.assertEqual(result, 104)

    def test_with_pto_and_ceremonies(self):
        team_data = pd.DataFrame({
            'PTO Hours': [1, 3, 2],
            'Ceremony Hours': [3, 2, 1],
            'Available Hours/Day': [6.2, 5.9, 7.2]
        })
        sprint_days = 10
        result = calculate_team_effort_capacity(team_data, sprint_days)
        self.assertEqual(result, 127)

if __name__ == '__main__':
    unittest.main()