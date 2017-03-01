.. bayes 1 (powerbayes)

Bayesian Inference
====================================================

Mini-bbjectives:

1. Discuss the philosophy
2. Review conditional probability
3. Bayes Rule
4. Discuss Bayesian inference

Bayes Theorem
----------------

   :math:`P(A|B) = \frac{P(B|A)P(A)}{P(B)}`    

   :math:`P(\theta|x) = \frac{P(x|\theta)P(\theta)}{P(x)}`    

The **posterior** is proportional to the **likelihood** times the **prior** distribution

Bayesian inference works by combining information about parameters :math:`\theta` contained in the observed data :math:`x` as quantified in the likelihood function :math:`p(x|\theta)`.  Classical statistics works by making inference about a single point, while Bayesian inference works on the whole distribution.  Parameters through the Bayesian lens are treated as random variables described by distributions.

  
The Philosophy of Bayesian Inference
	
You are a skilled programmer, but bugs still slip into your code. After a particularly difficult implementation of an algorithm, you decide to test your code on a trivial example. It passes. You test the code on a harder problem. It passes once again. And it passes the next, *even more difficult*, test too! You are starting to believe that there may be no bugs in this code...

But why?
^^^^^^^^^^

* **Numerical Tractability** - can make hard problems *easier*
* **Absence of Asymptotics** - What *really* is a large number?
* **Ease of Error Propagation** - Dealing in uncertainty
* **Formal framework for combining information** - prior
* **Intuitive appeal** - intrepretation is more intuitive
* **Coherence and intellectual beauty**

Then why isn't everyone a Bayesian?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Subjective** by nature
* **Amazing for complex models, but** are they necessary for simpler ones?
* **Accessablility** - Many of the books out there are difficult reads
* Requires a deeper understanding of your model
* Implementation tools


A tale of two philosophies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  
* **Frequentist** assumes that probability of an event is the long-run frequency of events
* **Bayesian** assigns a degree of belief to event

* Which one seems like a **better** choice for car accidents, predicting elections, predicting user behaivor, predicting test scores?
* `Breast cancer subtype and ethnicity? <http://www.ncbi.nlm.nih.gov/pubmed/26454611>`_
* Are we making conclusions about a population in nature or about an individual?
* Neither of these philosophies are better in all cases

   "All models are wrong, but some are useful" --George Box

Is the Bayesian paradigm more naturally aligned with the way we think?

* Flip a coin, but I saw how it was going to land
* Code has a bug or not---are you certain?
* A doctor has a **belief** about a diagnosis based on symptoms and experience

The pieces
############

* **prior** - :math:`P(\theta)` - one's beliefs about a quantity before presented with evidence 
* **posterior** - :math:`P(\theta|x)` - probability of the parameters given the evidence
* **likelihood** - :math:`P(x|\theta)`  - probability of the evidence given the parameters
* **normalizing constant** - :math:`P(x)`


Resources
-----------

Before I go any further I want to mention that many of these materials
come from a number of places and there is so much more to learn.

* `Probabilistic Programming and Bayesian Methods for Hackers <https://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers>`_ by `Cameron Davidson-Pilon <https://github.com/CamDavidsonPilon>`_

* `nice intro <http://www.kdnuggets.com/2016/12/datascience-introduction-bayesian-inference.html>`_
