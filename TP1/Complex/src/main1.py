#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
	A little program using complex module. 
	
"""

import sys
import complex1


def main(x1, x2, x3, x4):


    z1 = complex1.create(x1, x2)
    z2 = complex1.create(x3, x4)

    print()
    print('z1 = ',end='')
    complex1.print(z1)
    print ("z1's modulus = {:f}".format(complex1.modulus (z1)))
    print()

    print('z2 = ',end='')
    complex1.print(z2)
    print("z2's modulus = {:f}".format (complex1.modulus (z2)))
    print()
    
    print('z1 + z2 = ', end='')
    complex1.print(complex1.add(z1, z2))
    print()
    
    print('z1 * z2 = ', end='')
    complex1.print(complex1.mul(z1, z2))
    print()

    

def usage():
    print('Usage : {:s} x1 y1 x2 y2'.format(sys.argv[0]))
    print('with x1, y1, x2, y2 real numbers')
    exit(1)


if __name__ == "__main__":    

    if len(sys.argv) != 5:
        usage()
    else:
        try:
            x1 = float(sys.argv[1])
            y1 = float(sys.argv[2])
            x2 = float(sys.argv[3])
            y2 = float(sys.argv[4])
        except ValueError:
            print('Not a number')
            usage()
        main(x1, y1, x2, y2)
