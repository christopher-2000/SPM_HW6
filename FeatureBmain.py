def main():
    print("Options:")
    print("1. Calculate Individual Effort Capacity from CSV")
    print("2. Calculate Team Effort Capacity from CSV")
    print("3. Exit")

    while True:
        option = input("Select an option: ")

        if option == "1":
            csv_file_path = input("Enter the path to the CSV file: ")
            sprint_days = int(input("Enter the number of sprint days: "))
            calculate_individual_and_team_capacity(csv_file_path, sprint_days)
        elif option == "2":
            csv_file_path = input("Enter the path to the CSV file: ")
            sprint_days = int(input("Enter the number of sprint days: "))
            total_team_hours = calculate_team_effort_capacity(csv_file_path, sprint_days)
            print("Total Team Effort Capacity:", total_team_hours, "hours")
        elif option == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()