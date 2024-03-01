import pandas as pd

def read_team_data_from_csv(file_path):
    
    team_data = pd.read_csv(file_path)
    return team_data
