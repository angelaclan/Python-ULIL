#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`complex1` module : version 1 of a (simple) module for complex numbers

:author: `FIL - Faculté des Sciences et Technologies - 
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2015, september. Last revision: 2017, september

Complex numbers are represented with dictionaries 

.. seealso::
           :mod:`complex2`


Provides :

* create : complex constructor
* get_real_part : real part selector
* get_imag_part : imaginary part selector
* modulus : modulus
* add : complex numbers addition
* mult : complex numbers multiplication

"""

import builtins, math

def create(real_part, imag_part):
    """
    create a complex number with real part  and imaginary part 

    :param real_part: the real part of the complex number to create
    :type real_part: int or float
    :param imag_part: the imaginary part of the complex number to create
    :type real_part: int or float
    :return: the complex number real_part + i imag_part
    :rtype: complex
    :UC: none
    :Example:

    >>> z = create(1, 2)
    >>> get_real_part(z)
    1.0
    >>> get_imag_part(z)
    2.0
    """
    assert type(real_part) in {int, float}, 'first argument is not int or float' 
    assert type(imag_part) in {int, float}, 'second argument is not int or float' 
    return {'re' : float(real_part), 'im' : float(imag_part)}

def from_real_number(x):
    """
    create the complex number x + i0 from real number x

    :param x: a real number
    :type x: int or float
    :return: the complex number x + 0i
    :rtype: complex
    :UC: none
    :Example:

    >>> z = from_real_number(1)
    >>> get_real_part(z)
    1.0
    >>> get_imag_part(z)
    0.0
    """
    return create(x, 0)


def get_real_part(z):
    """
    return the real part of complex number z

    :param z: a complex number
    :type z: complex
    :return: the real part of z
    :rtype: float
    :UC: none
    :Example:

    >>> z = create(1, 2)
    >>> get_real_part(z)
    1.0
    """
    return z['re']

def get_imag_part(z):
    """
    return the imaginary part of complex number z

    :param z: a complex number
    :type z: complex
    :return: the imaginary part of z
    :rtype: float
    :UC: none
    :Example:

    >>> z = create(1, 2)
    >>> get_imag_part(z)
    2.0
    """
    return z['im']

def are_equals(z1, z2):
    """
    return True if complex numbers z1 and z2 are equals
           False otherwise

    :param z1: a complex number
    :type z1: complex
    :param z2: a complex number
    :type z2: complex
    :return: True if z1 = z2, False otherwise
    :rtype: bool
    :UC: none
    :Example:

    >>> z1 = create(1, 2)
    >>> z2 = create(1, 2)
    >>> z3 = create(1, -1)
    >>> are_equals(z1, z2)
    True
    >>> are_equals(z1, z3)
    False
    """
    return get_real_part(z1) == get_real_part(z2) and get_imag_part(z1) == get_imag_part(z2) 

def modulus(z):
    """
    return the modulus of complex number z, ie :math:`\sqrt{x^2 + y^2}` 
    if :math:`z=x+yi`.

    :param z: a complex number
    :type z: complex
    :return: its modulus
    :rtype: float
    :UC: none
    :Example:

    >>> modulus(create(0, 0))
    0.0
    >>> modulus(create(3, 4))
    5.0
    """
    x = get_real_part(z)
    y = get_imag_part(z)
    return math.sqrt(x ** 2 + y ** 2)

def add(z1, z2):
    """
    return the sum of the two complex numbers z1 and z2
    
    :param z1: a complex number
    :type z1: complex
    :param z2: a complex number
    :type z2: complex
    :return: z1 + z2
    :rtype: complex
    :UC: none
    :Example:

    >>> z = add(create(1, 2), create(3, 4))
    >>> get_real_part(z)
    4.0
    >>> get_imag_part(z)
    6.0
    """
    x1 = get_real_part(z1)
    y1 = get_imag_part(z1)
    x2 = get_real_part(z2)
    y2 = get_imag_part(z2)
    return create(x1 + x2, y1 + y2)

def mul(z1, z2):
    """
    return the product of the two complex numbers z1 and z2
    
    :param z1: a complex number
    :type z1: complex
    :param z2: a complex number
    :type z2: complex
    :return: z1 * z2
    :rtype: complex
    :UC: none
    :Example:

    >>> z = mul(create(1, 2), create(3, 4))
    >>> get_real_part(z)
    -5.0
    >>> get_imag_part(z)
    10.0
    
    """
    x1 = get_real_part(z1)
    y1 = get_imag_part(z1)
    x2 = get_real_part(z2)
    y2 = get_imag_part(z2)
    return create(x1 * x2 - y1 * y2, x1 * y2 + y1 * x2)
    
def __to_string(z):
    """
    return a string representation of the complex number z with algebraic form
    `x+yi` where x = real part of z and y = imaginary part

    :param z: complex number to convert
    :type z: complex
    :return: a string representation of z
    :rtype: string
    :UC: none
    :Example:

    >>> z = create(1, 2)
    >>> __to_string(z)
    '1.000000 + 2.000000i'
    """
    return '{:f} + {:f}i'.format(get_real_part(z), get_imag_part(z))

def print(z, end='\n'):
    """
    print the complex number z with algebraic form `x + yi`
    where x = real part of z and y = imaginary part

    :param z: complex number to print
    :type z: complex
    :param end: [optional] separator (default is '\\\\n')
    :type end: string
    :return: None
    :UC: none
    :Example:

    >>> z = create(1, 2)
    >>> print(z)
    1.000000 + 2.000000i
    """
    builtins.print(__to_string(z), end=end)


if __name__ == '__main__':
    import doctest
    doctest.testmod()


