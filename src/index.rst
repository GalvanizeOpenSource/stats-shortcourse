.. stats-shortcourse documentation master file, created by
   sphinx-quickstart on Tue Oct 11 15:24:00 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. figure:: galvanize-logo.png
   :scale: 35%
   :align: center
   :alt: galvanize-logo
   :figclass: align-center

   
Statistics short-course
======================================

Where are we going?
----------------------

Within data science and perhaps at its core is the field of `Machine learning <https://en.wikipedia.org/wiki/Machine_learning>`_.

  * **Supervised learning** - learn a mapping from inputs :math:`x` to outputs :math:`y` (given :math:`\mathcal{D}`)
  * **Unsupervised learning** - given only :math:`x` the goal is to find interesting patterns
     
.. note::
       
   Machine learning is a type of artificial intelligence that enables
   a machine to learn without programming it explicitly.

   Machine learning makes extensive use of `linear algebra
   <https://en.wikipedia.org/wiki/Linear_algebra>`_---The branch of
   mathematics that works directly with matrices

On machine learning and statistics
-------------------------------------

`What is the difference between statistics and machine learning? <https://www.quora.com/What-is-the-difference-between-statistics-and-machine-learning>`_

  * none really
  * statistics - confidence intervals, hypothesis tests and optimal estimators
  * machine learning - empirical and computational techniques
  * ML tends to have more nonparametrics, less asymptotics, more
    computationally intensive techniques, and more dimensionality
 
What kind of statistics are out there?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
  * `Descriptive statistics <https://en.wikipedia.org/wiki/Descriptive_statistics>`_ - mean, median, skewness etc.
  * `Inferential statistics <https://en.wikipedia.org/wiki/Statistical_inference>`_  - hypothesis testing
  * `Predictive analytics <https://en.wikipedia.org/wiki/Predictive_analytics>`_ - focused on prediction
  * `Prescriptive analytics <https://en.wikipedia.org/wiki/Prescriptive_analytics>`_ - i.e. recommenders

There are many examples of where these areas of statistics blend into one and other. 
    
Course contents
-----------------

Objectives
^^^^^^^^^^^^^^^

We will dig into the basics.  These materials survey the areas of
probability and statistics that will be covered in the statistics
interview. In addition to the overview there are resources for further
study that are meant to reinforce the most important topics.

We well begin in the first day with a gentle introduction to
probability and the major distributions used in statistics. We will
finish with a concept-driven explanation of frequentist and Bayesian
statistics.

On the second day we will dive a bit further into how to make use of
probability distributions for inference and hypothesis testing. We
will then introduce regression and classification through the use of
examples. Finally, we will discuss some of the commonly use methods of
evaluating model results.

Day 1
    
.. toctree::
   :maxdepth: 1

   getting-started
   probability-concepts
   combinatorics
   probability	      
   probability-distributions
      
Day 2
    
.. toctree::
   :maxdepth: 1

   paradigms	      
   statistics-concepts
   statistical-inference
   regression-classification-metrics
   concluding-remarks
	      
Resources for further study
-----------------------------

  * `Galvanize self study resources <https://github.com/zipfian/self-study-resources>`_
  * `Useful flashcards <http://www.cram.com/flashcards/probability-for-data-science-8215075>`_
  * `Khan Academy - statistics and srobability <https://www.khanacademy.org/math/statistics-probability>`_
  * `15 hours of machine learning videos <http://www.dataschool.io/15-hours-of-expert-machine-learning-videos>`_
  
Reference materials
^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   helpful-math	      
   references

To view/download the source of these materials visit the GitHub repository.

   * `<https://github.com/GalvanizeOpenSource/stats-shortcourse>`_
