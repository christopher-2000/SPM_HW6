from input_reader import read_points_from_list, read_points_from_csv
from velocity_calculator import calculate_velocity
import sys

def main():
    print("Choose input method:")
    print("1. List of points")
    print("2. CSV file path")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        points_list = input("Enter a list of points separated by commas: ")
        points_completed = read_points_from_list(points_list)
    elif choice == '2':
        csv_path = input("Enter the path to the CSV file: ")
        points_completed = read_points_from_csv(csv_path)
    else:
        print("Invalid choice. Please enter '1' or '2'.")
        sys.exit(1)

    average_velocity = calculate_velocity(points_completed)
    print("Average Velocity:", average_velocity)

if __name__ == "__main__":
    main()
