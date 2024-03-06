import numpy as np
import matplotlib.pyplot as plt

sample = 1000
# calculate the value and err of x and dx at target
def calculate(x,y,err,power,targetx):
    if power<1: print("ERROR! the power must not be smaller than 1")
    n = len(x)
    if n<=power: print("ERROR! the number of points is not enough for fitting")

    x = np.array(x) - targetx
    X = np.array([[pow(x[i],power-j) for j in range(power+1)] for i in range(n)])
    tempX = np.linalg.inv(np.dot(X.transpose(),X))
    poly = np.dot(tempX , X.transpose())
    poly = np.dot(poly,y)

    fitvalue = poly[-1]
    fitder = poly[-2]
    if power>1:
        fitqua = poly[-3]


    if n>power+1:    var = sum([ (y[i]-np.polyval(poly,x[i]))**2  for i in range(n) ])*1.0/(n-power-1)
    else: var = 0
    internalerr = (var * tempX[-1,-1])**0.5
    internaldererr = (var * tempX[-2,-2])**0.5

    # calculate the extra error
    acty = [0 for i in range(n)]
    externalvalue = []
    externalder = []
    for r in range(sample):
        for i in range(n):
            acty[i] = np.random.normal(y[i],err[i])
        newpoly = np.polyfit(x, acty, power)
        externalvalue.append(newpoly[-1])
        externalder.append(newpoly[-2])
    externalerr = np.std(externalvalue)
    externaldererr = np.std(externalder)

    fiterr = (internalerr**2 + externalerr**2)**0.5
    fitdererr = (internaldererr**2 + externaldererr**2) ** 0.5
    return [poly[::-1],fiterr]


def getdata(ax,data,text,index,c,shift,power):
    shift = 0
    if power==1:  cut = 6
    else:  cut = 10
    plt.errorbar(data[:,0]+shift,data[:,1],data[:,2],color=c,linestyle=':',capsize=2.4,marker='o',markersize=6,elinewidth=2,mew=1.5)
    popt,perr = calculate(data[:,0][:cut],data[:,1][:cut],data[:,2][:cut],power,0)

    if power==1:
        x = np.arange(0,0.048,0.001)
        y = popt[-1]*x + popt[-2]
        extra = str(round(popt[-2],4))
        err = str(round(perr,4))
    elif power==2:
        x = np.arange(0,0.071,0.001)
        y = popt[-1]*x*x + popt[-2]*x + popt[-3]
        extra = str(round(popt[-3],4))
        err = str(round(perr,4))
    plt.errorbar(shift,float(extra),float(err),color=c,capsize=2.4,marker='*',mfc='w',markersize=14,mew=1.5)
    plt.plot(x+shift,y,linestyle='-',color=c, linewidth=1.5)

def plot (ax):
    xi = 2*(2**0.5)

    data1 = np.loadtxt("right_0.125_0.2.dat")
    data4 = np.loadtxt("right_0.125_-0.2.dat")
    data5 = np.loadtxt("right_0.33_-0.2.dat")

    getdata(ax,data4,"tp=-0.2, doping=0.125",3,'k',0,1)
    getdata(ax,data1,"tp=0.2, doping=0.125",0,'r',0.0005,1)
    getdata(ax,data5,"tp=-0.2, doping=0.333",4,'dodgerblue',-0.0005,2)

    ax.set_xlabel("$h_d$",fontsize=16)
    ax.set_ylabel("$\Delta_d$",fontsize=16)
    ax.set_xlim([-0.005,0.085])
    ax.set_ylim([0,0.063])
    ax.tick_params(axis='both', which='major', labelsize=14)
