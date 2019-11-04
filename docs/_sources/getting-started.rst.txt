.. stats-shortcourse 

Getting started
======================================

Where are we going?
----------------------

We mentioned **Machine Learning** on the workshop land page ---here's a figure that provides a little more perspective.
Note the emphasis on sample size "rules of thumb".  This is a characteristic of the 
empirical and computational nature of machine learning that enables the use of 
complex and sensitive models which subsequently require large amounts of data to actualize
meaningful (as opposed to spurious) model fits.  The figure also gives an indication of 
the vast and diverse set of tools and tasks that make up the machine learning world.
If you're interested in exploring this fascinating methodology space and learning 
how to leverage and apply these powerful tools (which, since you're here, you probably are), then
you're going to need a fundamental understanding and serviceable skill set in programming, 
probability and statistics. And if you're just starting your journey (congratulations!!) 
you're in the right place!

.. figure:: ./images/sklearn-map.png
   :scale: 35%
   :align: center
   :alt: galvanize-logo
   :figclass: align-center

`<http://scikit-learn.org/stable/tutorial/machine_learning_map>`_

Industry Leading Tools
----------------------

The above figure is part of `Scikit-Learn's <http://scikit-learn.org/>`_
extensive documentation and tutorial collection. Scikit-Learn is the leading open source
collection of machine learning tools. There are some competitors (notably R, which has
seen an increase in machine learning capabilities, but is still tailored more towards 
the more historical statistics and traditional data analysis communities), 
but it is safe to say that 
Scikit-Learn is the industry standard bearer. Scikit-Learn is a library in the python
programming language -- another industry standard in terms of programming languages -- 
which has seen widespread adoption and the establishment of an incredibly vast 
and diverse ecosystem. Python is, and has been for quite some 
time now, the hottest most generally useful program language around. If you're 
looking to build up your programming skill set, you cannot go wrong Python.  
One final industry leader is the Anaconda framework from Continuum Analytics. 
Anaconda is a platform that simplifies package management and deployment of open source 
data science capabilities.  Data Scientists Love Anaconda.


Installing Python
-------------------

Because (a) Python is the working language of the Data Science Immersive, and because (b) 
you'll need to have a installation of Python on your computer if you want to follow 
along with the examples in this work shop, we encourage you to install Anaconda 
(which comes with a working installation of Python out of the box).

`<https://docs.continuum.io/anaconda/install>`_

Installing an Editor
-----------------------

Data scientists need to be proficient at programming.  To do this there is a
`specific kind of editor <https://en.wikipedia.org/wiki/Source-code_editor>`_ that is commonly used.
There are many editors to choose from... Unless you have a programming editor that you are already comfortable with 
we recommend that you start with `VSCode <https://code.visualstudio.com/download>`_. 

Another alternative for a beginner level editor is Atom. 

* `<https://flight-manual.atom.io/getting-started/sections/installing-atom>`_

.. note:: Programming practices, editors, version control, software engineering, and other related topics are not part of the scope of this short course.

Installing Git (optional)
-----------------------------

On windows
^^^^^^^^^^^

   1. Download the `latest Git for Windows installer <https://git-for-windows.github.io>`_
   2. When you've successfully started the installer, you should see the Git Setup wizard screen

   .. important::

      To use Git from the command prompt you must check the box
   
   3. Open a Command Prompt (or Git Bash if that functionality was not enabled)

On OSX
^^^^^^^^^

   1. Install Brew (If it is not already installed) using `the instructions here <https://brew.sh/>`_
  
   2. Install git from the command line

      .. code-block:: bash
      
         ~$ brew install git

On Ubuntu
^^^^^^^^^^^

   .. code-block:: bash

      ~$ sudo apt install git


Keeping your materials up to date
-----------------------------------

If you have Git installed on your machine.  `cd` into the directory on your machine and

   .. code-block:: bash

      ~$ git pull

If you are not using Git:

   1. Copy the any downloaded materials you might have into a backup directory
   2. Download the zip file from the repository and uncompress it

At the end of the course you may wish to `fork` the repository to your personal GitHub.

A note on Jupyter
------------------------

Jupyter notebooks are a way to mix interactive Python with prose as expressed using Markdown. They are also both very powerful and an industry standard so practice with them is useful.

An in-depth understanding of Jupyter notebooks is not necessary for this course, but they are frequently used so it can be helpful to become familiar with the technology. Here are some resources to help you better understand this computing environment.

* http://jupyter.readthedocs.io/en/latest
* https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest


