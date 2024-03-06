import matplotlib.pyplot as plt
import plotsetting2 as ps
import plotlatt as hsz
import numpy as np

def plot_hszx (dat, ax, **args):
    datx = np.mean (dat, axis=1)
    xs = range(1,len(datx)+1)
    p, = ax.plot (xs, datx, **args)
    return p

def errorbar_hszx (dat, err, ax, **args):
    datx = np.mean (dat, axis=1)
    errx = np.mean (err, axis=1)
    xs = range(1,len(datx)+1)
    p = ax.errorbar (xs, datx, errx, **args)
    return p

def plot_hszlatt (hdat, szdat):
    lx,ly = np.shape (hdat)
    f,ax = hsz.gen_figure (lx, ly, marginy=4)
    hsz.plot_square_latt (ax, lx, ly)
    xs, ys = hsz.get_xys (lx, ly)
    hsz.plot_hsz (ax, xs, ys, hs, szs, AFDomain=True)
    return f, ax
