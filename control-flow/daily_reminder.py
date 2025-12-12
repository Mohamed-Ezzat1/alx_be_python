task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority.lower() :
    case "high" if time_bound.lower() == "yes":
        print(f"Reminder: Your high-priority task '{task}' is time-bound. Please address it immediately!")
    case "high":
        print(f"Reminder: Your high-priority task '{task}' needs your attention soon.")
    case "medium" if time_bound.lower() == "yes":
        print(f"Reminder: Your medium-priority task '{task}' is time-bound. Try to complete it on time.")
    case "medium":
        print(f"Reminder: Your medium-priority task '{task}' should be completed in due course.")
    case "low" if time_bound.lower() == "yes":
        print(f"Reminder: Your low-priority task '{task}' is time-bound. Don't forget to finish it.")
    case "low":
        print(f"Reminder: Your low-priority task '{task}' can be done at your convenience.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")

        