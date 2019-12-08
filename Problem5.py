from math import*
import numpy as np
import matplotlib.pyplot as pl


def x(n):
    return np.sin(3 * n * (pi) / 100);

def y(n):
    value = 0.5 * x(n+1) - 0.5 * x(n-1);
    value[0] = -1.5 * x(0) + 2 * x(1) - 0.5 * x(2);
    value[np.size(n)-1] = 1.5 * x(np.size(n)-1) - 2 * x(np.size(n)-2) + 0.5 * x(np.size(n)-3);
    return value;

def getY(xval):
    value = np.zeros(np.size(xval))
    for ctr in range (0,(np.size(xval))):
        if ctr == 0:
            value[ctr] = -1.5 * xval[ctr] + 2 * xval[ctr+1] - 0.5 * xval[ctr+2];
        elif ctr < np.size(xval) - 1:
            value[ctr] = 0.5 * xval[ctr+1] - 0.5 * xval[ctr-1];
        else:
            value[ctr] = 1.5 * xval[ctr] - 2 * xval[ctr-1] + 0.5 * xval[ctr-2];
    return value;

n = np.arange(0,200)
varX = x(n)
varY = y(n)
varZ = getY(varX);


pl.plot(varX, label="x(n)")
pl.plot(varY)
pl.plot(varZ,  label="y(n)")

pl.xlabel("n")
pl.ylabel("y(n)")
pl.legend(loc = "upper right")


