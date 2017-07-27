.. stats-shortcourse

Bayesian Inference
====================================================


Mini-objectives:

  1. Review Probability
  2. Discuss Statistical Philosophies
  3. Repurpose Bayes' rule for Distributions 
     (and start callling it Bayes' Theorem)
  4. Discuss Bayesian Inference

Probability Review	
------------------

Recall that we have learned about *three* probability estimands

* Joint: :math:`Pr(A \cap B)`
* Conditional: :math:`Pr(A | B)`
* Marginal: :math:`Pr(A)`
     
These concepts `are reviewed here
<http://sites.nicholas.duke.edu/statsreview/probability/jmc/>`_ and
some related practice problems `are available here
<http://cecs.wright.edu/~gdong/mining03/tuto1/lesson_1.html>`_.

.. note::

   **EXERCISE**
   
   Specify the *conditional* probability in terms of 
   *joint* and *marginal* probabilities. 
     
Conditional probability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Recall the exercise from yesterday

.. note::

   **PREVIOUSLY**

   * Three types of fair coins are in an urn: HH, HT, and TT
   * You pull a coin out of the urn, flip it, and it comes up H
   * Q: what is the probability it comes up H if you flip it a second time?

.. note::

   **SOLUTION**

   The way you solved this problem yesterday was to list out the 
   sample space and count the outcomes comprising the event of interest. 
   But of course this problem can also be solved analytically. 
   To do so we calculate

   1. :math:`Pr(F_1=H \cap F_2=H)`
   2. :math:`Pr(F_1=H)`
   3. :math:`Pr(F_2=H|F_1=H) = \frac{Pr(F_1=H, F_2=H)}{Pr(F_1=H)}`

   as 

   :math:`\begin{eqnarray}Pr(F_1=H \cap F_2=H) &=& \underset{c \in \{HH,HT,TT\}}{\sum}Pr(F_1=H \cap F_2=H | C=c) Pr(C=c)\\&=&1\times\frac{1}{3}+\frac{1}{4}\times\frac{1}{3}+0\times\frac{1}{3} = \frac{5}{12}\\\\\\Pr(F_1=H) &=& \underset{c \in \{HH,HT,TT\}}{\sum}Pr(F_1=H | C=c) Pr(C=c)\\&=&1\times\frac{1}{3}+\frac{1}{2}\times\frac{1}{3}+0\times\frac{1}{3} = \frac{1}{2}\\\\\\\Pr(F_2=H|F_1=H) &=& \frac{5/12}{1/2}=\frac{5}{6}\end{eqnarray}`
   
So we first answered this question 
*counting outcomes in events based on the sample space*, and  
now we answered it using the *law of total probability*. 
But if you're still skeptical about our answer,
perhaps just *simulating* the experiment will help convince you:

.. note::

   **EXERCISE**

   Figure out what the following code does and try it out!

   .. code-block:: python

     import random
     import pandas as pd

     coins = ['HH', 'HT', 'TT']
     results = []
     for i in range(10000):
         coin = random.choice(coins)
         results.append([random.choice(coin) for j in [1,2]])
     df = pd.DataFrame(results, columns=['first', 'second']) == 'H'

     # df.groupby('first').mean()
     # 5./6
 
Simulation is a great way to confirm your answers to different problem.
It's a general purpose tool that you should always remember to keep at 
your disposal when you're trying to figure out how something works.  
Just even the process of creating the simulation can be helpful to nail
down your understanding of a problem. 

If you are not familiar with pandas,
here is another way of simulating the conditional probability.

.. code-block:: python

   import numpy as np

   n = 10000
   coins = ['HH', 'HT', 'TT']
   coins_selected = np.random.choice(coins,n)
   first_side_shown = np.array([c[np.random.random_integers(0,1,1)[0]] for c in coins_selected])
   coins_with_heads = coins_selected[np.where(first_side_shown == 'H')[0]]
   second_side_shown = np.array([c[np.random.random_integers(0,1,1)[0]] for c in coins_with_heads])
   print("%s/%s"%(np.where(second_side_shown=='H')[0].size,second_side_shown.size))
   print(np.where(second_side_shown=='H')[0].size/second_side_shown.size)  

.. code-block:: python
     
   4096/4938
   0.8295



More discussion about conditional probabilities can be found `here <http://sites.nicholas.duke.edu/statsreview/probability/jmc/>`_.
   
Bayesian Inference
------------------

**Bayesian inference** is based on the idea that *distributional parameters*
:math:`\theta` can themselves be viewed as *random variables* with their
own distributions.  This is distinct from the **Frequentist** perspective which
views parameters as *known and fixed constants* to be estimated. E.g.,
"If we measured everyone's height instantaneously, at that moment there would
be *one true average height* in the population."  Regardless of one's philosophical
perspective, both approaches have value in practice.

The key computational step in the Bayesian framework is deriving the posterior
distribution, which is done using the a forumula we have already seen; namely 
Bayes' theorem: 

.. math::

   P(\theta|X) = \frac{P(X|\theta)P(\theta)}{P(X)}

Bayes' theorem is comprised of

       * :math:`P(\theta|X)` -- the **posterior distribution**
       * :math:`P(X|\theta)` -- the **likelihood function**
       * :math:`P(\theta)` -- the **prior distribution**
       * :math:`P(X)` -- the **marginal likelihood**

Just as the *posterior distribution* is the central estimand in Bayesian statistics,
the likelihood function is the central piece of machinery in a Frequentist context.
But as you can see from the formula, the posterior is simply a kind of
"re-weighting" of the likelihood function (so Bayesian and frequentist inference  
must not be completely at odds -- they agree on at least *something*).  
The re-weighting is accomplished
by striking a balance between the *likelihood function* and the
*prior distribution*. The *prior* distribution represents our belief about the
parameter prior to seeing the data, while the *likelihood function* tells us
what the data implies about the parameter -- and then these two perspectives
are reconciled.  The *marginal likelihood* turns out to just be a constant which
ensures that the posterior is a *probability mass function* or a *probability
density function* (i.e., sums to one or has area one).  As such, in many
contexts the *marginal likelihood* simply represents a formality that is not
crucial to the posterior calculation; however, sometimes it is useful (although
it can be difficult to obtain).  Interestingly, the *marginal likelihood* can be
used for Bayesian model selection, so for some tasks it is an estimand of
primary importance.

Statistical Paradigms
---------------------

**Bayesian inference** works by updating the belief about the parameters 
:math:`\theta` encoded in the *prior distribution* with the information 
contained in the observed
data :math:`x` about the parameters as quantified in the *likelihood function*.
This updated belief -- called the *posterior distribution* -- 
can serve as the next "prior" for the subsequent collection
of additional data, and can itself be updated, and so on.
The updated belief is always encoded as a probability distribution,
so statements of belief about parameters are made using probability
statements. In contrast, **Classical** (or **Frequentist**) **statistics** 
instead focusses 
on characterizing uncertainty in parameter estimation procedures that 
results from random sampling variation. I.e., *Frequentist statistics*
never makes statements about *parameters*, but instead makes
statements about probabilities (long-run frequency rates) of
*estimation procedures*.  

Arguments for Bayesian Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Ease of Interpretation:**  
  making probability statements about parameters of interest 
  is much simpler than trying to perform *hypothesis testing*
  by $interpreting p-values* and 
  *confidence intervals* *(*to be discussed later).*

..

* **No "Large Sample" Requirements**:
  the accuracy of many Frequentist results rely upon asymptotic distributional
  results that require a "large sample size" -- the actual quantity 
  of which often remains unclear -- whereas Bayesian analysis 
  is a fully coherent probabilistic framework regardless of sample size.

..

* **Integrated Probabilistic Framework:**
  Bayesian analysis provides a hierarchical modeling framework that 
  definitionally characterizes and propagates all the
  modeled uncertainty into parameter estimation. 

..

* **Ability to Utilize Prior Information:** 
  the Bayesian framework naturally provides a way to 
  combine information, or *learn*; **however,
  the ability to input (potentially arbitrary) information
  into analysis via the prior means objectivity can be sacrificed for
  subjectivity.** 

..

* **Natural Framework for Regularization:**
  the prior distribution of a Bayesian specification can 
  be used to perform *regularization*, i.e., stabilize 
  model fitting procedures so that they are less prone to 
  overfitting data.

.. 

* **Complex Data Modeling:**
  Bayesian analysis provides -- via computational techniques -- 
  the ability to develop and use 
  more complicated modeling specifications than
  can be evaluated and use with classical statistical techniques;
  however, such approaches can be computationally demanding.  
  
  *In general, Bayesian computation is more expensive than Frequentist
  computation as there tends to be a lot of overhead. Also, complex
  models are not always preferable: (a) they require practitioners
  with more advanced skill sets, (b) they will be more difficult to implement 
  correctly, and (c) simple solutions can outperform complex solutions
  at a fraction of total development and computational costs*.

  *Occam's razor* says that the simplest answer is often correct one.
  And *Murphy's law* says that if something can go wrong, it will go wrong.
  These are very good considerations to keep in my as you contruct your 
  data analysis pipelines. 

 

.. note::

   **CLASS DISCUSSION**

   What do you appreciate most about the *Bayesian philosophy*?

   What do you appreciate about the *Frequentist philosophy*?

   

Are YOU a Bayesian?
-------------------

.. note::

   **CLASS DISCUSSION**

  * You're playing poker to win (like your life depends on it!), and the
    person you're bidding against just tipped his hand a little too low and
    you've seen his cards...

  * You're a skilled programmer, but bugs still slip into your code. After a 
    particularly difficult implementation of an algorithm, you decide to test 
    your code on a trivial example. It passes. You test the code on a harder 
    problem. It passes once again. And it passes the next, *even more difficult*, 
    test too! You are starting to believe that there may be no bugs in this code...

  * You're a doctor who has some previous experience with the symptoms that are 
    presenting for the current patient and you've diagnosed this sort of condition
    many times before...  



.. note::
     
   **Are YOU SURE you're a Bayesian?**

   Without looking...

   Write Bayes' theorem and describe the function of the different components 
   that comprise the theorem, particularly with respect to parameters and evidence.

   
Further study
------------------

If *you do* actually want to be a Bayesian -- fear not -- you can!
Programming in the Bayesian landscape has become incredibly easy
via the advent of *probabilistic programming*.
Here are several outstanding resources available 
that you can use to start learning more about Bayesian analysis: 

* `Entry level intro posted through kdnuggets <http://www.kdnuggets.com/2016/12/datascience-introduction-bayesian-inference.html>`_

* `Probabilistic Programming and Bayesian Methods for Hackers <https://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers>`_ by `Cameron Davidson-Pilon <https://github.com/CamDavidsonPilon>`_

* `A repository introducing probabilistic programming in Python <https://github.com/GalvanizeOpenSource/probabilistic-programming-intro>`_



