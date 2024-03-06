import numpy as np
import matplotlib.pyplot as plt
import linear
import sys 

plt.figure(figsize=(4,4))
plt.subplots_adjust(left=0.17,bottom=0.12,right=0.97,top=0.97)


plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.linewidth"] = 0.6
plt.rcParams["xtick.major.width"] = 1.6
plt.rcParams["xtick.direction"] = 'out'
plt.rcParams["ytick.major.width"] = 1.6
plt.rcParams["ytick.direction"] = 'in'

lx = 20
maxy = 0.038


plt.text(0.003,0.91*maxy,"(c)",fontsize=16)

clist = ['r','orange','y','g','c','olive','b','darkgreen','m','grey','k']

xi = 2*(2**0.5)
width = 1.0
sample = 10000


tdltabc = np.loadtxt("tdltabc.dat")

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
    print(poly)


    fitvalue = poly[-1]
    fitder = poly[-2]
    if power>1:
        fitqua = poly[-3]


    if n>power+1:    var = sum([ (y[i]-np.polyval(poly,x[i]))**2  for i in range(n) ])*1.0/(n-power-1)
    else: var = 0
    internalerr = (var * tempX[-1,-1])**0.5
    internaldererr = (var * tempX[-2,-2])**0.5
    print(fitvalue,fitder)

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

    print(internalerr,externalerr)
    fiterr = (internalerr**2 + externalerr**2)**0.5
    fitdererr = (internaldererr**2 + externaldererr**2) ** 0.5
    print(fiterr, fitdererr)
    print("----")
    return [poly[::-1],fiterr]








for i in range(len(tdltabc)):
    plt.errorbar(tdltabc[i,0],tdltabc[i,1],tdltabc[i,2],color=clist[i],linestyle='-',linewidth=width,capsize=2.4,marker='o')


popt,perr = calculate(tdltabc[:,0],tdltabc[:,1],tdltabc[:,2],2,0)

print("qua result: ",popt[-3],perr)

x = np.arange(0,0.15,0.01)
y =  popt[-1]*x*x + popt[-2]*x + popt[-3]

chi_square = []

for i in range(len(tdltabc)):
    h = tdltabc[i,0]
    value = tdltabc[i,1]
    chi = ( ( popt[-1]*h*h + popt[-2]*h + popt[-3] - value ) / tdltabc[i,2] ) **2
    chi_square.append(chi)
    
print("chi_square is: ", sum(chi_square))



plt.plot(x,y,linestyle='-',color='grey',label='quadratic fit',linewidth=0.6)


points = 7 
popt,perr = calculate(tdltabc[:,0][:points],tdltabc[:,1][:points],tdltabc[:,2][:points],1,0)

x = np.arange(0,0.15,0.01)
y =   popt[-1]*x + popt[-2]






plt.plot(x,y,linestyle='--',color='grey',label='linear fit',linewidth=0.6)

print("linear result: ",popt[-2],perr)


chi_square = []

for i in range(points):
    h = tdltabc[i,0]
    value = tdltabc[i,1]
    chi = ( ( popt[-1]*h + popt[-2] - value ) / tdltabc[i,2] ) **2
    chi_square.append(chi)
    
print("chi_square is: ", sum(chi_square))


plt.tick_params(axis='both', which='major', labelsize=12)
plt.xlim([-0.001,0.081])
plt.ylim([-0.002,maxy])
plt.xlabel("$h_d$",fontsize=12)
plt.ylabel("$\Delta_d$",fontsize=12)
plt.legend(loc=4,fontsize=12,ncol=1)


#plt.savefig("pairing_c.pdf")
plt.show()
