import unittest

def calculate_effort_hours_per_person(sprint_days, team_member_details):
    effort_hours_per_person = []

    for member in team_member_details:
        total_hours_available = sprint_days * member['hours_per_day']
        total_hours_unavailable = member.get('pto_hours', 0) + member.get('ceremony_hours', 0)
        available_hours = total_hours_available - total_hours_unavailable
        effort_hours_per_person.append(available_hours)

    return effort_hours_per_person

class TestCalculateEffortHoursPerPerson(unittest.TestCase):
    def test_all_paths(self):

        sprint_days = 10
        team_member_details = [
            {'pto_hours': 8, 'ceremony_hours': 12, 'hours_per_day': 8},
            {'pto_hours': 16, 'ceremony_hours': 8, 'hours_per_day': 6},
            {'pto_hours': 0, 'ceremony_hours': 0, 'hours_per_day': 7.5}
        ]
        expected_result = [60, 36, 75.0]
        self.assertEqual(calculate_effort_hours_per_person(sprint_days, team_member_details), expected_result)


        sprint_days = 5
        team_member_details = [
            {'hours_per_day': 8},
            {'hours_per_day': 6},
            {'hours_per_day': 7.5}
        ]
        expected_result = [40, 30, 37.5]
        print(calculate_effort_hours_per_person(sprint_days,team_member_details))
        self.assertEqual(calculate_effort_hours_per_person(sprint_days, team_member_details), expected_result)

        sprint_days = 0
        team_member_details = [
            {'pto_hours': 8, 'ceremony_hours': 12, 'hours_per_day': 8},
            {'pto_hours': 16, 'ceremony_hours': 8, 'hours_per_day': 6},
            {'pto_hours': 0, 'ceremony_hours': 0, 'hours_per_day': 7.5}
        ]
        expected_result = [-20, -24, 0.0]
        self.assertEqual(calculate_effort_hours_per_person(sprint_days, team_member_details), expected_result)

if __name__ == '__main__':
    unittest.main()
