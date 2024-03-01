from read_team_data import read_team_data_from_csv
def calculate_team_effort_capacity(csv_file_path, sprint_days):
    
    team_data = read_team_data_from_csv(csv_file_path)
    team_data['Total Available Hours'] = (sprint_days * team_data['Available Hours/Day']) - team_data['PTO Hours'] - (sprint_days * team_data['Ceremony Hours'])
    total_effort_hours = team_data['Total Available Hours'].sum()
    return total_effort_hours
