
Python Installation Guide
===============================

The programming language Python has a number of packages associated
with it and we recommend installing the `Conda
<https://conda.io/docs/>`_ package management system to help maintain
your Python environment.


.. note:: these install instructions will install a Python3 default environment with a Python2 backup.


If there is an old version of anaconda you can remove it with

.. code-block::
   bash
		
   ~$ rm -rf ~/anaconda*
   
Download the image or install script from https://www.anaconda.com/download/

On Ubuntu
^^^^^^^^^^^^

1. install via the command line

.. code-block::
    bash
   
    ~$ bash ~/Downloads/Anaconda3-4.3.1-Linux-x86_64.sh

Answer yes to the path adding question
   
2. Restart terminal


On OSX
^^^^^^^^^^

1. Run the installer on the downloaded image

Answer yes to the path adding question

2. restart terminal


On Windows
^^^^^^^^^^^^^^^^^^^

1. Ensure that you install the ``Anaconda installer for Windows`` for Python 3

2. Double-click the .exe file

3. Follow the instructions on the screen

If you are unsure about any setting, accept the defaults. You can change them later.
When installation is finished, from the Start menu, open the Anaconda Prompt.

https://conda.io/docs/user-guide/install/windows.html

   
Then run this to create a working python 2 environment
-----------------------------------------------------------

.. code-block::
    bash
		
    ~$ conda create -n py2 python=2 anaconda


To activate the python 2 environment

.. code-block::
    bash
		
    ~$ source activate py2

To toggle back to a Python3 environment

.. code-block::
    bash
   
    ~$ source deactivate py2

Then ensure you can run Jupyter with Py2
------------------------------------------

.. code-block:: bash
		
    ~$ source activate py2
    ~$ conda install notebook ipykernel
    ~$ ipython kernel install --user

   
Keeping conda up-to-date
------------------------------

.. code-block:: bash

    ~$ conda update conda
    ~$ conda update --all
