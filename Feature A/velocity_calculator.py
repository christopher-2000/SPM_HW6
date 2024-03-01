def calculate_velocity(points_completed):
    if not points_completed:
        return 0  # Return 0 if there are no points completed
    
    total_points = sum(points_completed)
    num_sprints = len(points_completed)
    velocity = total_points / num_sprints
    return velocity
