from re import A


def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    score = float(input("Enter score:"))
    if score >= 0.9:
        grade = "A"
    elif score < 0.9 and score >= 0.8:
        grade = "B"
    elif score < 0.8 and score >= 0.7:
        grade = "C"
    elif score < 0.7 and score >= 0.6:
        grade = "D" 
    elif score < 0.6:
        grade = "F" 
    else:
        grade = "Bad score"
    print(grade)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculateGrade()