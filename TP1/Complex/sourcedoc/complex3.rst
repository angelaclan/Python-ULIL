----------------------
 ``complex3`` module
----------------------

:doc:`back <index>`


Complex numbers are objects of the class Complex

Class description
-----------------
.. autoclass::	complex3.Complex 


Methods
-------

.. automethod:: complex3.Complex.from_real_number

.. automethod:: complex3.Complex.get_real_part

.. automethod:: complex3.Complex.get_imag_part

.. automethod:: complex3.Complex.modulus

.. automethod:: complex3.Complex.add

.. automethod:: complex3.Complex.mul

.. automethod:: complex3.Complex.equals
								
Private methods
---------------
.. automethod:: complex3.Complex.__init__

Special methods
---------------
Here are special methods for class :class:`Complex` which allow using usual arithmetic or comparison operators.

.. automethod:: complex3.Complex.__abs__

.. automethod:: complex3.Complex.__neg__
				
.. automethod:: complex3.Complex.__add__
								
.. automethod:: complex3.Complex.__sub__
								
.. automethod:: complex3.Complex.__mul__

.. automethod:: complex3.Complex.__eq__

.. automethod:: complex3.Complex.__neq__

Following special method are for external representation of objects of class :class:`Complex`.

.. automethod:: complex3.Complex.__repr__

.. automethod:: complex3.Complex.__str__
				
Example
-------

Following code give a script example using :mod:`complex3`.
This script

* takes four float numbers on the line command,
* build two complex numbers,
* and print results of some calculations.

.. literalinclude:: ../src/main3.py
   :language: python
   :linenos:

Suppose this script in a file named :file:`main3.py`, here is an example using this script:
	  
.. code:: bash

   $  python3 main3.py 1 2 3 4
   z1 = 1.000000 + 2.000000i
   z1's modulus = 2.236068

   z2 = 3.000000 + 4.000000i
   z2's modulus = 5.000000
   
   z1 + z2 = 4.000000 + 6.000000i
   
   z1 * z2 = -5.000000 + 10.000000i

