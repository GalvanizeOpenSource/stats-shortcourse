import csv
import numpy as np
import scipy
import scipy.stats as stats

def get_simple_regression_samples(n,b0=-0.3,b1=0.5,error=0.2,seed=None):
    if seed:
        np.random.seed(seed)

    trueX =  np.random.uniform(-1,1,n)
    trueT = b0 + (b1*trueX)
    return np.array([trueX]).T, trueT + np.random.normal(0,error,n)

def fit_linear_lstsq(xdata,ydata):
    """
    y = b0 + b1*x
    """
    
    matrix = []
    n,d = xdata.shape

    for i in range(n):
        matrix.append([1.0, xdata[i,0]]) 

    coeffs = scipy.linalg.basic.lstsq(matrix,ydata)[0]
    #yFit =coeffs[0] + (coeffs[1] * xdata)

    return coeffs

def get_rsme(targets,predictions):
    """return the root mean sq error"""
    if targets.shape[0] != predictions.shape[0] or targets.shape[1] != predictions.shape[1]:
        raise Exception("bad dims")

    return(np.linalg.norm(predictions - targets) / np.sqrt(n))

if __name__ == "__main__":

    ## simple linear regression
    n = 12
    x,y = get_simple_regression_samples(n,seed=42)
    print('x = %s'%[round(_x,2) for _x in x])
    print('y = %s'%[round(_y,2) for _y in y])

    y_pred, coeffs = fit_linear_lstsq(x,y)

    print(coeffs)
    
    #slope, intercept, r_value, p_value, std_err = stats.linregress(t,t_predict)
    #print intercept,slope
