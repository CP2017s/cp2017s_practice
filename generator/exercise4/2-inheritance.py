#!/usr/bin/env python3
# coding: UTF-8

import os
import sys
import names
import random as rand


def gen(index):
    n = rand.randrange(2, 50)
    m = rand.randrange(1, n)

    students = []
    student_names = set()
    school_students = set()

    for i in range(n):
        if rand.randrange(0, 1) is 0:
            gender = 'male'
        else:
            gender = 'female'

        name = names.get_first_name(gender)
        while name in student_names:
            name = names.get_first_name(gender)
        student_names.add(name)

        age = rand.randrange(1, 100)

        if gender is 'male':
            gender = 'Male'
        else:
            gender = 'Female'

        students.append({'name': name, 'age': age, 'gender': gender})

    while len(school_students) < m:
        for i in range(n):
            if rand.randrange(0, 1) is 0:
                school_students.add(i)
                students[i]['school'] = names.get_first_name()

                if len(school_students) == m:
                    break

    with open('{}/input/{}.in'.format(sys.argv[1], index), 'w') as fp:
        fp.write('{}\n'.format(n))

        for student in students:
            fp.write('{} {} {}\n'.format(student['name'], student['age'], student['gender']))

        fp.write('{}\n'.format(m))

        for idx in school_students:
            fp.write('{} {}\n'.format(students[idx]['name'], students[idx]['school']))

    with open('{}/output/{}.out'.format(sys.argv[1], index), 'w') as fp:
        for idx, student in enumerate(students):
            fp.write('{} is {} years old, and is {}\n'.format(student['name'], student['age'], student['gender']))
            if idx in school_students:
                fp.write('{} is studying in {}\n'.format(student['name'], student['school']))


def main():
    if len(sys.argv) != 2:
        print('pass exercise\'s id as parameter 1')
        return

    os.makedirs('{}/input'.format(sys.argv[1]), exist_ok=True)
    os.makedirs('{}/output'.format(sys.argv[1]), exist_ok=True)

    n = int(input())

    for index in range(n):
        gen(index + 1)


if __name__ == "__main__":
    main()
