#Program to check the grade of given marks


marks=int(input("Enter your marks"))
if marks >= 90:
    print("Your grade is A+")
elif marks > 80 and marks < 89:
    print("Your garde is A")
elif marks > 70 and marks < 79:
    print("Your grade is B+")
elif marks > 60 and marks < 69:
    print("Your grade is B")
else:
    print("You need a retest")
