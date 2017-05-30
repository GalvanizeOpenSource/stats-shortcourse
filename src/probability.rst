.. probability lecture

Probability
=============

Probability provides the mathematical tools we use to model 
and describe randomness. The likeliness of a random event is 
characterized either in terms of 

   * Long term frequency behavior, 
     if viewed from a *Frequentist* perspective
   * Our degree of belief expressed as a probability, 
     if viewed from a *Bayesian* perspective

*(We will return to a discussion between these two paradigms later).*

Naturally, probability provides the foundation for statistics and machine learning
as all (good) data analyses seek to identifiy patterns in data 
*while accounting for* the random sampling and measurement variation 
present in data populations under consideration. 
Perhaps counterintuitively, while probability statements seem easy to express and
interpret, our intuitions about randomness are often incorrect. This is because in
actual life we only live one realization of the randomness and don't experience
all the *counterfactual* outcomes that actually could have occured 
(but didn't actualize in our timeline).  To protect ourselves against faulty 
intuition, we need to approach probability problems using a methodical and 
objective framework that computes event probabilities by enumerating all 
possible outcomes (using combinatorics).

.. note::
	 
   **EXERCISE**

   1. What is the probability of a Queen in a 52 card deck?
   2. What is the probability of a Queen or a King?
   3. What is the probability of a Queen or a spade?


Formalization
---------------

There are three *axioms of probability*.

For some sample space :math:`S` with 
events :math:`A \subseteq S` and :math:`B \subseteq S`, 
a probability function `Pr` has these properties:

  1. The probability of any event is positive and less than or equal to 1, i.e.,

  .. math::
      0 \leq Pr(s \in A) = Pr(A) \leq 1

  where :math:`Pr(A)` is a common shorthand notational convenience

  2. The probability of a sure event is 1, i.e.,

  .. math::
      Pr(S) = 1
      
  3. If A and B are mutually exclusive, then:

  .. math::
      Pr(A \cup B) = Pr(A) + Pr(B)

  *(Remember that two events are mutually exclusive if they cannot both be true at the same time -- i.e., the two event sets are disjoint).*

From these three axioms all other familiar probability properties can be proven.
E.g.,

  a. The sum of the probabilities of an event and its complement is 1

  .. math::     	    
      Pr(A) + Pr\left(A^C\right) = Pr(S) = 1

  b. The probability of an impossible event is zero.

  .. math::
      Pr\left(S^C\right) = 0




      
Independence
--------------

Two events are **independent** (notated as :math:`A\bot B`) if

.. math::
   
   Pr(A\cap B) = Pr(A, B) = Pr(A)\times Pr(B)

or

.. math::
      
   Pr(A|B) = Pr(A)
   
where :math:`Pr(A|B)` denotes a **conditional probability** which gives
gives the probability of an event occuring *given the knowledge that* another 
event as occured.
When considering the independence of two events, ask yourself: "Does knowing 
somethign about event :math:`A` provide increased information about the 
likelihood of event :math:`B`?

.. note::
	 
   **PAIRED EXERCISE**

   Discuss with your neighbor what "knowing that :math:`A` has occurred" tells 
   us about the likelihood of :math:`B` occuring

   a. Under independence?

   b. Without independence?

   How you go about testing if two events were indeed independent?

.. note::
	 
   **QUESTION**

   What is the relationship between **independence** and **mutually exclusivity**?

     
Conditional Probability	
----------------------------

It turns out that it is always true that 

.. math::
   Pr(A \cap B) = Pr(A, B) = Pr(A|B) \times Pr(B)

where :math:`Pr(A, B)` is the standard way not specify *intersection* 
in statistical notation.  This rule is known as the **chain rule**, 
and we shall generalize it to more than two events shortly.  
But for now, rearranging this equation gives us 

.. math::
   Pr(A|B) = \frac{Pr(A, B)}{Pr(B)}

which is the definition of **conditional probability**.

.. note::

   **EXERCISE**
   
   Draw a Venn diagram for sample space :math:`S` with intersecting events 
   :math:`A` and :math:`B` to demonstrate the *Conditional Probability* formula.

.. note::

   **EXERCISE**

   Take a moment to think about this question:

      * Three types of fair coins are in an urn: HH, HT, and TT
      * You pull a coin out of the urn, flip it, and it comes up H
      * Q: what is the probability it comes up H if you flip it a second time?

   *Hint: write out the sample space!*

   When you're ready, compare your solution to those around you.


Chain Rule
----------

In probability theory, the **chain rule** provides a way to calculate 
probabilities sequentially for any number of events according
to the pattern of conditional probabilities

.. math::

   Pr(A, B, C) = Pr(A| B,C) \times Pr(B,C) = Pr(A|B,C) \times Pr(B|C) \times Pr(C)

where :math:`Pr(A)` is a shorthand notational convencience specifying
:math:`Pr(X=x \in A)`.



.. note::

   **EXERCISE**
   
   Calculate the probability of getting a Queen and a King if you draw
   two cards from a standard 52-card deck. 



Law of Total Probability
----------------------------

For a partition :math:`\{A_1, A_2, \cdots A_n\}` of a sample space `S`, i.e.,
a set of events such that :math:`\underset{i=1}{\overset{n}{\cup}} 
A_i = S` and :math:`A_i \cap A_j=\emptyset` for all :math:`i` and :math:`j`
such that :math:`1 \leq i \not = j \leq n`, and an event :math:`B \subseteq S`, 
the **Law of Total Probability** guarantees that

.. math::
   \displaystyle Pr(B) = \sum^n_{i=1} Pr(B\cap A_i) = \sum^n_{i=1} Pr(B|A_i) Pr(A_i)

.. note::

   **EXERCISE**
   
   Draw a Venn diagram for sample space :math:`S` partitioned 
   into :math:`\{A_1, A_2, \cdots A_n\}` and :math:`B \subseteq S`
   to demonstrates the *Law of Total Probability*.


Bayes' Theorem
---------------

**Bayes' theorem** is a formula for computing the conditional probability 
(or distribution) of
:math:`A|B` based on the reverse conditional probability (or distribution) of
:math:`B|A`.  Bayes’s theorem follows directly from a re-expression and a 
subsequent re-application of the chain rule:

.. math::

   P(B|A) = \frac{P(A, B)}{P(A)} = \frac{P(A|B)P(B)}{P(A)}

.. note::

   **EXERCISE**
   
   1. Prove *Bayes' theorem* using the *Chain Rule*.
   2. Use the *Law of Total Probability* to express :math:`P(A)` in terms of :math:`P(A|B_i)P(B_i)`, where :math:`B_i` is a partition of the sample space in question.

*(We will discuss a generalization of Bayes' theorem that results in an entire 
branch of statistics known as Bayesian statistics tomorrow).*


Medical Testing
^^^^^^^^^^^^^^^

Suppose we are interested in screening a population 
for some condition :math:`C` and have 
a test :math:`T` which predicts if the condition is present or not.

* The **positive predictive value** of the test is the probability that an individual who tested positive (i.e., :math:`i.e., T^{+}`) truly *does* have the condition (i.e., :math:`C^{+}`):

   :math:`PV^{+} = Pr(C^{+} |T^{+})`

* The **negative predicitve value** of the test is the probability that an individual who tested negative (i.e., :math:`T^{-}`) truly *does not* have the condition (i.e., :math:`C^{-}`):

   :math:`PV^{-} = Pr(D^{-} |T^{-} )`    

* The **sensitivity** of the test is the probability the test detects the condition (i.e., :math:`T^{+}`) when it should (i.e., when :math:`C^{+}` is true):

   :math:`Pr(T^{+} |C^{+})`
   
* The **specificity** of the test is the probability the test *does not* detect the condition (i.e., :math:`T^{-}`) when it shouldn't (i.e., when :math:`C^{-}` is true):

   :math:`Pr(T^{-} |C^{-})`

* And **prevalance** here refers to the overall rate at which the condition presentsitself in the poplulation being tested:

   :math:`Pr(C^{+})`
   
* And finally, note that :math:`Pr(T^{+} |C^{-} ) = 1 - \textrm{specificity}`

A common measure of the usefulness of a test is its *positive predictive value*
:math:`PV^{+}`:
   
   .. math::
      :nowrap:

      \begin{eqnarray}
      P (C^{+} |T^{+}) &=& \frac{P(T^{+}|C^{+}) P(C^{+})}{P(C^{+})P(T^{+}|C{+})+P(C^{-})P(T^{+}|C^{-})} \\
                       &=& \frac{Pr(C^{+}) \times \textrm{sensitivity}}{Pr(C^{+}) \times \textrm{sensitivity}+(1-Pr(C^{+})) \times (1-\textrm{specificity})} 
      \end{eqnarray}

which is just an example of *Bayes' theorem*.  
      
So, if we were given a test with sensitivity of 0.84 and specificity of 0.77
and apply the test to condition with with a prevalence of 0.20 in the 
population under examination, then

   .. math::
    
      PV^{+} = \frac{(0.2)(0.84)}{(0.2)(0.84)+(0.8)(0.23)}  = 0.48

and  

   .. math::

      PV^{-} = \frac{(0.8)(0.77)}{(0.8)(0.77)+(0.2)(0.16)}  = 0.95

.. note::

   **EXERCISE**
   
   Verify the that the answer given for :math:`PV^{-}` above is correct.


Further resources
-----------------

  * `<https://www.khanacademy.org/math/probability/probability-geometry/probability-basics/a/probability-the-basics>`_
  * `Visual introduction to probability and statistics <http://students.brown.edu/seeing-theory/basic-probability/index.html>`_
