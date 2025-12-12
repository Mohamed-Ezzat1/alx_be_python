task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority.lower() :
    case "high" :
        if time_bound.lower() == "yes":
            print(f"Reminder: Your high-priority task '{task}' is time-bound. Please address it immediately!")
        else:
            print(f"Reminder: Your high-priority task '{task}' needs your attention soon.")
    case "medium" :
        if time_bound.lower() == "yes":
            print(f"Reminder: Your medium-priority task '{task}' is time-bound. Please plan accordingly.") 
        else:
            print(f"Reminder: Your medium-priority task '{task}' should be completed in due time.")
    case "low" :
        if time_bound.lower() == "yes":
            print(f"Reminder: Your low-priority task '{task}' is time-bound. Try to fit it into your schedule.")
        else:
            print(f"Reminder: Your low-priority task '{task}' can be addressed at your convenience.")
    case _ :
        print("Invalid priority level entered. Please use high, medium, or low.")