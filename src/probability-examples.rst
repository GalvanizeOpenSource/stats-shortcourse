.. probability lecture


Combinatorics
====================

The mathematics of ordering, choosing sets, etc. Useful for counting events in your sample space.

Factorials
--------------

If there are 10 lottery balls and we want draw them all, how many possible orderings are there?

>>> import math
>>> math.factorial(10)
3628800

Combinations
----------------

Number of ways to choose things when order doesn't matter

How many different pairs are there for afternoons sprints with 24 students?

>>> from itertools import combinations
>>> list(combinations("ABC",2))
[('A', 'B'), ('A', 'C'), ('B', 'C')]

This is also know as `N` choose `K`

It is the number of ways to select `k` objects from a pool of `n` objects

.. code-block:: python

   from math import factorial		
   def comb(n, k):
       return factorial(n) / factorial(k) / factorial(n - k)

>>> from scipy.misc import comb
>>> comb(3,2)
3.0

Permutations
----------------

Number of ways to choose things when order does matter.

On a baseball team with 20 players, how many different batting orders are there?

>>> from itertools import permutations
>>> list(permutations("ABC",2))
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

.. note:: High speed is retained by preferring `vectorized` building blocks over the use of for-loops and generators which incur interpreter overhead.
   
`itertools` also has a `groupby` that works like pandas.

