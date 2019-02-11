##############################################################################
# TITLE:  Actiavation Functions
# DESCRIPTION:  "Which Activation Function Should I Use?" by Siraj Raval
#               https://youtu.be/-7scQpJT7uo
# AUTHOR:  Kenny Haynie
##############################################################################

import numpy as np

def sigmoid(x,derivative=False):
    # (5:01)
    # Problems:
    # - Gradients vanish
    # - Output isn't zero-centered
    if (derivative==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

def tanh(x,derivative=False):
    # (6:25)
    # Problems:
    # - Gradients vanish
    if (derivative==True):
        return (1-(x**2))
    return np.tanh(x)

def relu(x,derivative=False):
    # (6:41)
    if (derivate==True):
        for i in range(0,len(x)):
            for k in range(len(x[i])):
                if x[i][k]>0:
                    x[i][k]=1
                else:
                    x[i][k]=0
        return x
    for i in range(0,len(x)):
        for k in range(len(x[i])):
            if x[i][k]>0:
                x[i][k]=1
            else:
                x[i][k]=0
    return x
