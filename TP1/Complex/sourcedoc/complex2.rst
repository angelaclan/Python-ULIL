----------------------
 ``complex2`` module
----------------------

:doc:`back <index>`


Complex numbers are objects of the class Complex

Class description
-----------------
.. autoclass::	complex2.Complex2 


Methods
-------

.. automethod:: complex2.Complex2.from_real_number

.. automethod:: complex2.Complex2.get_real_part

.. automethod:: complex2.Complex2.get_imag_part

.. automethod:: complex2.Complex2.modulus

.. automethod:: complex2.Complex2.add

.. automethod:: complex2.Complex2.mul

.. automethod:: complex2.Complex2.equals
								
Private methods
---------------
.. automethod:: complex2.Complex2.__init__


Example
-------

Following code give a script example using :mod:`complex2`.
This script

* takes four float numbers on the line command,
* build two complex numbers,
* and print results of some calculations.

.. literalinclude:: ../src/main2.py
   :language: python
   :linenos:

Suppose this script in a file named :file:`main2.py`, here is an example using this script:
	  
.. code:: bash

   $  python3 main2.py 1 2 3 4
   z1 = 1.000000 + 2.000000i
   z1's modulus = 2.236068

   z2 = 3.000000 + 4.000000i
   z2's modulus = 5.000000
   
   z1 + z2 = 4.000000 + 6.000000i
   
   z1 * z2 = -5.000000 + 10.000000i

