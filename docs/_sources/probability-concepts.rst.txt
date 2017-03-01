.. probability lecture

======================
 Probability Concepts
======================

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

Intersection: :math:`A \cap B = \{x: x \in A \wedge x\in B\}`

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

Further study
=============

If you want to learn more about working with sets in Python

`<https://www.programiz.com/python-programming/set>`_

If you want more about sets and set operations in general then check out the Khan academy video series on sets

`<https://www.khanacademy.org/math/statistics-probability/probability-library/basic-set-ops/v/intersection-and-union-of-sets>`_
	       
