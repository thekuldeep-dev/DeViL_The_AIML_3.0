# 2. Write a program to accept marks of 6 students and display them in a sorted manner.
# 

marks = []

for i in range(6):
    s_marks = int(input(f"Enter marks of student {i+1}: "))
    marks.append(s_marks)
print(marks) 

marks.sort()
print(marks)
