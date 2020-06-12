#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`complex3` module : version 3 of a (simple) module for complex numbers

:author: `FIL - Faculté des Sciences et Technologies - 
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2017, september. Last revision: 2017, september

Complex numbers are objects 

.. seealso::
           :mod:`complex2`

"""

import math

class Complex(object):
    """
    class for complex numbers

    >>> z1 = Complex(1, 2)
    >>> z1.get_real_part()
    1.0
    >>> z1.get_imag_part()
    2.0
    >>> z1.modulus() == math.sqrt(5)
    True
    >>> z2 = Complex.from_real_number(3)
    >>> z1.equals(z2)
    False
    >>> z3 = z1.add(z2)
    >>> z3.equals(Complex(4, 2))
    True
    >>> z4 = z1.mul(z2)
    >>> z4.equals(Complex(3, 6))
    True
    >>> z4
    Complex(3.0, 6.0)
    >>> print(z1 + z2)
    4.000000 + 2.000000i
    >>> print(z1 * z2)
    3.000000 + 6.000000i
    >>> print(-z1)
    -1.000000 + -2.000000i
    >>> print(z2 - z1)
    2.000000 + -2.000000i
    >>> z1 * z2 == z4
    True
    >>> z1 != z2
    True
    """
    
    def __init__(self, real_part, imag_part):
        """
        create a complex number with real part real_part and imaginary part imag_part.

        This method is implicitely called at object creation.

        :param real_part: 
        :type real_part: int or float
        :param imag_part: 
        :type imag_part: int or float
        :raises: ``AssertionError`` if params are not int or float numbers
        :Example:
        
        >>> z = Complex(3, 2)
        >>> z.get_real_part()
        3.0
        >>> z.get_imag_part()
        2.0
    
        """
        assert type(real_part) in {int, float}, 'first argument is not int or float' 
        assert type(imag_part) in {int, float}, 'second argument is not int or float' 
        self.__real_part = float(real_part)
        self.__imag_part = float(imag_part)

    def from_real_number(x):
        """
        create a complex number with real part x and zero imaginary part.

        :param x: (int or float)
        :return: a new complex number x + 0.0i
        :rtype: Complex
        :UC: none
        :Example:
        
        >>> z = Complex.from_real_number(3)
        >>> z.get_real_part()
        3.0
        >>> z.get_imag_part()
        0.0
        """
        assert type(x) in {int, float}, 'argument is not int or float'
        return Complex(float(x), 0.0)

    def __repr__(self):
        """
        :return: an external representation of complex number self
           (for visualizing complex numbers value in interactive mode for example)
        :rtype: str
        :UC: none
        :Example:

        >>> Complex(3, 2)
        Complex(3.0, 2.0)
        """
        return 'Complex({}, {})'.format(self.__real_part, self.__imag_part)
    
    def __str__(self):
        """
        :return: an external representation of complex number self 
           (for printing complex numbers for example)
        :rtype: str
        :UC: none
        :Example:

        >>> z = Complex(3, 2)
        >>> z.__str__()
        '3.000000 + 2.000000i'
        >>> print(z)
        3.000000 + 2.000000i
        """
        return '{:f} + {:f}i'.format(self.__real_part, self.__imag_part)

    def __eq__(self, z):
        """
        :return: 
           - True if complex numbers self and z are equals
           - False otherwise
        :rtype: bool
        :UC: none
        :Example:

        >>> Complex(3, 2) == Complex(3, 2)
        True
        >>> Complex(3, 2) == Complex(2, 2)
        False
        """
        return self.equals(z)

    def __neq__(self, z):
        """
        :return: 
           - True if complex numbers self and z are not equals
           - False otherwise
        :rtype: bool
        :UC: none
        :Example:

        >>> Complex(3, 2) != Complex(2, 2)
        True
        >>> Complex(3, 2) != Complex(3, 2)
        False
        """
        return not self.equals(z)

    
    def __abs__(self):
        """
        :return: modulus of self
        :rtype: float
        :UC: none
        :Example:

        >>> z = Complex(3, 2)
        >>> abs(z) == math.sqrt(13)
        True
        """
        return self.modulus()
    

    def __add__(self, z):
        """
        :return: the sum of complex numbers self and z
        :rtype: Complex
        :UC: none
        :Example:

        >>> Complex(1, 2) + Complex(3, 4)
        Complex(4.0, 6.0)
        """
        return self.add(z)

    def __mul__(self, z):
        """
        :return: the product of complex numbers self and z
        :rtype: Complex
        :UC: none
        :Example:

        >>> Complex(1, 2) * Complex(3, 4)
        Complex(-5.0, 10.0)
        """
        return self.mul(z)

    def __neg__(self):
        """
        :return: the opposite complex number -self
        :rtype: Complex
        :UC: none
        :Example:

        >>> -Complex(1, 2)
        Complex(-1.0, -2.0)
        """
        return Complex(-self.__real_part, -self.__imag_part)

    def __sub__(self, z):
        """
        :return: the complex number self - z
        :rtype: Complex
        :UC: none
        :Example:

        >>> Complex(1, 2) - Complex(3, 4)
        Complex(-2.0, -2.0)
        """
        return self + -z

    def get_real_part(self):
        """
        return the real part of complex number self

        :return: the real part of self
        :rtype: float
        :UC: None
        :Example:

        >>> z = Complex(3, 2)
        >>> z.get_real_part()
        3.0
        """
        return self.__real_part

    def get_imag_part(self):
        """
        return the imaginary part of complex number self

        :return: the imanigary part of self
        :rtype: float
        :UC: None
        :Example:

        >>> z = Complex(3, 2)
        >>> z.get_imag_part()
        2.0
         """
        return self.__imag_part

    def equals(self, z):
        """
        :return: 
           - True if complex number self equals complex number z2
           - False otherwise
        :rtype: bool
        :UC: none
        :Example:

        >>> z = Complex(1, 2)
        >>> z.equals(Complex(1, 2))
        True
        >>> z.equals(Complex(-1, 2))
        False
        """
        return self.__real_part == z.get_real_part() and self.__imag_part == z.get_imag_part() 

    def modulus(self):
        """
        :return: modulus of complex number self, ie :math:`\sqrt{x^2 + y^2}` 
            if :math:`z = x + yi`.
        :rtype: float
        :UC: none
        :Example:

        >>> z = Complex(3, 2)
        >>> z.modulus() == math.sqrt(13)
        True
        """
        x = self.__real_part
        y = self.__imag_part
        return math.sqrt(x ** 2 + y ** 2)

    def add(self, z):
        """
        :param z: 
        :type z: Complex
        :return: the sum of complex numbers self and z.
        :rtype: Complex
        :UC: none
        :Example:

        >>> z = Complex(1, 2).add(Complex(3, 4))
        >>> z.get_real_part()
        4.0
        >>> z.get_imag_part()
        6.0
        """
        x1 = self.__real_part
        y1 = self.__imag_part
        x2 = z.get_real_part()
        y2 = z.get_imag_part()
        return Complex(x1 + x2, y1 + y2)

    def mul(self, z):
        """
        :param z: 
        :type z: Complex
        :return: the product of complex numbers self and z.
        :rtype: Complex
        :UC: none
        :Example:

        >>> z = Complex(1, 2).mul(Complex(3, 4))
        >>> z.get_real_part()
        -5.0
        >>> z.get_imag_part()
        10.0
        """
        x1 = self.__real_part
        y1 = self.__imag_part
        x2 = z.get_real_part()
        y2 = z.get_imag_part()
        return Complex(x1 * x2 - y1 * y2, x1 * y2 + y1 * x2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()


