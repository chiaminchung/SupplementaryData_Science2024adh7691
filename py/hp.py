import numpy as np

def getdata_dmrg (fname):
    dat = np.loadtxt (fname, skiprows=1)
    angles = dat[:,0]
    pair = dat[:,1]
    perr = dat[:,2]
    n = dat[:,3]
    nerr = dat[:,4]
    E = dat[:,5]
    Eerr = dat[:,6]
    return angles, pair,perr, n,nerr, E,Eerr

def getdata_qmc (fname):
    dat = np.loadtxt (fname)
    angles = dat[:,0]
    v = dat[:,1]
    verr = dat[:,2]
    return angles, v, verr
