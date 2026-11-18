# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

math_marks = int(input("Enter marks of math: "))
physics_marks = int(input("Enter marks of physics: "))
chemistry_marks = int(input("Enter marks of chemistry: "))

total_marks = 300
get_marks = math_marks+physics_marks+chemistry_marks
get_marks_percentage = (get_marks/total_marks)*100

if(get_marks_percentage>=40):
    if(math_marks>=33 and physics_marks>=33 & chemistry_marks>=33):
        print("passed")
    else:
        print("Failed due to Indiviual subjects marks less than 33 but overall greater than 40")
else:
    print("Failed due to Overall subjects marks less than 40")            