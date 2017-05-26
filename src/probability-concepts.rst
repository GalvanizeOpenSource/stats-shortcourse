.. probability lecture

======================
 Probability Concepts
======================

Probability is a discipline of mathematics that studies analytical formulations 
of uncertainty that can be used characterize random phenomenon.


.. note::

   **EXERCISE**

   Think of an example of a random phenomenon.
   
   Talk with somebody next to you about whether it's possible to predict a
   random phenomenon? 

Sets
====

Random Variables
----------------
A **random variable** can be thought of as a *function* which outputs some 
"random phenomenon". 




Sample space
------------

The so-called **sample space** :math:`S` of a random variable :math:`X`
is a mathematical set listing all possible **outcomes** :math:`x^* \in S` 
that the random variable :math:`X` might actualize. An **event** :math:`E`
is a set comprised of these outcomes (:math:`E \subseteq S`).

**Outcomes**

   * Coin flips, die rolls, cards in deck
   * Cookies, jelly beans, teachers, meetups 
   * Heights, weights, volumes, temperatures, distances
   * Number of cups of coffee consumed before before 10 am
   * Number of beers... 

**Events**

   * "Half heads", "Odds", "Spades"
   * "With Chips", "Licorice", "Boring", "Data Science related meetup"
   * "Tall people" (>6 ft), "Small people" (<100 lbs), "Not full milk" (<1 G), "Frozen water (<32 F)", "close" (<2 mi)
   * "<2 cups of coffee before before 10 am"
   * ">5 beers, bro"...

.. note:: 

   **EXERCISE**
   
   Talk with your neighbor about possible sample spaces for the
   above examples
  
Set Operations for Building Complex Events
------------------------------------------

For an actualized (observed) value :math:`x^*` of a 
random variable :math:`X` and events :math:`A` and :math:`B`
defined on the sample space :math:`S` of :math:`X`

Union: :math:`A \cup B = \{x: x \in A \vee x\in B\}`

  is the event where :math:`x^*` implies **either** event :math:`A` or event :math:`B` or both occur.

Intersection: :math:`A \cap B = \{x: x \in A \wedge x\in B\}`

  is the event where :math:`x^*` implies **both** the event :math:`A` and the event :math:`B` occur.

Difference: :math:`A \setminus B = \{x: x \in A \wedge x \notin B\}`

  is the event where :math:`x` implies **only** the event :math:`A` occurs **but not** the event :math:`B`

Complement: :math:`\overline A = A^C = \{x: x\notin A\}`

  is the event where :math:`x^*` implies that event :math:`A` **does not** occur

The Null (empty) Set: :math:`\emptyset`

  is the event with no outcomes in it, which is not a possible event
  since an observed :math:`x^*` is an outcome.

.. note:: 

   **EXERCISE**
   
   Break out into groups with the people at your desk and distribute
   the creation of example *Unions*, *Intersections*, *Differences*, 
   *Complements*, and *Null Sets* based on events from the examples
   above and give an example of an *outcome* under which your example 
   event occurs.


DeMorgan's Law's 
-------------------------------------------------------------
(The next best thing to Bayes' rule and rum)

De Morgan's laws say:

  1. The complement of the union of two sets is the same as 
  the intersection of their complements

  :math:`\neg (A \vee B) \iff \neg A \wedge \neg B`

  2. The complement of the intersection of two sets is the same as 
  the union of their complements

  :math:`\neg (A \wedge B) \iff \neg A \vee \neg B`
   
where the expressions utilize the standard logic notation 
of :math:`\vee` and :math:`\wedge` for the
`or` and `and` operators, respectively, 
and :math:`\neg` for the negation operator ("not").


.. figure:: Demorganlaws.png
   :scale: 75%
   :align: center
   :alt: demorgans-laws
   :figclass: align-center
     
`<https://en.wikipedia.org/wiki/De_Morgan's_laws>`_


Another useful notation is :math:`\mathbf{card}(A)` which is the *cardinality*,
or number, of elements in :math:`A`.

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

Random Variables and Probability Distributions 
----------------------------------------------

   
A random variable :math:`X`  maps outcomes :math:`s` from its sample space :math:`S` onto the real numbers :math:`x \in \mathbb{R}`, i.e.,

        :math:`X(s) : S\rightarrow \in \mathbb{R}`

Standard notation utilizes capital letters for random variables, and lowercase letters for observed instantiations (realizations) of random variables. 

The realizations :math:`x` of a random random variable :math:`X` are governed according to the probability of outcomes :math:`s` defined in the sample space :math:`S`, i.e., 

        :math:`Pr(X=x \in E) = Pr(\{s\in S : X(s) \in E\})`

Some distributions -- known as **discrete distributions** -- define positive probabilities for :math:`s\in S`, thus it is meaningful to write 

       :math:`Pr(X=x) = Pr(\{s\in S : X(s)=x\})`

which is a so-called **probability MASS function**.

Perhaps surprisingly, other distributions -- known as **continuous distributions** -- do not define positive probabilities for :math:`s\in S` and instead only define probabilities on special sets :math:`E^* \subset S`.  For these continuous distributions we instead rely upon so-called **probability DENSITY functions** 

        :math:`f(X=x)`

which describes the behavior of realizations :math:`x` of a random random variable :math:`X` in a retaliative rather than absolute manner. Regardless of if a random variable has a discrete or continuous distribution, however, a standard notation for specifying the distribution of the random variable is

        :math:`X \sim XYZ(\alpha, \beta, ...)` 

which states that :math:`X` is distributed according to an :math:`XYZ` distribution with parameters :math:`\alpha` and :math:`\beta` and so on.

A set of random variables that are distributed according to the same probability distribution and do not "interfere" with each other (i.e., the realizations of one random variable do not influence the realizations of another random variable) are called **identically and independently distributed**, or **"i.i.d."**.


.. note::

   **QUESTION**

   Does a random variable have a "value" like a variable in python, or an
   algebraic expression?
     
`Random variables (Khan academy) <https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/discrete-and-continuous-random-variables/v/random-variables>`_

Putting it together
^^^^^^^^^^^^^^^^^^^^^^^

Now let's see how well we've put this all together by doing some  
exercises using the concepts we've learned along with a new idea 
called **mutual exclusivity**.  To get you started, here's a hint:
two events :math:`A` and :math:`B` are said to be *mutually exclusive* 
if :math:`Pr (X=x \in A \cup B) = Pr(X=x \in A) + Pr(X=x \in B)`. Good luck!

.. note::

   **EXERCISE**

   Let :math:`X` be a random variable which measures cholesterol 
   and :math:`x` an actual cholesterol measurement and define
   the following three events  

   .. math::
      A = (250 \leq chol \leq 300)

   .. math::
      B = (chol > 300)

   .. math::
      C = (chol \leq 280)

   where :math:`A` and :math:`B` are **mutually exclusive**, but :math:`A` and :math:`C` are not.

   1. Discuss what it means to be mutually exclusive.
	 
   2. What is the union of sets :math:`A` and :math:`C`?
      And how about :math:`(A \cup B)` = ?
 
   3. If :math:`Pr(X=x\in A) = 0.2` and :math:`Pr(X=x\in B) = 0.1`, 
   then :math:`Pr(X=x \geq 250)` = ?

   4. If :math:`P(X=x\in A) = .3` and :math:`P(X=x\in C)=.2`, then what would you need to know to calculate :math:`P(X=x \leq 300)`?

      
Further study
=============

If you want to learn more about working with sets in Python

`<https://www.programiz.com/python-programming/set>`_

If you want more about sets and set operations in general then check out the Khan academy video series on sets

`<https://www.khanacademy.org/math/statistics-probability/probability-library/basic-set-ops/v/intersection-and-union-of-sets>`_
	       
