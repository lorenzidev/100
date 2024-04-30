students_heights = input("Insert the heights separated by a space! ").split()

for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])

total_height = 0
for heigh in students_heights:
    total_height += heigh

print(f"Total Height: {total_height}")

total_students = 0
for student in students_heights:
    total_students += 1

print(f"Number of students: {total_students}")

average_height = total_height / total_students

print(f"Average: {average_height:.2f}")