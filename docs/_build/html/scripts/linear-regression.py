#!/usr/bin/env python
"""
linear regression example

"""

from __future__ import division
import os,sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from mylib import *

import logging
_logger = logging.getLogger("theano.gof.compilelock")
_logger.setLevel(logging.ERROR)

if not os.path.isdir("traces"):
    os.mkdir("traces")

seed = 42
n = 20
b0_true = -0.3
b1_true = 0.5
x,y = get_simple_regression_samples(n,b0=b0_true,b1=b1_true,seed=seed)

print(x)
print(y)


## plot the model
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.plot(x[:,0],y,'ko')
#ax.plot(x[:,0],y_pred_lstsq,color='black',label='least squares')
ax.plot(x[:,0], b0_true + x[:,0]*b1_true,color='black',label='model mean')
ax.legend()
plt.show()


## make a least squares fit    
coefs_lstsq = fit_linear_lstsq(x,y)
y_pred_lstsq = coefs_lstsq[0] + (coefs_lstsq[1]*x[:,0])


## print summary
print("\n-----------------------")
print("truth: b0=%s,b1=%s"%(b0_true,b1_true))
print("lstsq fit: b0=%s,b1=%s"%(round(coefs_lstsq[0],3),round(coefs_lstsq[1],3)))
