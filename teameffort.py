def calculate_team_effort_capacity(team_data, sprint_days):

    team_data['Total Available Hours'] = (sprint_days * team_data['Available Hours/Day']) - team_data['PTO Hours'] - (sprint_days * team_data['Ceremony Hours'])
    total_effort_hours = team_data['Total Available Hours'].sum()
    return total_effort_hours
