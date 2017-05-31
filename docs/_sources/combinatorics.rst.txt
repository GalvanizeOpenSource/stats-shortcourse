.. probability lecture


Combinatorics
====================

Combinatorics is a branch of mathematics dedicated to figuring out how to count
things! Specifically, the number of elements contained 
in -- i.e., the **cardinality** -- of event :math:`A`:

.. math::
   \mathbf{card}(A) = |A|

Counting's not so hard, you say? Think again: when it comes to ordering and 
choosing sets in complicated and clever ways things can get tricky in heartbeat.
Be that as it may, combinatorics plays a fundamental and foundational role 
in probability as it forms the basis for assigning probabilities to events
in many contexts. Beyond that, the need to count
carefully and correctly is obviously a hugely important part of Data Science,
and it's important to have few of the "standard counting tricks" handy or 
you might make something a whole lot harder than it needs to be.  
For a good "industry perspective" on the importance and challenge of counting 
in data science check out 
`Counting in Data Science <http://daynebatten.com/2016/06/counting-hard-data-science/>`_.  


     
Factorials
--------------

**Factorials** count the number of ways to order a set of objects. 

E.g., if there are 10 lottery balls (labeled 1-10) and we draw them all, 
how many possible orderings could be drawn? The answer to this question is

* there are 10 choices for the first ball
* 9 choices for the second ball (because we've already drawn the first lottery ball)
* 8 choices for the third ball (because we've already drawn the first two lottery balls)
* and so on...

until there is only one ball left and we must pick it.
That is, there are :math:`10*9*8*\cdots*1 = 10!`, i.e.
*10 factorial*, possible orderings.

The number *10 factorial* can be calculated in Python, but watch out: factorials get really big really fast...

>>> import math
>>> math.factorial(10)
3628800

Combinations
--------------------------------

**Combinations** count the number of ways to choose things when 
**order does not matter**.  Here's an example of all the two character
*combinations* that can be made from the letters `A`, `B`, and `C`:

>>> from itertools import combinations
>>> list(combinations("ABC",2))
[('A', 'B'), ('A', 'C'), ('B', 'C')]

The "number of combinations" problem -- i.e., 
counting the number of all possible 
unordered collections of size `K` from a pool of `N` objects --- 
is often referred to as the "`N` choose `K`" problem, and the 
solution to the problem is commonly notated as  

.. math::
    \left(\begin{array}{c}N\\K\end{array}\right) = \displaystyle \frac{N!}{(N-K)!K!}

.. note:: 

   **EXERCISE**

   If you think about the "`N` choose `K`" solution carefully, 
   you can actually see that it makes
   sense: the :math:`K!` in the denominator is the number of ways to order a list 
   of length :math:`K`, whereas the :math:`\frac{N!}{(N-K)!}` is all possible
   lists of length :math:`K` where order matters.  With that in mind, see if you
   can think through why the formula counts the right thing.

If you're still a little confused about how the counting actually works,
don't worry, it's really easy to calculate combinations Python:

>>> from math import factorial		
>>> def comb(n, k):
... 	return factorial(n) / (factorial(k) * factorial(n - k))

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

*Permutations* counts the number of ways subsets can be chosen when 
**order does matter**. If you followed the "`N` choose `K`" thought exercise 
above then you won't be surprised to learn that the number of ways to 
choose `K` things out of `N` things **when order matters** is 

    :math:`\displaystyle \frac{N!}{(N-K)!}`

Explicitly writing out the formula makes it clear that permutations 
are just a slight variation on the factorial theme. And of
course, once again, it's easy to do permutations in Python:

.. code-block:: python
		
   from math import factorial
   def permu(n, k):
       return factorial(n) / factorial(n - k)

>>> from itertools import permutations
>>> list(permutations("ABC",2))
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

.. note::

   **EXERCISE**

   On a baseball team with 12 players, how many different batting lineups are there?
   
   Hint: there are 9 players in a lineup.

.. note::

   **PAIRED EXERCISE**

   Face off against the person next to you, pitting permutations against 
   combinations, and defending the dignity and honor of your position!
   No low blows are allowed, but don't be afraid to bring size into
   the argument if you think it helps your case.



.. Explain to the person next to you the difference between
.. permutations and combinations. Include in your explanation which
.. one results in more possibilities.
   
Further study
-------------

   * `Khan academy video <https://www.khanacademy.org/math/precalculus/prob-comb/combinations/v/introduction-to-combinations>`_
   * `Khan academy practice <https://www.khanacademy.org/math/precalculus/prob-comb/combinations/e/permutations_and_combinations_2>`_
