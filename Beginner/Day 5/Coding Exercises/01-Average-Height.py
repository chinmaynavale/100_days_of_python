# Without using sum().

student_heights = input('Enter a list of Student Heights ').split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)


sum_of_heights = 0
no_of_students = 0
for height in student_heights:
    sum_of_heights += height
    no_of_students += 1

average = sum_of_heights//no_of_students
print(f'\nAverage: {average}')
