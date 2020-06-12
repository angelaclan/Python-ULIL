----------------------
 ``complex1`` module
----------------------

:doc:`back <index>`


Complex numbers are represented with dictionaries 

Constructors
------------


.. autofunction:: complex1.create

.. autofunction:: complex1.from_real_number
				    
Selectors
---------

.. autofunction:: complex1.get_real_part

.. autofunction:: complex1.get_imag_part

Predicate
---------

.. autofunction:: complex1.are_equals

Functions
---------

.. autofunction:: complex1.modulus
		  
.. autofunction:: complex1.add

.. autofunction:: complex1.mul

.. autofunction:: complex1.print
									
Private functions
-----------------

These functions should not be used.

.. autofunction:: complex1.__to_string


Example
-------

Following code give a script example using :mod:`complex1`.
This script

* takes four float numbers on the line command,
* build two complex numbers,
* and print results of some calculations.

.. literalinclude:: ../src/main1.py
   :language: python
   :linenos:

Suppose this script in a file named :file:`main1.py`, here is an example using this script:
	  
.. code:: bash

   $  python3 main1.py 1 2 3 4
   z1 = 1.000000 + 2.000000i
   z1's modulus = 2.236068

   z2 = 3.000000 + 4.000000i
   z2's modulus = 5.000000
   
   z1 + z2 = 4.000000 + 6.000000i
   
   z1 * z2 = -5.000000 + 10.000000i


