.. linear algebra, linear regression
   

Linear regression - part 1
=======================================

Objectives
^^^^^^^^^^^^^^

  1. State assumptions of linear regression model
  2. Estimate a linear regression model
   
  3. Evaluate a linear regression model
  4. Look at the R and Bayesian ways of implementing linear regression

     
Lets imagine there is some true model
 
   .. math::
      y = f(x) + \epsilon

We are trying to approximate :math:`f(x)` with another function :math:`\hat{f}(x)`     

Before we talk about the **how** lets just back up a second

Many ways to say the same thing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In machine learning we generally have a feature matrix :math:`X` (n samples by m features).  These features often come with pairings :math:`\mathcal{D}` that provide a mapping of each observation to a target vector :math:`y`.

+--------------------------+-----------------------------------------------+
| Machine-learning         | other fields                                  |
+==========================+===============================================+
| **Features** :math:`X`   | Covariates, independent variables, regressors |
+--------------------------+-----------------------------------------------+
| **Targets** :math:`y`    | dependent variable, regressand                |
+--------------------------+-----------------------------------------------+
| **Training**             | learning, estimation, model fitting           |
+--------------------------+-----------------------------------------------+

Two main types of machine learning models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Supervised learning**: models using labels paired with features

   * **Regression**: :math:`y` is continuous (price, demand, size)
   * **Classification**: :math:`y` is categorical or discrete (fraud, churn)

2. **Unsupervised learning**: pattern recognition, or discovery of patterns or labels using only :math:`X`

   * **Clustering**: hierarchical, k-means
   * **Dimension reduction**: PCA, SVD, NMF

Features
^^^^^^^^^^^^

Features may be:

1. **Continuous**:

   * price, quantity, sales, tenure
   * sometimes it makes since to map continuous variables into discrete ones 
     
2. **Categorical**:

   * Takes discrete levels
   * Also called a factor
   * Example: 1/0, Yes/No, Treated/Control, High/Medium/Low

3. Missing

   * May require estimation

4. May not look like a matrix
  
   * Text, audio, images, signals
   * May need to generate meaningful features

.. note:: sometimes our models is vastly improved by deriving new
          features from the ones we have (**feature engineering**)

Size of data
^^^^^^^^^^^^^^^^^

The size of your data plays a role in how you go about your analysis

* For associative studies:

   * May require large :math:`N` so that estimator is asymptotically normal
   * Power is a function of :math:`N` 
   * With large :math:`N` may be prone to overfitting depending on model and estimation method
   * Causality can be challenging

* For **predictive studies**
   * It can be difficult without large data sets:
   * What is large?
   * Must check model via **cross-validation**
   * Can run at scale
   * May need **regularization** (tomorrow)

There are probabilistic versions under both paradigms
     
Linear regression
------------------

With just one feature simple linear regression is as follows:

.. math::   

   Y = \beta_{0} + \beta_{1}\mathbf{X} + \epsilon

   * :math:`\beta_{0}` and :math:`\beta_{1}` are the unknown constants
   * :math:`\epsilon` is the error term and it is i.i.d. as well as :math:`\sim N(0,\sigma^{2})`  

So we train the model using :math:`\mathbf{X}=\mathbf{x}` to get:

.. math::   

   \hat{y} = \hat{\beta}_{0} + \hat{\beta}_{1}

     
.. math::   

   y_{i} = x_{i}^{T}\beta + \epsilon_{i} , \forall i


* Linear regression predicts the mean value (mean) of y , holding x fixed
* Model is linear in parameters :math:`\beta` but features may be non-linear
* functions of data, such as polynomials or splines
* Other models are possible, (quantile regression, stepwise regression, multilevel and more)
 
We can simulate data for linear regression with the following.

.. code-block:: python

   import numpy as np

   def get_simple_regression_samples(n,b0=-0.3,b1=0.5,error=0.2):
       trueX =  np.random.uniform(-1,1,n)
       trueT = b0 + (b1*trueX)
   
   return np.array([trueX]).T, trueT + np.random.normal(0,error,n)

.. plot:: linear-regression.py

Notation
^^^^^^^^^^

* :math:`y_{i}`:  dependent variable for observation :math:`i`
* :math:`x_{i}` : :math:`K \times 1` vector of covariates for observation :math:`i`
* :math:`\epsilon_{i}` : unobserved error for observation :math:`i`
* :math:`y` : :math:`N \times 1` vector of :math:`y_i`
* :math:`X` : :math:`N \times K` matrix of covariates, where there are :math:`k` covariates and each row is :math:`x_{i}^{T}`
* :math:`\epsilon`: :math:`N \times 1` vector of  :math:`\epsilon_{i}`
* :math:`\beta`: parameters (coefficients) to estimate

Assumptions
^^^^^^^^^^^^^^^^^


1. Linearity: :math:`y = x^{T} \beta + \epsilon`
2. **Full rank**: :math:`X` has full rank (rank = K)
3. **Exogeneity** of regressors: :math:`E[\epsilon|X] = 0`
4. Spherical errors, i.e., homoscedastic and not autocorrelated:

   * Var :math:`[\epsilon_{i}|X ] = σ 2 , \forall i`
   * Cov :math:`[\epsilon_{i}, \epsilon_{j}|X] = 0, \forall i \neq j`
   * Normally distributed errors: :math:`\epsilon|\mathbf{X} \sim N(0, \sigma^{2} I)`

     
.. note:: Many of these assumptions are relaxed especially Normality

An exogenous variable is determined outside the model.  If exogeneity fails, then:

   * Estimates for :math:`\beta` will be biased
   * Then :math:`x_{i}` is endogenous, i.e., determined inside the model
   * :math:`x_{i}` is correlated with  i

Homoscedastic errors mean the variance of the shock is constant:
   * Often fails in practice because variance of shock depends on covariates
   * Can correct by estimating a regression with ‘robust’ standard errors:

