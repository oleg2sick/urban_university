grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students)           #изменения типа: множество -> список

student_for_dict = students.sort()  #сортировка списка

average_grade = []                  #создание пустого списка

for i in range(len(grades)):                                #заполнение пустого списка средними оценками
    average_grade.append(sum(grades[i]) / len(grades[i]))

grades_dict = dict()                #создание пустого словаря

for i in range(len(students)):
    grades_dict.update({students[i]: average_grade[i]})     #заполнение пустого словаря именами учеников и их средними оценками

print(grades_dict)