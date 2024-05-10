student_scores = (input('Add the scores separated by spaces: ').split())

for i in range(len(student_scores)):
    student_scores[i] = int(student_scores[i])

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f'The highest score is {highest_score}')