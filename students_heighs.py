# Input principal para saber quantos estudantes.
quantity = int(input('How many students? '))

# Lista que será utilizada para armazenar as alturas.
students_heigh = []
students_total_heigh = 0

for i in range(quantity):
    student_heigh = int(input(f"Enter the student heigh in centimeters: "))
    students_heigh.append(student_heigh)
    students_total_heigh += student_heigh

average = students_total_heigh / quantity

print(f'Heighs: {students_heigh} \nThe average is {average:.2f} cm')