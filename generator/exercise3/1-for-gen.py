#!/usr/bin/env python3

import os
import sys
import random


def gen(n: int, index: int):
	val = n * (n + 1) // 2
	
	with open('{}/input/{}.in'.format(sys.argv[1], index), 'w') as fp:
		fp.write('{}\n'.format(n))
	
	with open('{}/output/{}.out'.format(sys.argv[1], index), 'w') as fp:
		fp.write('{}\n'.format(val))

def main():
	if len(sys.argv) != 2:
		print('pass exercise\'s id as parameter 1')
		return

	os.makedirs('{}/input'.format(sys.argv[1]), exist_ok=True)
	os.makedirs('{}/output'.format(sys.argv[1]), exist_ok=True)

	n = int(input())

	for i in range(n):
		gen(random.randrange(1, 10000), i + 1)


if __name__ == '__main__':
	main()

