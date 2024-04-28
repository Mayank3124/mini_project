student_name = input("Enter the name of the student: ")
subject1_marks = int(input("Enter the marks for the first subject: "))
subject2_marks = int(input("Enter the marks for the second subject: "))
subject3_marks = int(input("Enter the marks for the third subject: "))
subject4_marks = int(input("Enter the marks for the fourth subject: "))
subject5_marks = int(input("Enter the marks for the fifth subject: "))

total_marks = subject1_marks + subject2_marks + subject3_marks + subject4_marks + subject5_marks
percentage = total_marks / 5

print("Your percentage is:", percentage)

if (subject1_marks > 100 or subject2_marks > 100 or subject3_marks > 100 or subject4_marks > 100 or subject5_marks > 100 or subject1_marks < 0 or subject2_marks < 0 or subject3_marks < 0 or subject4_marks < 0 or subject5_marks < 0):
    print("Error: Invalid marks entered.")
elif (percentage == 100):
    print("Congratulations", student_name + ", your grade is A+!")
elif (percentage >= 90):
    print("Well done", student_name + ", your grade is A+!")
elif (percentage >= 80):
    print("Good job", student_name + ", your grade is B+.")
elif (percentage >= 70):
    print("Good effort", student_name + ", your grade is B.")
elif (percentage >= 60):
    print("You passed", student_name + ", your grade is C.")
elif (percentage >= 50):
    print("Work harder", student_name + ", your grade is D.")
else:
    print("Sorry", student_name + ", you failed.")
