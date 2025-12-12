task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match (priority.lower(), time_bound.lower()):
    case ("high", "yes"):
        print(f"Reminder: You have a high-priority task '{task}' that is time-bound. Please address it immediately!")
    case ("high", "no"):
        print(f"Reminder: You have a high-priority task '{task}'. Please address it as soon as possible.")
    case ("medium", "yes"):
        print(f"Reminder: You have a medium-priority task '{task}' that is time-bound. Please plan accordingly.")
    case ("medium", "no"):
        print(f"Reminder: You have a medium-priority task '{task}'. Please attend to it when you can.")
    case ("low", "yes"):
        print(f"Reminder: You have a low-priority task '{task}' that is time-bound. Don't forget to complete it.")
    case ("low", "no"):
        print(f"Reminder: You have a low-priority task '{task}'. You can complete it at your leisure.")
        