import numpy as np
import sys
import matplotlib.pyplot as plt

plt.figure(figsize=(4,4))
plt.subplots_adjust(left=0.15,bottom=0.12,right=0.97,top=0.97)

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.linewidth"] = 0.6
plt.rcParams["xtick.major.width"] = 1.6
plt.rcParams["xtick.direction"] = 'out'
plt.rcParams["ytick.major.width"] = 1.6
plt.rcParams["ytick.direction"] = 'in'



clist = ['r','orange','y','g','c','olive','b','darkgreen','m','grey','k']

dic = {0:0,2:2,4:4,6:6,8:8,10:10}

lx = 20
ymax = 0.053

plt.text(0.004,ymax*0.91,"(b)",fontsize=16)


sample = 100
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
    


num = 5

#  4,6,8,12,14,16
ly = [4,6,8,10,12,14,16]
data = [[],[],[],[],[],[],[]]


xx = []

def getdata(index):
    try:
        data[index] = np.loadtxt("tabcaverage"+str(ly[index])+str(lx)+".dat")
        if index > 0: xx.append(1.0/ly[index])
    except:
        print(ly[index],lx)
        pass


for index in range(7):
    getdata(index)

    


outputx = data[1][:,0]
outputy = []
outputerr = []

xxx = [0.25]+xx+[0]

print(len(data[1]))
for i in range(len(data[1])):
    yy = []
    err = []
    for index in range(1,7):
        if len(data[index]) == 0 : continue
        yy.append(data[index][i,1])
        err.append(data[index][i,2])

    
    [alpha,alphaerr,beta,betaerr] = draw(xx,yy,err,True)

    outputy.append(alpha)
    outputerr.append(alphaerr)
    print(outputx[i],"  ",outputy[-1],"  ",outputerr[-1])
    if i in dic:
        
        for j in range(len(xx)):
            plt.errorbar(xx[j],yy[j],err[j],color=clist[dic[i]],capsize=2.4,marker='o',markersize=3)
        plt.plot(np.array(xxx),np.array(xxx)*beta+alpha,color=clist[dic[i]],label=str(round(outputx[i],3)))
        plt.errorbar(0,alpha,alphaerr,color=clist[dic[i]],capsize=2.6,elinewidth=0.5)


if len(data[0]) > 0:
    for i in range(len(data[0])):
        if i in dic:
            plt.errorbar(0.25,data[0][i,1],data[0][i,2],color=clist[dic[i]],marker='s',markerfacecolor='None')




plt.xlim([-0.01,0.26])
plt.ylim([-0.002,ymax])

plt.tick_params(axis='both', which='major', labelsize=11)
plt.legend(loc=1,framealpha=1.0,ncol=2,fontsize=11)
plt.xlabel("1/"+r"$L_y$",fontsize=12)
plt.ylabel(r"$\Delta_d$",fontsize=12)
#plt.savefig("pairing_b.pdf")

outdata = []
for i in range(min(len(outputx),11)):
    outdata.append([outputx[i],outputy[i],outputerr[i]])
np.savetxt("tdltabc.dat",outdata)

plt.show()
