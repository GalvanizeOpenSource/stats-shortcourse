.. probability lecture

======================
 Probability Concepts
======================

Probability is the discipline of mathematics designed to deal with random pheonomena.

.. note::

   ** EXERCISE **

   Think of an example of a random phenomenon.
   
   Talk with somebody next to you about whether it's possible to predict a
   random phenomenon? 

Sets
====

Sample space
------------

The range of all possible outcomes or events, also called the **sample space**.

   * Coin flips, die rolls, cards in deck
   * Cookies, jelly beans, teachers, meetups 
   * Heights, weights, volumes, temperatures, distances
   * Number of cups of coffee consumed before before 10 am
   * Number of beers... 

.. note:: 

   **EXERCISE**
   
   Talk with someone next to you about possible sample spaces for the
   above examples
  
Set Operations
--------------

Union: :math:`A \cup B = \{x: x \in A \vee x\in B\}`

  It is the event that **either** :math:`A` or :math:`B` or both occurs.

Intersection: :math:`A \cap B = \{x: x \in A \wedge x\in B\}`

  It is the event that **both** :math:`A` and :math:`B` simultaneously.

Difference: :math:`A \setminus B = \{x: x \in A \wedge x \notin B\}`

Complement: :math:`A^C = \{x: x\notin A\}`

The null (empty) set: :math:`\emptyset`

DeMorgan's Law's
----------------

De Morgan's laws says:

  1. The complement of the union of two sets is the same as the intersection of their complements
  2. The complement of the intersection of two sets is the same as the union of their complements

.. figure:: Demorganlaws.png
   :scale: 75%
   :align: center
   :alt: demorgans-laws
   :figclass: align-center
     
`<https://en.wikipedia.org/wiki/De_Morgan's_laws>`_

:math:`\neg (A \vee B) \iff \neg A \wedge \neg B`

:math:`\neg (A \wedge B) \iff \neg A \vee \neg B`
   
The :math:`\vee` and :math:`\wedge` refers to the logical
`or` and the logical `and`.  Also :math:`\neg` is the
negation logic operator (NOT)

Another useful notation is :math:`\mathbf{card}(A)` which is the *cardinality* or number of elements in `A` 

.. note::

   **EXERCISE**

   Copy the following 3 lines into a python interpreter, ipython session or script. 
		
   >>> a = set(["A","B","C","D"])
   >>> b = set(["C","D","E","F"])
   >>> sample_space = set(["A","B","C","D","E","F","G"])

   This is how you perform set operations in Python
   
   >>> a.intersection(b)
   set(['C', 'D'])
   >>> a.difference(b)
   set(['A', 'B'])
   >>> a.union(b))
   set(['A', 'B', 'C', 'D', 'E', 'F'])
   >>> complement_a = sample_space.difference(a)
   
   Can you show that De Morgan's laws work in Python?

Random variables
---------------------
   
   * Random variables formalize a mapping we have been implicitly using already
   * The set for a random variable occurs in real space 
      :math:`X(s) : S\Rightarrow \Re`
   * Capital letters refer to random variables.
   * Lowercase to refer to specific realization. 
      :math:`P(X=x) = P(\{s\in S : X(s) = x\})`
   * :math:`X \sim XYZ(\alpha, \beta, ...)` means X is distributed as, XYZ with parameters.
   * "i.i.d."
   * We denote the probability of X as P(X)
     
`Random variables (Khan academy) <https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/discrete-and-continuous-random-variables/v/random-variables>`_

Putting it together
^^^^^^^^^^^^^^^^^^^^^^^

Lets see how well we can put these concepts together.  This exercise also introduce the idea of mutual exclusivity.  If outcomes A and B cannot happen at the same time then :math:`P (A \cap B) = P (A) + P (B)`.

.. note::

   **EXERCISE**

   Lets use cholesterol ranges as an example.  Given that,

   .. math::
      A = (250 \leq chol \leq 299)

   .. math::
      B = (chol \geq 300)

   .. math::
      C = (chol \leq 280)

   :math:`A` and :math:`B` are **mutually exclusive**, but :math:`A` and :math:`C` are not.

   1. Discuss what it means to be mutually exclusive
	 
   2. What is the union of sets :math:`A` and :math:`C`?
      :math:`(A \cup B)` = ?
	 
   3. If :math:`P(A) = 0.2`, and :math:`P(B) = 0.1` then :math:`P(chol \geq 250)` = ?

      
Further study
=============

If you want to learn more about working with sets in Python

`<https://www.programiz.com/python-programming/set>`_

If you want more about sets and set operations in general then check out the Khan academy video series on sets

`<https://www.khanacademy.org/math/statistics-probability/probability-library/basic-set-ops/v/intersection-and-union-of-sets>`_
	       
