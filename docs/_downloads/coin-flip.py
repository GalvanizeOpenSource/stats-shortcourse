#!/usr/bin/env python
"""
The standard coinflip example
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

n = 100
pcoin = 0.62 # actual value of p for coin
results = st.bernoulli(pcoin).rvs(n)
h = sum(results)
print results
print("we observed %s heads out of %s"%(h,n))

## Expected distribution for fair coin
p = 0.5
rv = st.binom(n, p)
mu = rv.mean()
sd = rv.std()
print("The expected distribution for a fair coin is mu=%s, sd=%s"%(mu,sd))

##### if we move into a hypothesis testing framework

## we can use the binomial test
print("binomial test - %s"%st.binom_test(h, n, p))

## normal approximation for binomal
z = (h-0.5-mu)/sd
print("normal approx for binomial - %s"%(2*(1 - st.norm.cdf(z))))

## we can also use simulation to get a p-value
nsamples = 100000
xs = np.random.binomial(n, p, nsamples)
print("simulation p-value - %s"%(2*np.sum(xs >= h)/(xs.size + 0.0)))

## MLE
print("Maximum likelihood %s"%(np.sum(results)/float(len(results))))
bs_samples = np.random.choice(results, (nsamples, len(results)), replace=True)
bs_ps = np.mean(bs_samples, axis=1)
bs_ps.sort()
print "Bootstrap CI: (%.4f, %.4f)" % (bs_ps[int(0.025*nsamples)], bs_ps[int(0.975*nsamples)])

## The Bayesian approach directly estimates the posterior distribution
## all other point/interval statistics can be estimated from posterior

fig  = plt.figure()
ax = fig.add_subplot(111)

a, b = 10, 10
prior = st.beta(a, b)
post = st.beta(h+a, n-h+b)
ci = post.interval(0.95)
map_ =(h+a-1.0)/(n+a+b-2.0)

xs = np.linspace(0, 1, 100)
ax.plot(prior.pdf(xs), label='Prior')
ax.plot(post.pdf(xs), label='Posterior')
ax.axvline(mu, c='red', linestyle='dashed', alpha=0.4)
ax.set_xlim([0, 100])
ax.axhline(0.3, ci[0], ci[1], c='black', linewidth=2, label='95% CI');
ax.axvline(n*map_, c='blue', linestyle='dashed', alpha=0.4)
ax.legend()
plt.savefig("coin-toss.png")
