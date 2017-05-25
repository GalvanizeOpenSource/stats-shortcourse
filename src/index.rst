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

Within data science (and perhaps at its core) is the field of `Machine learning <https://en.wikipedia.org/wiki/Machine_learning>`_, which seeks to accomplish two objectives:

  * **Supervised learning** - learn a mapping from inputs :math:`x` to outputs :math:`y`
  * **Unsupervised learning** - given only :math:`x`, learn interesting patterns in :math:`x`
     
.. note::
       
   Machine learning is a type of artificial intelligence that equips a computer 
   to capture a specific instance of a general class of patterns, and then asks the 
   computer to determine (for some data) what the actual instance of the pattern is.

   This is different than explicitly hardcoding some identified relationship into a
   computer as though it was already known beforehand. 

   Machine learning makes extensive use of `linear algebra
   <https://en.wikipedia.org/wiki/Linear_algebra>`_---the branch of
   mathematics that works directly with matrices---in conjunction numerical optimization procedures
   in order to identify the patterns present in data.

   This is a process called "model fitting" which allows a model of generic patterns to be
   restricted to a specific example that looks as similar to the data as possible. Once a 
   machine has such a model representation of the data, then it has "learned" the pattern
   in the data and can use it as a part of other programatic instructions.


 

On machine learning and statistics
-------------------------------------

`What is the difference between statistics and machine learning? <https://www.quora.com/What-is-the-difference-between-statistics-and-machine-learning>`_

Statistics and Machine Learning represent distinct quantitative analysis methodology 
traditions that developed towards distinctive objectives that suited their idiosyncratic access to 
different (primarily in terms of computational) problem solving methodologies and philosophies; 
however, both disciplines are rooted in the common enterprise of "data analysis" and so have 
found common ground on which to reconcile and merge methodologies, leading to the 
current situation in which the line between the two is increasingly blurry. Nonetheless, some
general statements related to the traditional domains claimed by each discipline can be made:


**Statistics**

  * confidence intervals, hypothesis tests, and optimal estimators  
  * characterization of uncertainty in estimation is paramount  
  * results are based on distribution theory and asymptotics  

**Machine Learning**

  * nonparametric and complex models harnessed via regularization  
  * "out of sample" performance (i.e., generalizability) is paramount  
  * results leverage empirical and computationally intensive techniques   

 
What kind of quantitative methodologies are out there?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
  * `Descriptive statistics <https://en.wikipedia.org/wiki/Descriptive_statistics>`_ - mean, median, skewness etc.
  * `Inferential statistics <https://en.wikipedia.org/wiki/Statistical_inference>`_  - hypothesis testing, interval estimation
  * `Predictive analytics <https://en.wikipedia.org/wiki/Predictive_analytics>`_ - supervised learning: regression, classification
  * `Prescriptive analytics <https://en.wikipedia.org/wiki/Prescriptive_analytics>`_ - unsupervised learning and recommenders

But of course, specific applications are rarely restricted to just one of these domains---these tools are highly synergistically informative and are best leveraged in cohort.

    
Course contents
-----------------

Objectives
^^^^^^^^^^^^^^^

These materials dig into the basics, introducing the areas of
probability and statistics that are assessed in the statistics and machine learning
interview step of the Galvanize Data Science Immersive admission
process. In addition to the content here, we provide a listing of 
resources for further study that review and reinforce these topics. 
Mastery of all this material is crucial for forming a strong foundation for statistics, 
machine learning, data science, or any other analytical and data-oriented discipline. 
And if you are interested in pursuing data science through the 
`Galvanize Data Science Immersive <https://www.galvanize.com/pick-a-locatoin?page=%2Fdata-science>`_, 
mastery of all this material will help make your Galvanize admission process -- rather than impossible -- a breeze.

We'll begin the first day with a gentle introduction to "counting" and probability problems.
Then we'll continue with an exploration into the (discrete and continuous) distributions most
commonly encountered in statistics. Finally, we'll finish with a concept-driven explanation of 
the frequentist and Bayesian paradigms (or philosophies) on which today's modern statistical analyses are based. 


On the second day we'll dive a bit further into how to make use of
probability distributions for inference and hypothesis testing. Then
we'll introduce regression and classification and explore these 
methodologies a little deeper through some example applications.
And finally we'll conclude by discussing some of the commonly 
used methods for evaluating how useful a model actually is. 
After that, if you want to stay around to hear a little bit more about the 
Data Science Immersive, you're welcome to -- but you don't have to.

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
  * `Khan Academy - statistics and probability <https://www.khanacademy.org/math/statistics-probability>`_
  * `15 hours of machine learning videos <http://www.dataschool.io/15-hours-of-expert-machine-learning-videos>`_
  
Reference materials
^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   helpful-math	      
   references

To view/download the source of these materials visit the GitHub repository.

   * `<https://github.com/GalvanizeOpenSource/stats-shortcourse>`_
