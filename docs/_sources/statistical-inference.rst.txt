.. stats-shortcourse

Statistical Inference
===============================

Statistics looks at some data, and asks the following questions:

* **Hypothesis Testing**: how well does the data match some assumed (null) distribution?

* **Point Estimation**: if not well, what instance of some distributional class does it match well?

* **Uncertainty Estimation**: are there reasonable competitors to that best guess distribution?

* **Distribution Estimation**: how heavily do our results relying on distributional assumptions?

These questions are addressed through various statistical/computational
methodologies:

  * Least squares
  * Numerical optimization
  * maximum likelihood
  * Numerical optimization
  * Expectation maximization (EM)
  * Monte Carlo methods
  * Variational methods
  * Simulation of null distribution (bootstrap, permutation)
  * Estimation of posterior density (Monte Carlo integration, MCMC, EM)



Is my coin fair?
----------------

**Simulating Data**
    
.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   import scipy.stats as st

   n = 100
   pcoin = 0.62 # actual value of p for coin
   results = st.bernoulli(pcoin).rvs(n)
   h = sum(results)
   print("We observed %s heads out of %s"%(h,n))

   We observed 67 heads out of 100

**Null Hypothesis**

.. code-block:: python

   p = 0.5
   rv = st.binom(n,p)
   mu = rv.mean()
   sd = rv.std()
   print("The expected distribution for a fair coin is mu=%s, sd=%s"%(mu,sd))

   The expected distribution for a fair coin is mu=50.0, sd=5.0

Hypothesis testing
^^^^^^^^^^^^^^^^^^

1. Identify target question ("Is this coin fair?")
2. Specify the *null hypothesis* ("The chance of heads is 50%") 
3. Choose *test statistic* ("The number of heads observed")
4. Collect data ("Flip the coin a few times")
5. Calculate the test statistics ("Count the total heads flipped")
6. *Reject* the null hypothesis if the test statistic looks "strange"
   compared to its *sampling distribution* under the null hypothesis;
   otherwise, *fail to reject* the null hypothesis

**Binomial Test**

.. code-block:: python

   print("binomial test p-value: %s"%st.binom_test(h, n, p))

   binomial test p-value: 0.000873719836912
   

**Z-Test** (with continuity correction)

.. code-block:: python

   z = (h-0.5-mu)/sd
   print("normal approximation p-value: - %s"%(2*(1 - st.norm.cdf(z))))

   normal approximation p-value: 0.000966848284768

**Simulation**

.. code-block:: python

   nsamples = 100000
   xs = np.random.binomial(n, p, nsamples)
   print("simulation p-value - %s"%(2*np.sum(xs >= h)/(xs.size + 0.0)))

   simulation p-value - 0.00062

.. note::

   **EXERCISE**

   Does anyone know what a **p-value** is?

   * Hint: it is *not* the probability that the null hypothesis is false.
   * Hint: it is *not* the probability that the test wrongly rejected the null.


Maximum Likelihood Estimation (MLE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python


   bs_samples = np.random.choice(results, (nsamples, len(results)), replace=True)
   bs_ps = np.mean(bs_samples, axis=1)
   bs_ps.sort()

   print("Maximum likelihood %s"%(np.sum(results)/float(len(results))))
   print("Bootstrap CI: (%.4f, %.4f)" % (bs_ps[int(0.025*nsamples)], bs_ps[int(0.975*nsamples)]))

   Maximum likelihood 0.67
   Bootstrap CI: (0.5800, 0.7600)

Bayesian Estamition
^^^^^^^^^^^^^^^^^^^
   
The Bayesian approach directly estimates the posterior
distribution, from which all other point/interval statistics can be
estimated.
The calculations here have `analytic solutions
<https://en.wikipedia.org/wiki/Closed-form_expression>`_. For most
real life problems an appropriate model is generally 
a more statistically complex and makes use of advanced numerical simulation
methods. 
 
.. code-block:: python
		
   fig  = plt.figure()
   ax = fig.add_subplot(111)

   a, b = 10, 10
   prior = st.beta(a, b)
   post = st.beta(h+a, n-h+b)
   ci = post.interval(0.95)
   map_ =(h+a-1.0)/(n+a+b-2.0)

   xs = np.linspace(0, 1, 100)
   ax.plot(prior.pdf(xs), label='Prior')
   ax.plot(post.pdf(xs), label='Posterior')
   ax.axvline(mu, c='red', linestyle='dashed', alpha=0.4)
   ax.set_xlim([0, 100])
   ax.axhline(0.3, ci[0], ci[1], c='black', linewidth=2, label='95% CI');
   ax.axvline(n*map_, c='blue', linestyle='dashed', alpha=0.4)
   ax.legend()
   plt.savefig("coin-toss.png")
   
.. figure:: coin-toss.png
   :scale: 75%
   :align: center
   :alt: coin-toss
   :figclass: align-center

.. note::

   **EXERCISE**

   Use the Python code above to play around with the *prior specification* 
   a little bit.  Does it seem to influence the results of the analysis 
   (i.e., the resulting posterior distribution)? If so, how? How do you 
   feel about that?


.. note::

   **CLASS DISCUSSION**

   1. How were the Bernoulli and binomial distributions used here?
   2. Explain the underlying hypothesis and the tests used to investigate it.
   3. Can you interpret the p-values based on this level of 
      significance (assuming :math:`\alpha=0.05`)?
   4. Compare and contrast the Bayesian and Frequentist paradigms for estimation.
   5. Are there any other examples besides the coin-flip where you might apply 
      what you have learned here?
   
