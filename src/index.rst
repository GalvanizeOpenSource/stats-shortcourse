.. stats-shortcourse documentation master file

.. figure:: galvanize-logo.png
   :scale: 35%
   :align: center
   :alt: galvanize-logo
   :figclass: align-center

   
Statistics Short Course
=======================

Where are we going?
----------------------

Within data science (and perhaps at its core) is the field of `Machine learning <https://en.wikipedia.org/wiki/Machine_learning>`_, which seeks to accomplish two objectives:

  * **Supervised learning** - learn a mapping from inputs :math:`x` to outputs :math:`y`
  * **Unsupervised learning** - given only :math:`x`, learn interesting patterns in :math:`x`
     
These tasks are a form of artificial intelligence that endow a
computer with the capability to represent a general class of patterns.

Then through that representation they have the ability to **predict
outputs** and **identify patterns**.  Note that this is different than
explicitly hardcoding some data relationship into a computer as though
the specific relationship was already known beforehand.

.. container:: toggle

   .. container:: header

      **Show More**

   In order to identify which specific patterns (out of a general class
   of patterns) are present in the data, machine learning makes extensive use 
   of `linear algebra <https://en.wikipedia.org/wiki/Linear_algebra>`_---the 
   branch of mathematics that works directly with matrices---in conjunction numerical 
   optimization procedures.  

   This process of identifying a specific instance (out of a general class
   of patterns) that looks as similar to the data as possible
   is called "model fitting".  Once a machine has such a model representation of the data, 
   then it has *learned* the pattern in the data and can use it as a part of
   other programatic instructions designed to accomplish some objective. 

|
		  
.. note::

   Advanced linear algebra and computation topics are not a part of this
   short course, but by the end course you will be able to fit and utilize
   a prediction model using Python!


Machine Learning versus Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`What is the difference between statistics and machine learning? <https://www.quora.com/What-is-the-difference-between-statistics-and-machine-learning>`_

**Statistics** and **Machine Learning** represent distinct quantitative analysis 
traditions that developed towards distinctive objectives that 
suited their idiosyncratic access to (primarily computationally) different 
problem solving methodologies and philosophies; 
however, both disciplines are rooted in the common enterprise of 
"data analysis" and so have found common ground on which to reconcile and 
merge methodologies, leading to the current situation in which the line between 
the two has become increasingly blurred. Nonetheless, some general statements related to 
the traditional domains and expertise claimed by each discipline can be made:


**Statistics**

  * utilizes confidence intervals, hypothesis tests, and optimal estimators  
  * places paramount importance on characterizing uncertainty in estimation 
  * bases methodological development on distribution and asymptotic theory  

**Machine Learning**

  * utilizes nonparametric and complex models harnessed via regularization  
  * places paramount importance on "out of sample" generalizability/performance
  * bases methodological development on empirical and computational techniques 
    
Objectives
^^^^^^^^^^

The purpose of this short course is to (a) equip you with actual quantitative 
tools that you can apply to more effectively tackle problems you're 
interested in using data, and (b) to provide you with a appropriate foundation 
on which you can effectively build a synergistic data science skill set that
leverages
    
  * `Descriptive statistics <https://en.wikipedia.org/wiki/Descriptive_statistics>`_ - mean, median, skewness... 
  * `Inferential statistics <https://en.wikipedia.org/wiki/Statistical_inference>`_  - hypothesis testing, interval estimation...
  * `Predictive analytics <https://en.wikipedia.org/wiki/Predictive_analytics>`_ - supervised learning: regression, classification...
  * `Prescriptive analytics <https://en.wikipedia.org/wiki/Prescriptive_analytics>`_ - unsupervised learning, recommender systems...




 
Course Contents
---------------

The materials we cover dig into the basics, introducing the areas of
probability and statistics that are assessed in the statistics and machine learning
interview step of the Galvanize Data Science Immersive admission
process. In addition to the content here, we provide a listing of 
resources for further study that review and reinforce these topics. 
Mastery of all this material is crucial for forming a strong foundation 
for statistics, machine learning, data science, or any other analytical and 
data-oriented discipline. 
And if you are interested in pursuing data science through the 
`Galvanize Data Science Immersive <https://www.galvanize.com/pick-a-locatoin?page=%2Fdata-science>`_, 
mastery of all this material will help make your Galvanize admission process -- rather than a daunting scary prospect -- a breeze.

Day 1
^^^^^

    
.. toctree::
   :maxdepth: 1

   getting-started
   probability-concepts
   combinatorics
   probability	      
   probability-distributions
      
We'll begin the first day by introducing the modern open source data science 
ecosystem and tools to create your own cutting edge data science workspace. 
We'll then survey the fundamental concepts in probability and "counting". 
And finally we'll conclude the day with an exploration into the 
(discrete and continuous) distributions most commonly encountered in 
statistics. 

Day 2
^^^^^



.. toctree::
   :maxdepth: 1

   paradigms	      
   statistics-concepts
   statistical-inference
   regression-classification-metrics
   concluding-remarks


We'll kick off the second day a comparison of 
the frequentist and Bayesian paradigms (or philosophies) on which today's modern 
statistical analyses are based. Then we'll dive a bit deeper into 
probability distribution theory, followed by some hypothesis testing and inference examples. 
Then we'll introduce regression, classification, and some evaluation
metrics for these methodologies.
After that, if you want to stay around to hear a little bit more about the 
Data Science Immersive, you're welcome to -- but you don't have to.





	      
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
