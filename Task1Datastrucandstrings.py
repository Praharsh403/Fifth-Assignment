student_details = {"John": 85,"Susan": 76,"Ryan":80,"Carol": 90}

"""Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message."""

Name = input("Enter the student's name: ").strip().lower().title()   #makes sure that extra spaces are removed and if name written in in small its title word automatically gets uppercase to match and check.
if Name in student_details:                                  #Name is getting checked in dictionary
    print(f"{Name}'s marks : {student_details[Name]}")
else:
    print("Student not found")

"""The following program displays result of students name entered with their respective scores!"""