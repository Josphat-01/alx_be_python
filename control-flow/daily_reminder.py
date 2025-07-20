task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

if time_bound == "yes":
    match priority:
        case "high":
         print("Reminder:",task, "is a high priority task that requires immediate attention today!")
        case "medium":
         print("Reminder:", task,"is a medium priority task that requires medium attention today!")

elif time_bound == "no":
  priority = "low"
  print("Note:", task, "is a low priority task. Consider completing it when you have free time!")

else:
    print("Re-write the task")


