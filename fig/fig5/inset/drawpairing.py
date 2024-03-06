import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(3.5,3))
plt.subplots_adjust(left=0.17,bottom=0.17,right=0.97,top=0.97)

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.linewidth"] = 0.6
plt.rcParams["xtick.major.width"] = 1.6
plt.rcParams["xtick.direction"] = 'out'
plt.rcParams["ytick.major.width"] = 1.6
plt.rcParams["ytick.direction"] = 'in'


dmrg = np.loadtxt("dmrg-ground.dat")
dmrge = np.loadtxt("dmrg-excited.dat")
dmrgel = np.loadtxt("dmrg-excitedline.dat")

qmc0 = np.loadtxt("qmcpairing-ground.dat")
#qmc1 = np.loadtxt("qmcpairing-ground_075.dat")

clist = ['r','orange','m','g','b','c','olive','grey','y']


qmccolor = 'k'
dmrgcolor = 'r'

#plt.errorbar(dmrg[:,0]/2,dmrg[:,1],dmrg[:,2],label="DMRG-ground",color='k',marker='s',linewidth=0.5)
#plt.errorbar(dmrgel[:,0]/2,dmrgel[:,1],dmrgel[:,2],color='k',linestyle='--',label="dmrg-excited",marker='^',linewidth=0.5)

#for i in range(len(dmrge)):
#    if i==0:  plt.errorbar(dmrge[i,0]-0.01,dmrge[i,1],dmrge[i,2],marker='s',color='k',markersize=4)
#    else:  plt.errorbar(dmrge[i,0]+0.01,dmrge[i,1],dmrge[i,2],marker='s',color='k',markersize=4)



plt.errorbar(2*qmc0[:,0],qmc0[:,1],qmc0[:,2],label="QMC-ground",color=qmccolor,linewidth=1.5,marker='o',markersize=2)

kx_list = ['00','05','15','25','35','45','50']

for kx in kx_list:
    qmc70 = np.loadtxt("energyqmc"+kx+"-70.dat")
    qmc75 = np.loadtxt("energyqmc"+kx+"-75.dat")
    for i in range(len(qmc70)):
        x = int(kx)*0.01
        y = (qmc70[i,1] - qmc75[i,1])/(0.005)/2.8284/156
        err = (qmc70[i,2]**2 + qmc75[i,2]**2 )**0.5 / (0.005)/2.8284/156
  
        print(round(x,2),y,err)

        if kx=='35' and i==0:  plt.plot(2*x,y,label="QMC-excited",marker='o',color=qmccolor,markersize=2,linewidth=0)
        else:  plt.plot(2*x,y,marker='o',color=qmccolor,markersize=2)


plt.errorbar(dmrgel[:,0],dmrgel[:,1],dmrgel[:,2],color=dmrgcolor,linestyle='--',label="DMRG-first excited",linewidth=1.0,marker='s',markersize=3)
plt.errorbar(dmrg[:,0],dmrg[:,1],dmrg[:,2],label="DMRG-ground",color=dmrgcolor,linewidth=1.5,marker='s',markersize=3)
#plt.errorbar(dmrgel[:,0]/2,dmrgel[:,1],dmrgel[:,2],color='k',linestyle='--',label="dmrg-excited",marker='^',linewidth=0.5)

upper = np.loadtxt("upperp.dat")
lower = np.loadtxt("lowerp.dat")


plt.fill_between(2*upper[:,0],lower[:,1],upper[:,1],color=qmccolor,alpha=0.1)

#plt.title("fixed "+r"$h_p$"+"=0.205",fontsize=12)
plt.xlim([-0.03,1.03])
plt.ylim([0.032,0.074])
#plt.legend(ncol=1,fontsize=12,loc=3)
plt.xlabel(r"$k_x/\pi$",fontsize=16)
plt.ylabel(r"$\Delta$",fontsize=16)
plt.savefig("benchmarkpairing2.pdf")
