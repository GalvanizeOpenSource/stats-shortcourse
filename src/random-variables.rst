.. probability lecture

Random Variables
==================================

Random variables formalize a mapping we have been implicitly using already:

:math:`X(s) : S\Rightarrow \Re`

   * Capital letters refer to random variables.
   * Lowercase to refer to specific realization.
   * :math:`P(X=x) = P(\{s\in S : X(s) = x\})`
   * :math:`X \sim XYZ(\alpha, \beta, ...)` means X is distributed as, XYZ with parameters.
   * "i.i.d."

`Random variables (Khan academy) <https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/discrete-and-continuous-random-variables/v/random-variables>`_
     
PDFs and CDFs
-----------------------------

* **Probability density function (PDF)** -- a function of a continuous random variable, whose integral across an interval gives the probability that the value of the variable lies within the same interval. 
* **Probability mass function (PMF)** -- a function of a discrete variable that gives the probability that a discrete random variable is exactly equal to some value.
* **Cumulative distribution function (CDF)** -- defines the the probability that a continuous variable :math:`X` will take a value less than or equal to :math:`x`.
* **Cumulative mass function (CMF)** -- defines the the probability that a discrete variable :math:`X` will take a value less than or equal to :math:`x`.

What does that mean in code talk?  Take a look at how the following plot was created.
  
.. plot:: pdf-cdf-plot.py

Cumulative distribution function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:math:`F_X(x) = P(X < x)`

   * What kinds of bounds can we put on this function?
   * This works for both continuous and discrete functions.

Probability mass function, PMF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For discrete variables:

:math:`f_X(x) = P(X = x), \forall x`

For continuous variables, think of it as the derivative of the CDF:

:math:`f_X(x)dx = P(x < X < x+dx)`

:math:`f_X(x) = \frac{dF_X(x)}{dx}`

* `PDF (Khan academy) <https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/discrete-and-continuous-random-variables/v/probability-density-functions>`_
 	      	    
Expectation
------------------

   Discrete:
      :math:`E[X] = \sum_{s\in S} X(s) f_X(s)`

   Continuous:
      :math:`E[X] = \int_{-\infty}^{\infty}X(s) f_X(s)ds`

   A measure, but not the only one, of the central tendecy of a distribution. Alternatives?

      Note, the sample mean is:

      :math:`\bar{x} = \frac{1}{n}\sum_j^n x_j`

* `Expectation (Khan academy) <https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/expected-value-lib/v/term-life-insurance-and-death-probability>`_
	    
Variance
------------

:math:`Var[x] = E[(x - E[X])^2]`

Note, the sample variance is:

:math:`s^2 = \frac{1}{n-1} \sum_j^n (x_j - \bar{x})^2`

Standard deviation
^^^^^^^^^^^^^^^^^^^

:math:`\sigma(x) = \sqrt{Var[x]}`

Useful because its units are in units of our original RV.

* `Measures of spread (Khan academy) <https://www.khanacademy.org/math/probability/data-distributions-a1/summarizing-spread-distributions/v/range-variance-and-standard-deviation-as-measures-of-dispersion>`_

Covariance
^^^^^^^^^^^^^^^
We can also compute the covariance between two different variables:

:math:`Cov[X,Y] = E[(x - E[X])(y - E[Y])]`

Which is related to the

Correlation
^^^^^^^^^^^^^^

:math:`Corr[X,Y] = \frac{E[(x - E[X])(y - E[Y])]}{\sigma(X)\sigma(Y)} = \frac{Cov[X,Y]}{\sigma(X)\sigma(Y)}`

Correlation
-----------------   

A **spurious relationship** is a relationship where two or more events, that are not causally related to each other have a relationship.  This may be due to a "common response variable" or a "confounding factor".

Correlation coefficients vary between -1 and +1 with 0 implying no correlation.
			      
Pearson
^^^^^^^^^^^^^^^
>>> from scipy.stats import pearsonr
>>> pearsonr([1,2,3,4,5],[5,6,7,8,7])
(0.83205029433784372, 0.080509573298498519)

The Pearson correlation coefficient measures the linear relationship
between two datasets.  The p-value roughly indicates the probability
of an uncorrelated system producing datasets that have a Pearson
correlation at least as extreme as the one computed from these dataset.

In other words null hypothesis is that two sets of data are uncorrelated.

Spearman
^^^^^^^^^^^^^^^^

>>> from scipy.stats import spearmanr
>>> spearmanr([1,2,3,4,5],[5,6,7,8,7])
(0.82078268166812329, 0.088587005313543812)

The Spearman correlation is a nonparametric measure of the monotonicity of the relationship between two datasets. Unlike the Pearson correlation, the Spearman correlation does not assume that both datasets are normally distributed.

Marginal Distributions
--------------------------

Marginal distribution takes a--possibly not independent--multivariate distribution. And considers only a single dimension.

Accomplished by summing (discrete) or integrating (continuous).

.. math:: 

   f_X(x) = \int_{-\infty}^\infty f_{XY}(x,s) ds

.. figure:: MultivariateNormal.png
   :scale: 75%
   :align: center
   :alt: coin-toss
   :figclass: align-center

Further study
-----------------

A major goal of for the content on this page is not mastery.  You should be able to talk briefly about each of these concepts.  If you were to see a scatter plot of some data could you talk about it in terms of the concepts listed here?

Most major statistical textbooks will begin with an overview of these topics.

For example `Elements of Statistical Learning <https://statweb.stanford.edu/~tibs/ElemStatLearn/>`_ (Free)

Reading the opening chapters in these types of books will provide you with a perspective that is difficult to get across in a short lecture or on a single webpage.
