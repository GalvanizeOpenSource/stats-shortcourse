from pprint import pprint
import numpy as np


## the data
row_names = np.array(["A2M", "FOS", "BRCA2","CPOX"])
column_names = np.array(["4h","12h","24h","48h"])
values0  = np.array([[0.12,0.08,0.06,0.02]])
values1  = np.array([[0.01,0.07,0.11,0.09]])
values2  = np.array([[0.03,0.04,0.04,0.02]])
values3  = np.array([[0.05,0.09,0.11,0.14]])

#############################################
## create an array for the data
#############################################
print("\nQuestion 1")
X = np.vstack([values0,values1,values2,values3])
print(X)
print(X.shape)

#############################################
## find the mean expression value per gene
#############################################
print("\nQuestion 2")
gene_means = X.mean(axis=1)
print("Gene means check: ", X[0,:].mean()==gene_means[0])
print(["%s = %s"%(gene,gene_means[g]) for g, gene in enumerate(row_names)])

#############################################
## find the mean expression per time point
#############################################
print("\nQuestion 3")
time_means = X.mean(axis=0)
print("Time means check: ", X[:,0].mean()==time_means[0])
print(["%s = %s"%(tp,time_means[t]) for t, tp in enumerate(column_names)])

########################################################
## which gene has the maximum mean expression value?
########################################################

print("\nQuestion 4")
gene_means = X.mean(axis=1)
gene_mean_ind = np.argmax(gene_means)
print("gene with max mean expression value: %s (%s)"%(row_names[gene_mean_ind],gene_means[gene_mean_ind]))

########################################################
## sort the gene names by the max expression value
########################################################

gene_names = row_names
print("sorted gene names: %s"%(gene_names[np.argsort(np.max(X,axis=1))]))
