#!/usr/bin/env python3

import os
import sys
import random

def gen(index: int):
	price = random.randrange(1, 1000)
	count = random.randrange(1, 10000)
	money = random.randrange(100, 1000000)

	val = money // price

	ret = int()

	if val > count:
		ret = count
	else:
		ret = val

	with open('{}/input/{}.in'.format(sys.argv[1], index), 'w') as fp:
		fp.write('{} {}\n{}\n'.format(price, count, money))

	with open('{}/output/{}.out'.format(sys.argv[1], index), 'w') as fp:
		fp.write('{}\n'.format(ret))


def main():
	if len(sys.argv) != 2:
		print('pass exercise\'s id as parameter 1')
		return

	os.makedirs('{}/input'.format(sys.argv[1]), exist_ok=True)
	os.makedirs('{}/output'.format(sys.argv[1]), exist_ok=True)

	n = int(input())

	for i in range(n):
		gen(i + 1)

if __name__ == '__main__':
	main()

