import csv
import sys

def read_points_from_list(points_list):
    try:
        return [int(x) for x in points_list.split(',')]
    except ValueError:
        print("Invalid input. Please provide a list of integers separated by commas.")
        sys.exit(1)

def read_points_from_csv(csv_path):
    try:
        with open(csv_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header
            points_completed = [int(row[1]) for row in reader]
            return points_completed
    except FileNotFoundError:
        print(f"Error: File '{csv_path}' not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error: Invalid data in '{csv_path}'. Please ensure the second column contains integers.")
        sys.exit(1)
    except IndexError:
        print(f"Error: Invalid CSV format in '{csv_path}'. Please ensure it has at least two columns.")
        sys.exit(1)
