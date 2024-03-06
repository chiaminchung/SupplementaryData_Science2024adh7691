import numpy as np
import sys
import matplotlib.pyplot as plt

step = 6

plotnum = step

data1 = []
data2 = []

cbar = ['c','b','m','k']
sbar = ['o','v','*','p']

if plotnum>=1 :
    data1.append(   np.loadtxt("pairingqmc11.dat")     )
    data2.append(   np.loadtxt("pairingqmc21.dat")     )
if plotnum>=2 :
    data1.append(   np.loadtxt("pairingqmc12.dat")     )
    data2.append(   np.loadtxt("pairingqmc22.dat")     )
if plotnum>=3 :
    data1.append(   np.loadtxt("pairingqmc13.dat")     )
    data2.append(   np.loadtxt("pairingqmc23.dat")     )
if plotnum>=4 :
    data1.append(   np.loadtxt("pairingqmc16.dat")     )
    data2.append(   np.loadtxt("pairingqmc26.dat")     )


dmrg = np.loadtxt("dmrg.dat")


fig = plt.figure(figsize=(10,5))

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.linewidth"] = 1.2
plt.rcParams["xtick.major.width"] = 1.6
plt.rcParams["xtick.direction"] = 'in'
plt.rcParams["ytick.major.width"] = 1.6
plt.rcParams["ytick.direction"] = 'in'

plt.subplots_adjust(left=0.08,bottom=0.11,right=0.97,top=0.97,wspace=0,hspace=0)

labels1 = ["Iter1, "+r"$\alpha = $"+"0.10", "Iter2, "+r"$\alpha = $"+"0.27", "Iter3, "+r"$\alpha = $"+"0.37", "Iter6, "+r"$\alpha = $"+"0.43"  ]
labels2 = ["Iter1, "+r"$\alpha = $"+"1.00", "Iter2, "+r"$\alpha = $"+"0.53", "Iter3, "+r"$\alpha = $"+"0.46", "Iter6, "+r"$\alpha = $"+"0.43"  ]

axes1 = plt.subplot(121)
axes2 = plt.subplot(122)

for i in range(len(data1)):
    h1 = data1[i][:,0]
    value1 = data1[i][:,1]
    err1 = data1[i][:,2]

    h2 = data2[i][:,0]
    value2 = data2[i][:,1]
    err2 = data2[i][:,2]

    axes1.errorbar(h1,value1,err1,linewidth=0.8,color=cbar[i],marker=sbar[i],label=labels1[i],linestyle='--',markerfacecolor='None')
    axes2.errorbar(h2,value2,err2,linewidth=0.8,color=cbar[i],marker=sbar[i],label=labels2[i],linestyle='--',markerfacecolor='None')


axes1.errorbar(dmrg[:,0],dmrg[:,1],dmrg[:,2],label="DMRG", color='r',marker='s',linewidth=1.2,linestyle='-')
axes2.errorbar(dmrg[:,0],dmrg[:,1],dmrg[:,2],label="DMRG", color='r',marker='s',linewidth=1.2,linestyle='-')

axes1.tick_params(labelsize=16,top=False, bottom=True, left=True, right=False)
axes1.tick_params(axis='x',labelsize=16)
axes1.tick_params(axis='y',labelsize=16)

axes1.set_ylabel(r"$\Delta_d$", fontsize=16)

plt.setp(axes1, xticks=[0,0.03,0.06,0.09,0.12],yticks=[0,0.01,0.02,0.03,0.04,0.05], xlim=[-0.003,0.155], ylim=[-0.003,0.053] )


axes2.tick_params(labelsize=16, top=False, bottom=True, left=False, right=False)
axes2.tick_params(axis='y',labelcolor='None')

plt.setp(axes2, xticks=[0,0.03,0.06,0.09,0.12],yticks=[0,0.01,0.02,0.03,0.04,0.05], xlim=[-0.003,0.155], ylim=[-0.003,0.053] )

axes1.legend(fontsize=12,loc=4,framealpha=1.0)
axes2.legend(fontsize=12,loc=4,framealpha=1.0)

axes1.set_xlabel(r'$h_d$',fontsize=16)
axes2.set_xlabel(r'$h_d$',fontsize=16)

#plt.savefig("iteration_example"+str(step)+".pdf")
plt.show()




