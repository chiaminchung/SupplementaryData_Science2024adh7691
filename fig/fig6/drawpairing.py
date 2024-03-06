import numpy as np
import sys
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
sys.path.append('../../py')
import plotsetting2 as ps

def internalerr(x,y):
    n = len(x)
    sx = sum(x)
    sy = sum(y)
    sxx = np.dot(x,x)
    syy = np.dot(y,y)
    sxy = np.dot(x,y)
    beta = (n*sxy - sx*sy)/(n*sxx-sx*sx)
    alpha = sy/n - sx/n*beta
    sigma = (n*syy-sy**2-beta**2*(n*sxx-sx**2))/(n**2-2*n)
    betaerr = (n*sigma / (n*sxx - sx**2))**0.5
    alphaerr = betaerr*(sxx**0.5)/(n**0.5)
    return beta,betaerr,alpha,alphaerr

def outererr(x,y,err):
    beta2 = []
    alpha2 = []
    guass = lambda x,y: np.random.normal(x,y)
    n = len(x)
    sx = sum(x)
    sxx = np.dot(x,x)
    sample = 100
    for i in range(sample):
        newy = list(map(guass,y,err))
        sy = sum(newy)
        syy = np.dot(newy,newy)
        sxy = np.dot(x,newy)
        beta2.append( (n*sxy - sx*sy)/(n*sxx-sx*sx))
        alpha2.append( sy/n - sx/n*beta2[-1] )
    return np.std(beta2),np.std(alpha2)

def draw(xx,yy,err,haveerr):
    [beta,betaerr,alpha,alphaerr] = internalerr(xx,yy)
    if haveerr: [betaerr2,alphaerr2] = outererr(xx,yy,err)
    else: betaerr2,alphaerr2 = 0,0
    alphaerr = (alphaerr**2+alphaerr2**2)**0.5
    betaerr  = (betaerr**2+betaerr2**2)**0.5
    return [alpha,alphaerr,beta,betaerr]


def drawdata(ax,xx,yy,err,c,index,word,shift):
    [alpha,alphaerr,beta,betaerr] = draw(xx,yy,err,True)
    ax.errorbar(xx,yy,err,color=c,marker='o',elinewidth=2,capsize=2.4,linewidth=0.8,ms=6,ls='None',mfc='w',mew=2)
    xxx = [0,0.22]
    ax.plot(np.array(xxx)+shift,np.array(xxx)*beta+alpha,color=c,linestyle='-')
    ax.errorbar(shift,alpha,alphaerr,color=c,capsize=2.6,marker='o',markersize=6,mew=2,label=word,ls='None')


def plot (ax):
    xi = 2*(2**0.5)
    width = 0.5
    msize = 2


    data1 = np.loadtxt("left_0.33_-0.2.dat")
    data2 = np.loadtxt("left_0.125_-0.2.dat")
    data3 = np.loadtxt("left_0.125_0.2.dat")


    dh = 0.000

    drawdata(ax,1.0/data2[:,0],data2[:,1],data2[:,2],'k',1,"h doped, $\delta=1/8$",0)
    drawdata(ax,1.0/data1[:,0],data1[:,1],data1[:,2],'dodgerblue',0,"h doped, $\delta=1/3$",dh)
    drawdata(ax,1.0/data3[:,0],data3[:,1],data3[:,2],'r',2,"e doped, $\delta=1/8$",-dh)

    ax.errorbar(0.25,7.481999999999999935e-03,2.498509075428784199e-03,color='k',marker='o',markersize=6,capsize=2,mew=2,mfc='w')
    ax.errorbar(0.25-dh,5.101428571428571861e-03,1.001832852234344753e-03,color='r',marker='o',markersize=6,capsize=2,mew=2,mfc='w')

    ax.set_xlim(xmin=-0.01)
    ax.set_ylim(ymin=0)

    xlabels= ["","","$1/8$","$1/6$","$1/4$"]
    xticks = [1.0/16,1.0/12,1.0/8,1.0/6,1.0/4]
    ps.text (ax, 0.24, -0.11, '$1/16$', fontsize=14)
    ps.text (ax, 0.37, -0.11, '$1/12$', fontsize=14)

    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels)

    ax.tick_params(axis='both', which='major', labelsize=14)
    ax.set_xlabel(r"$1/L_y$",fontsize=16)
    ax.set_ylabel(r"$\Delta_d$",fontsize=16)


