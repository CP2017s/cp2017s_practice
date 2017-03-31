#!/usr/bin/env python3
# coding: UTF-8

import os
import sys
import random
import names

MAX_NUM = 50


def gen(index, name_set, age_list, group_set):
    name_list = list(name_set)
    group_list = list(group_set)

    with open('{}/input/{}.in'.format(sys.argv[1], index), 'w') as fp:
        for name, age, group in zip(name_list, age_list, group_list):
            fp.write('{} {} {}\n'.format(name, age, group))

        fp.write('QUIT 0 QUIT\n')

    with open('{}/output/{}.out'.format(sys.argv[1], index), 'w') as fp:
        for name, age in zip(name_list, age_list):
            fp.write('{} is {} years old.\n'.format(name, age))

        for name, age, group in zip(name_list, age_list, group_list):
            fp.write('{} : {}, {} years old.\n'.format(name, group, age))


def main():
    if len(sys.argv) != 2:
        print('pass exercise\'s id as parameter 1')
        return

    os.makedirs('{}/input'.format(sys.argv[1]), exist_ok=True)
    os.makedirs('{}/output'.format(sys.argv[1]), exist_ok=True)

    n = int(input())

    for i in range(n):
        n = random.randrange(1, MAX_NUM)

        name_set = set()
        group_set = set()
        age_list = []

        while len(name_set) <= n:
            name_set.add(names.get_first_name())

        while len(group_set) <= n:
            group_set.add(names.get_last_name())

        for _ in range(n):
            age_list.append(random.randrange(1, 100))

        gen(i + 1, name_set, age_list, group_set)


if __name__ == '__main__':
    main()
