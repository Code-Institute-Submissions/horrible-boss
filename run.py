employee = {"name": "David", "argue": 10, "rejuvenate_determination": 15, "determination": 100}
horrible_boss = {"name": "Chris", "argue": 12, "determination": 100}
arguement_running = True

while arguement_running == True:

    print("Please select action")
    print("1) Argue")
    print("2) Rejuvenate Determination")

    employee_action_selection = input()


    if employee_action_selection == "1":
        horrible_boss["determination"] = horrible_boss["determination"] - employee["argue"]
        employee["determination"] = employee["determination"] - horrible_boss["argue"]
        
        print(horrible_boss["determination"])
        print(employee["determination"])


    elif employee_action_selection == "2":
        print("Rejuvenate Determination")
    else: 
        print("Invalid Input")

    if employee["determination"] <= 0:
        arguement_running = False