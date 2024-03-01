def calculate_individual_effort_capacity(member_data, sprint_days):
    
    pto_hours = member_data['PTO Hours']
    ceremony_hours = member_data['Ceremony Hours']
    available_hours_per_day = member_data['Available Hours/Day']
    total_available_hours = (sprint_days * available_hours_per_day) - pto_hours - (ceremony_hours * sprint_days)
    return total_available_hours
