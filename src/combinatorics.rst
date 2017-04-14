.. probability lecture


Combinatorics
====================

   * The mathematics of counting, ordering, choosing sets, etc.
   * Useful for counting events in your sample space.

Factorials
--------------

If there are 10 lottery balls and we want draw them all, how many possible orderings are there?

>>> import math
>>> math.factorial(10)
3628800

Combinatorics
--------------------------------

Number of ways to choose things when **order does not matter**

>>> from itertools import combinations
>>> list(combinations("ABC",2))
[('A', 'B'), ('A', 'C'), ('B', 'C')]

This is also know as `N` choose `K`

It is the number of ways to select `k` objects from a pool of `n` objects

.. code-block:: python

   from math import factorial		
   def comb(n, k):
       return factorial(n) / (factorial(k) * factorial(n - k))

>>> from scipy.misc import comb
>>> comb(3,2)
3.0

.. note:: 

   **EXERCISE**
   
   >>> lefthand_beers = ["Milk Stout", "Good Juju", "Fade to Black", "Polestar Pilsner"]
   >>> lefthand_beers += ["Black Jack Porter", "Wake Up Dead Imperial Stout","Warrior IPA"]
   
   1. We have sampler plates that hold 4 beers.  How many different ways can we combine these beers? 
   2. Print a list of these pairs so we can identify the bad ones?

Source: `<lefthandbrewing.com/beers>`_
      
Permutations
----------------

Number of ways to choose things when order does matter.

.. code-block:: python
		
   from math import factorial
   def permu(n, k):
       return factorial(n) / factorial(n - k)

>>> from itertools import permutations
>>> list(permutations("ABC",2))
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

.. note::

   **EXERCISE**

   On a baseball team with 12 players, how many different batting orders are there?
   (Hint: only 9 people can bat in a given order)

.. note::

   **QUICK DISCUSSION**

   Explain to the person next to you the difference between
   permutations and combinations. Include in your explanation which
   one results in more possibilities.
   
Further study
------------------

   * `Khan academy video <https://www.khanacademy.org/math/precalculus/prob-comb/combinations/v/introduction-to-combinations>`_
   * `Khan academy practice <https://www.khanacademy.org/math/precalculus/prob-comb/combinations/e/permutations_and_combinations_2>`_
