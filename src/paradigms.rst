.. stats-shortcourse

Bayesian Inference
====================================================

Mini-objectives:

1. Review Probability
2. Discuss the philosophies
3. Bayes Rule again
4. Discuss Bayesian inference

Probability review	
----------------------------

I think it is helpful to keep in mind the major types of probabilities

   * Joint - :math:`P(A \cap B)`
   * Conditional - :math:`P(A | B)`
   * Marginal - :math:`P(A)`
     
Check out `this nicely written page on the topic <http://sites.nicholas.duke.edu/statsreview/probability/jmc/>`_

Recall that

   * :math:`P(A \cup B)` is the probability of A or B
   * :math:`P(A \cap B)` is the probability of A and B

`Try out these problems to get a better feel for things <http://cecs.wright.edu/~gdong/mining03/tuto1/lesson_1.html>`_
     
Conditional probability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:math:`\textrm{conditional} = \textrm{joint} / \textrm{marginal}`
      
:math:`P(B|A) = P(A \cap B) / P(A)`
      
.. note::

   **FROM LAST CLASS**

      * Three types of fair coins are in an urn: HH, HT, and TT
      * You pull a coin out of the urn, flip it, and it comes up H
      * Q: what is the probability it comes up H if you flip it a second time?

1. Figure out :math:`P(A \cap B)`
2. Figure out :math:`P(A)`
3. plug em in
   
:math:`P(X_2 = H \cap X_1 = H)` is probability that :math:`X_1 = H` **and** :math:`X_2 = H`

If you grab HH coin two head flips have probability: 1
but you could also grab HT coin and flip heads twice, probability:
:math:`\frac{1}{2} * \frac{1}{2} = \frac{1}{4}`

Each of those has probability :math:`\frac{1}{3}`
      
So :math:`P(X_2 = H \cap X_1 = H) = \frac{1}{3} * (1 + \frac{1}{4}) = \frac{5}{12}`

Finally :math:`P{X_1 = H}` is :math:`\frac{1}{2}`

Therefore :math:`P(X_2 = H | X_1 = H) = \frac{\frac{5}{12}}{\frac{1}{2}} = \frac{5}{6}`

Don't believe it? We can show this by simulation...

.. code-block:: python

   import random
   import pandas as pd

   coins = ['HH', 'HT', 'TT']
   results = []
   for i in range(10000):
       coin = random.choice(coins)
       results.append([random.choice(coin) for j in [1,2]])
   df = pd.DataFrame(results, columns=['first', 'second']) == 'H'
   df.groupby('first').mean()
		     
.. code-block:: none

          second
   first
   False  0.168256
   True   0.838502

.. note::

   **ANOTHER ONE**

   Given that it is a red card what is the probability that we draw a 4?
 
   `Answer explained here <http://sites.nicholas.duke.edu/statsreview/probability/jmc/>`_

A tale of two philosophies
-----------------------------
  
* **Frequentist** - assumes that the probability of an event is result of a long-run frequency of events
* **Bayesian** - assigns a degree of belief to an event

.. note::

   **DISCUSSION**

   Which one seems like a **better** choice for:

      * Probability of a car accident given a city
      * Predicting the result of an election
      * Predicting user behavior (e.g. A/B testing)
      * Identifying students with low test scores
   
* `Breast cancer subtype and ethnicity? <http://www.ncbi.nlm.nih.gov/pubmed/26454611>`_
* *TO REMEMBER* -- Are we making conclusions about a population in nature or about an individual?
* *TO REMEMBER* -- Neither of these philosophies are better in all cases

   "All models are wrong, but some are useful" --George Box
   
Bayes Theorem
----------------

   :math:`P(A|B) = \frac{P(B|A)P(A)}{P(B)}`    

   :math:`P(\theta|x) = \frac{P(x|\theta)P(\theta)}{P(x)}`    

The **posterior** is proportional to the **likelihood** times the **prior** distribution

Bayesian inference works by combining information about parameters :math:`\theta` contained in the observed data :math:`x` as quantified in the likelihood function :math:`p(x|\theta)`.  Classical statistics works by making inference about a single point, while Bayesian inference works on the whole distribution.  Parameters through the Bayesian lens are treated as random variables described by distributions.
  
The Philosophy of Bayesian Inference
----------------------------------------

You are a skilled programmer, but bugs still slip into your code. After a particularly difficult implementation of an algorithm, you decide to test your code on a trivial example. It passes. You test the code on a harder problem. It passes once again. And it passes the next, *even more difficult*, test too! You are starting to believe that there may be no bugs in this code...

But why?
-------------

* **Numerical Tractability** - can make hard problems *easier*
* **Absence of Asymptotics** - What *really* is a large number?
* **Ease of Error Propagation** - Dealing in uncertainty
* **Formal framework for combining information** - prior
* **Intuitive appeal** - interpretation is more intuitive
* **Everything is probabilities**

Then why isn't everyone a Bayesian?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Subjective** by nature
* **Great for complex models, but** is the overhead necessary?
* **Accessibility** - Many of the books out there are difficult reads
* Requires a deeper understanding of your model
* Implementations can quickly get hairy

Is the Bayesian paradigm more naturally aligned with the way we think?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Flip a coin, but I saw how it was going to land
* Code has a bug or not---are you certain?
* A doctor has a **belief** about a diagnosis based on symptoms and experience

The pieces
---------------------

* **prior** - :math:`P(\theta)` - one's beliefs about a quantity before presented with evidence 
* **posterior** - :math:`P(\theta|x)` - probability of the parameters given the evidence
* **likelihood** - :math:`P(x|\theta)`  - probability of the evidence given the parameters
* **normalizing constant** - :math:`P(x)`

.. note::
     
   **EXERCISE**

   Without looking...

   Write Bayes formula and talk about the pieces in terms of parameters and evidence

Don't forget about the :doc:`Bayes example in the previous section <probability>`
   
Further study
------------------

There is a lot so try not to get overwhelmed.  I feel that these two
resources are excellent entry points.  The thrid resource is a good
place to start if you want to start working with Bayesian models.

* `Probabilistic Programming and Bayesian Methods for Hackers <https://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers>`_ by `Cameron Davidson-Pilon <https://github.com/CamDavidsonPilon>`_

* `Entry level intro posted through kdnuggets <http://www.kdnuggets.com/2016/12/datascience-introduction-bayesian-inference.html>`_

Programming in the Bayesian landscape has become easier as a result of the use of probabilistic programming.

* `A repository introducing probabilistic programming in Python <https://github.com/GalvanizeOpenSource/probabilistic-programming-intro>`_
