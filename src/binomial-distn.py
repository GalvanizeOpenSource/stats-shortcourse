#!/usr/bin/env python 
"""
fit a binomial distribution with several parameterizations
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs

# declare variables
font_size = 11
font_name = 'sans-serif'
n = 10000
fig = plt.figure(figsize=(10, 6), dpi=300)
splot = 0

# looxp through parameterizations of the beta
for n, p in [(5, 0.25), (5, 0.5), (5, 0.75)]:
    splot += 1
    ax = fig.add_subplot(1, 3, splot)

    x = np.arange(scs.binom.ppf(0.01, n, p), scs.binom.ppf(.99, n, p)+1)
    ax.plot(x, scs.binom.pmf(x, n, p), 'bo', ms=8, label='pmf')
    ax.vlines(x, 0, scs.binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
    rv = scs.binom(n, p)

    ax.set_ylim((0, 1.0))
    ax.set_xlim((-0.5, 5.5))
    ax.set_title("n=%s,p=%s" % (n, p))
    ax.set_aspect(1./ax.get_data_ratio())

    for t in ax.get_xticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
    for t in ax.get_yticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)

plt.savefig("binomial.png", dpi=400)
plt.show()
