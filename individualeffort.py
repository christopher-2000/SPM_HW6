from read_team_data import read_team_data_from_csv
def calculate_individual_effort_capacity(csv_file_path, sprint_days):
    
    member_data = read_team_data_from_csv(csv_file_path)
    pto_hours = member_data['PTO Hours']
    ceremony_hours = member_data['Ceremony Hours']
    available_hours_per_day = member_data['Available Hours/Day']
    total_available_hours = (sprint_days * available_hours_per_day) - pto_hours - (ceremony_hours * sprint_days)
    return total_available_hours
