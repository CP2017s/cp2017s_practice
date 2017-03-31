#!/usr/bin/env python3

import sys
import os
import random as rand


def gen(n) :
    size = rand.randrange(1,101);

    for total in range(0,n):
        fin = open("{}/input/{}.in".format(sys.argv[1], total+1),'w')
        fout = open("{}/output/{}.out".format(sys.argv[1], total+1),'w')
        result_name = []
        result_price = []
        fin.write(str(size)+"\n")
        for i in range(0,size):
            name = ""
            length = rand.randrange(1,101);
            for _ in range(0,length):
                name+=chr(rand.randrange(33,126))
            price = rand.randrange(0,100000)
            result_name.append(name)
            result_price.append(price)
            fin.write(name+" "+str(price)+"\n")
        fin.close()
        for i in range(0,size):
            fout.write(result_name[i]+"\n")
        for i in range(0,size):
            fout.write(str(result_price[i])+"\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('pass exercise\'s id as parameter 1')

    os.makedirs('{}/input'.format(sys.argv[1]), exist_ok=True)
    os.makedirs('{}/output'.format(sys.argv[1]), exist_ok=True)
	
    n = int(input())
    gen(n)
