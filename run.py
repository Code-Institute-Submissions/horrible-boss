employee = {"name": "David", "argue": 10, "rejuvenate_determination": 15, "determination": 100}
horrible_boss = {"name": "Chris", "argue": 13, "determination": 100}
meeting_running = True

while meeting_running == True:
    """
    Get employee action selection from the user
    """
    employee_won = False
    horrible_boss_won = False

    print("Please select action")
    print("1) Argue")
    print("2) Rejuvenate Determination")

    employee_action_selection = input(" :\n")


    if employee_action_selection == "1":
        """
        Calculates the determination of the user and computer
        to decide who wins based on the action chosen
        """
        horrible_boss["determination"] = horrible_boss["determination"] - employee["argue"]
        if horrible_boss["determination"] <= 0:
            employee_won = True

        else:
            employee["determination"] = employee["determination"] - horrible_boss["argue"]
            if employee["determination"] <= 0:
                horrible_boss_won = True
            
        print(horrible_boss["determination"])
        print(employee["determination"])


    elif employee_action_selection == "2":
        print("Rejuvenate Determination")
    else: 
        print("Invalid Input")

    if employee_won == True or horrible_boss_won == True:
        """
        Decides the outcome of the meeting
        """
        meeting_running = False