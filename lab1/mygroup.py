#! /usr/bin/env python
# -*- coding: utf-8 -*-
groupmates = [
 {
 "name": "Александр",
 "surname": "Иванов",
 "exams": ["Информатика", "ЭЭиС", "Web"],
 "marks": [4, 3, 5]
 },
 {
 "name": "Иван",
 "surname": "Петров",
 "exams": ["История", "АиГ", "КТП"],
 "marks": [4, 4, 4]
 },
 {
 "name": "Кирилл",
 "surname": "Смирнов",
 "exams": ["Философия", "ИС", "КТП"],
 "marks": [5, 5, 5]
 },
 {
 "name": "Андрей",
 "surname": "Кот",
 "exams": ["Русский язык", "ОБЖ", "Литература"],
 "marks": [5, 4, 4]
 },
 {
 "name": "Анна",
 "surname": "Ли",
 "exams": ["Химия", "Биология", "История"],
 "marks": [5, 5, 5]
 },
 {
 "name": "Артур",
 "surname": "Яшкин",
 "exams": ["Физика", "Информатика", "Английский"],
 "marks": [3, 3, 3]
 }
]

def count_mark(students,mark):
    print ("Имя".ljust(15), "Фамилия".ljust(10), "Список экзаменов".ljust(40), "Оценки".ljust(20))
    for student in students:
        marks_list = student['marks']
        result =  (sum(marks_list)/len(marks_list))
        if result >= need:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(40), str(student["marks"]).ljust(20))

need = int(input('Введите средний балл:'))

count_mark(groupmates,need)
