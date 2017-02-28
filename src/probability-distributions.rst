.. probability lecturexc

Probability distributions
=============================

`The SciPy docs for statistics <https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html>`_ is quite useful.

Properties of distributions
-----------------------------

Use these properties to characterize a distribution:

   * Expectation/mean
   * Variance/standard deviation
   * Skewness (asymmetry)
   * Kurtosis (fat tails)
   * Correlation

Rules for choosing a good distribution
-----------------------------------------

Main questions
^^^^^^^^^^^^^^^^

   * Are my data discrete or continuous?
   * Are my data symmetric?
   * What limits are there on possible values for my data?

Other questions to keep in mind
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^     
     
   * How likely are extreme values?
   * Are there missing values?
   
Bernoulli:
---------------

A Bernoulli distribution is a discrete probability distribution for a Bernoulli trial.  The distribution takes the value 1 with success probability of :math:`p` and the value 0 with failure.   Success could be heads on a coin flip.

PMF = :math:`P[success] = p` , :math:`P[failure] = 1-p`

Mean: :math:`E[x] = p`

Variance: :math:`Var(x) = p(1-p)`

:download:`bernoulli-distn.py`

Binomial:
------------

The Binomial distribution gives the discrete probability distribution of obtaining exactly `p` successes out of `n` trials

PMF: :math:`P[X=k] = {n \choose k}p^k(1-p)^{n-k}, \forall k \in \{0, 1,..., n\}`

Mean: :math:`np`

Var: :math:`np(1-p)`

.. plot:: binomial-distn.py

Geometric:
-------------

The probability of some number (`X`) of Bernoulli trials needed to get one success.  It also refers to probability of (`X-1`) failures before the first success. 

PMF: :math:`P[X=k] = p (1-p)^{k-1}, \forall k \in \{0, 1,...\}`

Mean: :math:`\frac{1}{p}`

Variance: :`\frac{1-p}{p^2}`


Hypergeometric
-----------------

Hypergeometric distribution is a discrete probability distribution
that describes the probability of `k` successes in `n` draws, without
replacement.

The hypergeometric test uses the hypergeometric distribution to
calculate the statistical significance of having drawn a specific k
successes n total draws

Think of an urn with two types of marbles, red ones and green ones. Define drawing a green marble as a success and drawing a red marble as a failure (analogous to the binomial distribution).

Did I draw the **expected** number of green marbles?

The data are not accurately modeled by the binomial distribution,
because the probability of success on each trial is not the same.

.. note:: Think Texas Hold em

Poisson
------------

If a mean of an event happening per unit time is observed and you need the probability of `n` events happening

PMF: :math:`P[X=k] = \frac{\lambda^k e^{-\lambda}}{k!},\forall k \in \{0,1,2,...\}`

Mean: :math:`\lambda`

Variance: :math:`\lambda`

:download:`poisson-distn.py`

Exponential
----------------

A good way to model the time between events for a poisson
process.  It is a particular case of the gamma distribution.
It is governed by a rate parameter :math:`\lambda`.

SUPPORT: :math:`x \in (0, \inf)`.

PDF: :math:`\lambda e^{-\lambda x}`

MEAN: :math:`\frac{1}{\lambda}`

VARIANCE: :math:`\frac{1}{\lambda^2}`

:download:`exponential-distn.py`

Uniform
------------

PDF: :math:`f(x) = \frac{1}{b-a}, \forall x\in[a, b]`,  0 otherwise

MEAN: :math:`\frac{a+b}{2}`

VARIANCE: :math:`\frac{(b-a)^2}{2}`


Normal aka Gaussian
-----------------------

The Gaussian is the most widely used distribution for continuous
variables. The distribution is governed by the mean :math:`\mu` and variance :`\sigma^2`.

SUPPORT :math:`x \in (-\inf, \inf)`

PDF: :math:`\frac{1}{\sqrt{2\pi\sigma^2}}exp(-\frac{(x - \mu)^2}{2\sigma^2})`

MEAN: :math:`\mu`

VARIANCE: :math:`\sigma^2`

The inverse of the variance is known as the **precision** (:math:`\tau = 1/\sigma^{2}`).

:download:`gaussian-distn.py`
	  
Distributions are related
----------------------------

There are many more distributions than the ones mentioned above.  Here is an illustration from *Casella and Berger* that does a pretty good job making that point.

	  
.. figure:: statistical-inference-distns.jpg
   :scale: 35%
   :align: center
   :alt: distns
   :figclass: align-center
