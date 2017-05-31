#!/usr/bin/env python 
"""
fit a exponential distribution with several parameterizations
"""

import sys,os
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs

## declare variables
font_size = 11
font_name = 'sans-serif'
n = 10000
fig = plt.figure(figsize=(10,6))
splot = 0

## loop through parameterizations of the beta
for lamb in [0.5,1.0,5.0]:
    splot += 1
    scale = 1./lamb
    
    rv = scs.expon(scale=scale)
    r = scs.expon.rvs(size=1000,scale=scale)
    pdf_range = np.linspace(scs.expon.ppf(0.0001),scs.expon.ppf(0.9999), 100)
    
    ax = fig.add_subplot(1,3,splot)
    ax.hist(r,bins=60,facecolor="#9999FF",alpha=0.7,normed=1,histtype='stepfilled')
    ax.plot(pdf_range, rv.pdf(pdf_range),'#FF0099', lw=5, label='pdf')
    ax.set_xlim((0,12))
    ax.set_ylim((0,1.0))
    ax.set_title("lambda=%s"%(lamb))
    ax.set_aspect(1./ax.get_data_ratio())

    for t in ax.get_xticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
    for t in ax.get_yticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
    
plt.show()
