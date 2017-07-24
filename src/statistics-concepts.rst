.. probability lecture

Statistics Concepts
===================

Statistics is the sister discipline to probability in mathematics. 
Statistics addresses the *inverse problem* 
of learning about probability distributions from data,
as opposed to the *forward problem* of generating data from probability
distributions. The term **statistic** is also a definition -- a 
*statistic* is a "mathematical calculation of some data".  Since 
inference on probability distribution parameters relies upon *statistics*,
the term **Statistics** is an appropriate name for the discipline. 

     
PDFs and CDFs
-------------

As we have seen, there are two types of probability distributions:

* **Discrete distributions** define positive probabilities for specific outcomes :math:`x` of a *discrete-valued* random variable :math:`X` that are defined using a **probability mass function (PMF)**, i.e.,

.. math::
       Pr(X=x)

..

* **Continuous distributions** on the other hand (perhaps unexpectedly and paradoxically) define :math:`Pr(X=x) = 0` for every potential outcome :math:`x` of a *continuous-valued* random variable :math:`X` but define positive probabilities for :math:`Pr(X=x \in E \subseteq \mathbb{R})` according to the area under the **probability density function (PDF)** :math:`\; f_X(X=x)` over the set :math:`E`, i.e., 

  .. math::
       Pr(X=x \in E) = \underset{E}{\int} f(X=x)\; dx

  so that a *PDF* defines outcome prevalence in a relative (rather than absolute, i.e. probability) manner. For example, if :math:`f(X=x_1) = 2f(X=x_2)` then in the long-run :math:`x_2` will occur *twice as frequently* as :math:`x_1`. For more explanation, see `this video about PDFs from Khan academy <https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/discrete-and-continuous-random-variables/v/probability-density-functions>`_.


.. note::

   **EXERCISE**

   Have a look at the documentation for the `probability distribution
   functionality in SciPy <https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html>`_,
   which shows how to work with probability distributions using Python.
   Specifically, it shows how to use Python to evaluate 
   *probability mass functions* and *probability density functions* --
   something we haven't done yet.  For example, here's how
   to evaluate the *density* of the  *gamma distribution* for a given 
   outcome:

   >>> from scipy import stats
   >>> gamma_rv = stats.gamma(a = 5, scale = 10)
   >>> gamma_rv.pdf(10)
   0.0015328310048810102
   >>> poisson_rv = stats.poisson(mu=20)

   Once you've gotten the hang of this for the gamma distribution,
   try to generate analogous values for a *Poisson* distribution.  
   If you're running into trouble, consider what method of a 
   `poisson_rv` object you should be calling. Once you've got that 
   working, what would you say is the biggest difference between 
   these values as associated with the gamma distribution 
   compared to the Poisson distribution?





Both *discrete* and *continuous* distributions 
satisfy the *axioms of probability*, e.g.,

  1. :math:`0 \leq Pr(X=x) \leq 1` and :math:`0 \leq \underset{E \subseteq \mathbb{R}}{\int} f(X=x)\; dx \leq 1`

  ..

  2. :math:`\sum_{x \in S_X} Pr(X_i=x) = 1` and :math:`\int_{-\infty}^{\infty} f(X_i=x) \; dx = 1`

and both can be represented as a
**cumulative distribution functions (CDF)** which is defined as 

.. math::
       F_X(X=x) = Pr(X=x\leq x_0)


.. plot:: pdf-cdf-plot.py


Notice that for *continuous distributions* 

.. math::
       F_X(X=x_0) = \underset{x<x_0}{\int} f(X=x)\; dx

which means that the derivative of the CDF is the the PDF

.. math::
      \frac{d F_X}{X} f(X) = F_X(X)


Expectation
-----------

The **expectation operator** for a random variable :math:`X` is defined as

* :math:`E[X] = \sum_{x\in S_X} s Pr(X=x)`

..

* :math:`E[X] = \int_{-\infty}^{\infty}X(s) f_X(s)ds`

for discrete and continuous distributions, respectively. 


Parameters
----------

Recall the *first through fourth distributional moments* mentioned previously.
The first moments is the **expectation** :math:`E[X]` or **mean** of the 
distribution and is a measures the central tendecy of the distribution. For more explanation, see `this video about random variables from Khan academy <https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/expected-value-lib/v/term-life-insurance-and-death-probability>`_.


.. note::
  
  **EXERCISE**

  The second (central) moment of a distribution -- the **variance** -- is
  a measure of spread of the distribution and is defined as  

  .. math::
  
	Var[X] = E\left[(X-E[X])^2\right]

  and the **standard deviation**, which is defined on the original units 
  of the random variable is defined as :math:`\sigma_X = \sqrt{Var[X]}`.

  How would you actually calculate the standard deviation 
  of a random variable with a given discrete distribution?

  For more information, see: `Measures of spread (Khan academy) <https://www.khanacademy.org/math/probability/data-distributions-a1/summarizing-spread-distributions/v/range-variance-and-standard-deviation-as-measures-of-dispersion>`_.


Joint Distributions
-------------------


The **joint distribution** of two or more random variables is 
defined by the distributional form of the *chain rule*, i.e., 
the joint distribution of 
a collection of random variables :math:`X_i, \; i = 1, \cdots, n` is
given as 

.. math::
   \displaystyle P\left(\underset{i=1}{\overset{n}{\cap}}X_i\right) = \prod_i^n P\left(X_i | \underset{i=1}{\overset{n}{\cap}} X_i\right)

where :math:`P` specifies either a PMF or a PDF.  Further, notice that
if the :math:`X_i` are *independent* of each other, then

.. math::
   \displaystyle P\left(\underset{i=1}{\overset{n}{\cap}}X_i\right) = \prod_i^n P\left(X_i\right)


Linear Association
------------------

Linear association is encoded in a joint distribution of two variables 
as **covariance** 

.. math::
     
   Cov[X,Y] &= E[(x - E[X])(y - E[Y])]
   
            &= \left[\underset{x,y \in S_X,S_Y}{\sum or\int}\right] (x - E[X])(y - E[Y])P(X=x,Y=y) \left[dxdy\right]
  

   
Much like with standard deviation, it can be helpful to be on a more natural
scale, so we often use **correlation** -- which varies from -1 to +1 with 0 --
rather than covariance -- which is measured on the product of the two variables 
unit -- to describe the strength of a linear relationship:

.. math::
   Corr[X,Y] = \frac{E[(x - E[X])(y - E[Y])]}{\sigma_X\sigma_Y} = \frac{Cov[X,Y]}{\sigma_X\sigma_Y}



Marginal Distributions
--------------------------

Recasting the *Law of Total Probability* in terms of random variables
:math:`X` and :math:`Y`, we have for

* **discrete distributions**

.. math::
   \displaystyle Pr(X=x) = \sum_{y \in S_Y} Pr(X=x, Y=y) = \sum_{y \in S_Y} Pr(X=x|Y=y) Pr(Y=y)

* **continuous distributions**

.. math::
   \displaystyle f(X=x) = \int_{y \in S_Y} f(X=x, Y=y) \;dy = \int_{y \in S_Y} f(X=x|Y=y) f(Y=y) \;dy


The distributions
:math:`Pr(X=x)` and :math:`f(X=x)` are called **marginal distributions**
of their respective **joint distributions**, :math:`Pr(X, Y)` and
:math:`f(X, Y)`, respectively. Thus, a **marginal distribution** of a 
(possibly not independent) *multivariate (joint) distribution* is just the 
distribution of a 
single dimension (random variable) of the multivariate (joint) random variable.
Marginal distributions allow us to unpack joint distributions. 



.. figure:: MultivariateNormal.png
   :scale: 75%
   :align: center
   :alt: coin-toss
   :figclass: align-center


.. note::
   
   **EXERCISE**

   Draw the above plot, labeling it with all the concepts we've covered so far.



Statistics
----------	    

**Statistics** often correspond to distributional *parameters* as they 
are typically used to estimate specific distributional parameters.  It's important 
to always remember the distinction between *statistics* and *parameters*,
however: 
statistics are numerical calculations that are planned to be executed using 
sample data, while parameters are mathematical manipulations carried out on 
distributional forms. 



The statistic that corresponds to expectation is the **sample mean**:

.. math::
   \bar{x} = \frac{1}{n}\sum_j^n x_j

Common alternative statistics for measuring centrality are the **sample median**
and the **sample mode**.
The statistic that corresponds to variance is the **sample variance**:

.. math::

   s^2 = \frac{1}{n-1} \sum_j^n (x_j - \bar{x})^2

There are a couple common choices for 
statistics that correspond to linear associations parameters.  
The **Pearson correlation** coefficient measures the linear relationship
between two datasets.  
The alternative **Spearman correlation** is a nonparametric measure of the 
monotonicity of the relationship between two datasets, which is just a fancy
way of saying that calculates the correlation on the *ranks* rather than
original values. Here's how you can calculate these statistics using Python:

>>> from scipy.stats import pearsonr
>>> from scipy.stats import spearmanr
>>> 
>>> pearsonr([1,2,3,4,5],[5,6,7,8,7])
(0.83205029433784372, 0.080509573298498519)
>>> spearmanr([1,2,3,4,5],[5,6,7,8,7])
(0.82078268166812329, 0.088587005313543812)

The first value in the above tuples is the correlation.
The second is a *p-value* of a statistical *test* 
of the *null hypothesis* of no association.  
The two tests are based on different distributional
assumptions and as such are, unsurprisingly, different. 
A **spurious relationship** is a relationship is said to exist between
two or more random variables that are not causally related to each other 
but have a relationship due to a common **confounding factor**.


**Confounding** is just one of the many difficulties that will need to be 
dealt with in real data. When you actually begin working with 
real data you'll see that things can be quite messy.  In fact, messy
would be an understatement for some **outliers** that will be present in 
your data.  These outliers can drastically affect your calculated statistics 
and hence your conclusions. Weary and vigilant attention is required to 
suss out these influential data points and decide what is to be done about 
them.  And what if you have **missing data** that's not even available to
look at? Will you impute the missing data? With how much sophistication?
Will you simply disregard samples with missing entires? As you can see,
there are many questions and, unfortunately, too few answers. 


.. note::
   
   **EXERCISE**

   List out some statistics you could calculate with the data in the 
   above plot that you drew.


Further study
-----------------

Most major statistical textbooks,
for example `Elements of Statistical Learning <https://statweb.stanford.edu/~tibs/ElemStatLearn/>`_ (Free), will begin with an overview of these topics.





