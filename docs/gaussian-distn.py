#!/usr/bin/env python 
"""
fit a bernoulli distribution with several parameterizations
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
for mu,sig in [(1,5),(0.0,1.0),(5,2)]:
    splot += 1
    ax = fig.add_subplot(1,3,splot)
    
    rv = scs.norm(loc=mu,scale=sig)
    r = scs.norm.rvs(size=1000,loc=mu,scale=sig)
    pdf_range = np.linspace(scs.norm.ppf(0.01),scs.norm.ppf(0.99), 100)

    ax.hist(r,bins=60,facecolor="#9999FF",alpha=0.7,normed=1,histtype='stepfilled')
    pdf_range = np.linspace(scs.norm.ppf(0.0001, mu, sig),scs.norm.ppf(0.9999, mu, sig), 100)
    ax.plot(pdf_range, rv.pdf(pdf_range),'#FF0099', lw=4, label='pdf')
    ax.set_xlim((-20,20))
    ax.set_ylim((0,0.5))
    ax.set_title("mu=%s, sigma=%s"%(mu,sig))
    ax.set_aspect(1./ax.get_data_ratio())

    for t in ax.get_xticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
    for t in ax.get_yticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
    
plt.show()
