import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

plt.figure(figsize=(6,6))
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.96,top=0.96)


datapos = np.loadtxt("alldatapos.dat")
dataneg = np.loadtxt("alldataneg.dat")

curvepos = np.loadtxt("poscurve.dat")
curveneg = np.loadtxt("negcurve.dat")

fig, ax = plt.subplots()


for data in datapos:
    print(data)


x = np.array([0.001*i for i in range(400)])


curve_smooth_neg = interp1d(curveneg[:,0],curveneg[:,1],kind='cubic')
curve_smooth_pos = interp1d(curvepos[:,0],curvepos[:,1],kind='cubic')


#ax.errorbar(-datapos[:,0],datapos[:,1],datapos[:,2],color='b',label="tp=+0.2",linewidth=0.5)


#    ax.errorbar(data[0],data[1],data[2])

#for data in dataneg:
    
for i in range(len(dataneg)):
    if i==0:   ax.errorbar(dataneg[i,0],dataneg[i,1],dataneg[i,2],color='r',capsize=2.4,linewidth=0.5,marker='*')
    else:      ax.errorbar(dataneg[i,0],dataneg[i,1],dataneg[i,2],color='r',capsize=2.4,linewidth=0.5,marker='*')

for i in range(len(datapos)):
    if i==0:   ax.errorbar(-datapos[i,0],datapos[i,1],datapos[i,2],color='b',capsize=2.4,linewidth=0.5,marker='x')
    else:      ax.errorbar(-datapos[i,0],datapos[i,1],datapos[i,2],color='b',capsize=2.4,linewidth=0.5,marker='x')



ax.plot(x,curve_smooth_neg(x), color='r',label=r"$t'=-0.2$",linewidth=0.5,linestyle='--' )
ax.plot(-x,curve_smooth_pos(x), color='b',label=r"$t'=+0.2$",linewidth=0.5,linestyle='-.' )


labels = ["1/3","1/5","1/8","0","1/8","1/5","1/4","1/3"]

X = [-0.33,-0.2,-0.125,0,0.125,0.2,0.25,0.33]
Y = [0.01,0.02,0.03]



ax.spines['right'].set_visible(False)
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))



ax.set_xticklabels(labels)


ax.set_xticks(X)
ax.set_yticks(Y)

ax.set_ylim([0,0.03])

ax.set_xlabel(r"$\delta$"+"(doping)")
ax.set_ylabel("pairing order parameter")

plt.legend()

plt.savefig('scatter.pdf')

