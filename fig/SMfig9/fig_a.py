import numpy as np
import sys
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

plt.figure(figsize=(4,4))


plt.subplots_adjust(left=0.15,bottom=0.12,right=0.97,top=0.97)




plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.linewidth"] = 0.6
plt.rcParams["xtick.major.width"] = 1.6
plt.rcParams["xtick.direction"] = 'out'
plt.rcParams["ytick.major.width"] = 1.6
plt.rcParams["ytick.direction"] = 'in'

lx = 20
maxy = 0.053

plt.text(0.003,maxy*0.91,"(a)",fontsize=16)

xi = 2*(2**0.5)
width = 0.5
msize = 2


def get(ly,c,ms):
    tabc = np.loadtxt("tabcaverage"+str(ly)+str(lx)+".dat")
    plt.errorbar(tabc[:,0],tabc[:,1],tabc[:,2],label=str(lx)+r"$\times$"+str(ly),color=c,capsize=2,marker=ms,markersize=msize,linewidth=width)


try:
    get(4,'r','s')
except:
    pass

get(6,'orange','o')
get(8,'g','v')
try:
    get(10,'c','*')
except:
    pass

get(12,'b','x')

try:
    get(14,'m','^')
except:
    pass

try:
    get(16,'m','^')
except:
    pass



plt.xlim([-0.005,0.155])
plt.ylim([-0.002,maxy])

plt.tick_params(axis='both', which='major', labelsize=12)
plt.xlabel(r"$h_d$",fontsize=12)
plt.ylabel(r"$\Delta_d$",fontsize=12)

plt.legend(loc=4,fontsize=12,ncol=1,framealpha=1.0)

#plt.savefig("pairing_a.pdf")
plt.show()
