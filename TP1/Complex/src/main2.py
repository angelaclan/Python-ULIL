#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
	A little program using complex module. 
	
"""

import sys
import complex2


def main(x1, x2, x3, x4):

    z1 = complex2.Complex2(x1, x2)
    z2 = complex2.Complex2(x3, x4)

    print()
    print('z1 = {:f} + {:f}i'.format(z1.get_real_part(), z1.get_imag_part()))
    print ("z1's modulus = {:f}".format(z1.modulus ()))
    print()
    
    print('z2 = {:f} + {:f}i'.format(z2.get_real_part(), z2.get_imag_part()))
    print ("z2's modulus = {:f}".format(z2.modulus ()))
    print()
    
    z3 = z1.add(z2)
    print('z1 + z2 = {:f} + {:f}i'.format(z3.get_real_part(), z3.get_imag_part()))
    print()
    
    z4 = z1.mul(z2)
    print('z1 * z2 = {:f} + {:f}i'.format(z4.get_real_part(), z4.get_imag_part()))
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
