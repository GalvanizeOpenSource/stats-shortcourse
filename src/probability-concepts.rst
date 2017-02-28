.. probability lecture

Definitions and Concepts
======================================


Sets
---------

The range of all possible outcomes or events, also called the **sample space**.

  * Coin flips
  * Cookies
  * Heights
  * Number of slices of pizza eaten before 10 am


Set Operations
-----------------

Union: :math:`A \cup B = \{x: x \in A \vee x\in B\}`

Intersection: :math:`A \cap B = \{x: x \in A \wedge x\in B\}`

Difference: :math:`A \setminus B = \{x: x \in A \wedge x \notin B\}`

Complement: :math:`A^C = \{x: x\notin A\}`

The null (empty) set: :math:`\emptyset`

DeMorgan's Law
^^^^^^^^^^^^^^^^^

:math:`\neg (A \vee B) \iff \neg A \wedge \neg B`

:math:`\neg (A \wedge B) \iff \neg A \vee \neg B`
   
   
.. note:: the :math:`\vee` and :math:`\wedge` refers to the logical
          `or` and the logical `and`.  Also :math:`\neg` is the
          negation logic operator (NOT)

Another useful notation is :math:`\mathbf{card}(A)` which is the *cardinality* or number of elements in `A` 


.. topic:: Sets in Python

   >>> a = set(["A","B","C","D"])
   >>> b = set(["C","D","E","F"])
   >>> c = set(["A","C","E","G"])
   

   * What is the intersection of the three groups?
   * What is the union of the three groups?
   * What do we get if we make a union of `a` and `b` then we intersect it with `c`

.. note:: When we get to NumPy be reminded that `there are set routines in NumPy <https://docs.scipy.org/doc/numpy/reference/routines.set.html>`_ and they are **fast**.
	       
