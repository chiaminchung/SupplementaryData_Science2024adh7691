import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6,4.8))

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.linewidth"] = 0.6
plt.rcParams["xtick.major.width"] = 1.6
plt.rcParams["xtick.direction"] = 'out'
plt.rcParams["ytick.major.width"] = 1.6
plt.rcParams["ytick.direction"] = 'in'

plt.subplots_adjust(left=0.12,bottom=0.12,right=0.97,top=0.97,hspace=0,wspace=0)

xi = 2*(2**0.5)
width = 0.5

qmccolor = 'k'
dmrgcolor = 'r'



#dmrg = np.loadtxt("pairingdmrg.dat")
#qmc0 = np.loadtxt("pairing416.dat")
#qmc1 = np.loadtxt("pairing616.dat")
#qmc2 = np.loadtxt("pairing816.dat")
#qmc22 = np.loadtxt("pairing816-2.dat")
#qmc3 = np.loadtxt("pairing1216.dat")

#tabc4 = np.loadtxt("tabcaverage4.dat")
#tabc610 = np.loadtxt("tabcaverage610.dat")
tabc420 = np.loadtxt("tabcaverage420.dat")
tabc420o = np.loadtxt("tabcaverage420_opbc.dat")
tabc620 = np.loadtxt("tabcaverage620.dat")
tabc6202 = np.loadtxt("tabcaverage620_smooth.dat")
tabc620o = np.loadtxt("tabcaverage620_o.dat")

#tabc630 = np.loadtxt("tabcaverage630.dat")
tabc820 = np.loadtxt("tabcaverage820.dat")
tabc820o = np.loadtxt("tabcaverage820_o.dat")
#tabc1016 = np.loadtxt("tabcaverage1016.dat")
#tabc1020 = np.loadtxt("tabcaverage1020.dat")
tabc1220 = np.loadtxt("tabcaverage1220.dat")
tabc1220o = np.loadtxt("tabcaverage1220_o.dat")
tabc1620 = np.loadtxt("tabcaverage1620.dat")
tabc1620o = np.loadtxt("tabcaverage1620_o.dat")

#dmrg0 = np.loadtxt("dmrg416.dat")
#dmrg1 = np.loadtxt("dmrg616.dat")

#tdlopbc = np.loadtxt("tdlopbc.dat")
tdltabc = np.loadtxt("tabcaveragetdl.dat")
tdltabco = np.loadtxt("tabcaveragetdl_o.dat")
#qmc22 = np.loadtxt("pairing824.dat")
#qmc3 = np.loadtxt("pairing1016.dat")
#qmc4 = np.loadtxt("pairing1216.dat")

#qmc00 = np.loadtxt("pairing416pbc.dat")
#qmc01 = np.loadtxt("pairing816pbc.dat")
#qmc02 = np.loadtxt("pairing1216pbc.dat")
#qmc03 = np.loadtxt("pairing424pbc.dat")

#dmrg0 = np.loadtxt("dmrg416.dat")
#dmrg1 = np.loadtxt("dmrg616.dat")
#qmc3 = np.loadtxt("pairing1220.dat")
#qmc4 = np.loadtxt("pairingqmc4.dat")
#qmcinf = np.loadtxt("pairinginf.dat")
#qmcinfpbc = np.loadtxt("pairinginfpbc.dat")

#qmc = np.loadtxt("pairingqmccombine.dat")

#hf = np.loadtxt("pairinghf1.dat")

#plt.errorbar(dmrg[:,0],dmrg[:,1],dmrg[:,2],label="dmrg-extrap",color='k',linewidth=2*width)
#plt.plot(dmrg[:,0],dmrg[:,3],label="dmrg-m=4000",color='k',marker='x',linestyle="--")

#plt.errorbar(qmc0[:,0],qmc0[:,1],qmc0[:,2],label="qmc-4x16",color='r',linewidth=1.5*width)
#plt.errorbar(dmrg0[:,0],dmrg0[:,1],dmrg0[:,2],label="dmrg-4x16",color='r',linewidth=1.5*width,linestyle='--')
#plt.errorbar(qmc1[:,0],qmc1[:,1],qmc1[:,2],label="qmc-6x16",color='orange',linewidth=1.5*width)
#plt.errorbar(dmrg1[:,0],dmrg1[:,1],dmrg1[:,2],label="dmrg-6x16",color='orange',linewidth=1.5*width,linestyle='--')
#plt.errorbar(qmc2[:,0],qmc2[:,1],qmc2[:,2],label="qmc-8x16",color='limegreen',linewidth=1.5*width)
#plt.errorbar(qmc22[:,0],qmc22[:,1],qmc22[:,2],label="qmc-8x16-kx=0.01",color='limegreen',linewidth=1.5*width,linestyle='-.')
#plt.errorbar(qmc3[:,0],qmc3[:,1],qmc3[:,2],label="qmc-12x16",color='darkgreen',linewidth=1.5*width)

#plt.errorbar(tabc4[:,0],tabc4[:,1],tabc4[:,2],label="tabc 4x16",color='orange')






plt.errorbar(0.0075*2.8284,0.00751, 0.00036,label="DMRG",color=dmrgcolor,marker='s',markersize=5)
plt.errorbar(0.0175*2.8284,0.01730, 0.00146,color=dmrgcolor,marker='s',markersize=5)
plt.errorbar(0.0275*2.8284,0.02681, 0.00198,color=dmrgcolor,marker='s',markersize=5)
plt.errorbar(0.0425*2.8284,0.03794, 0.00256,color=dmrgcolor,marker='s',markersize=5)
plt.errorbar(0.0525*2.8284,0.04401, 0.00281,color=dmrgcolor,marker='s',markersize=5)
plt.errorbar(0.0625*2.8284,0.04971, 0.00302,color=dmrgcolor,marker='s',markersize=5)
plt.errorbar(0.0725*2.8284,0.05457, 0.00307,color=dmrgcolor,marker='s',markersize=5)

for i in [2,6,10,16,20,24,28]:
    if i==2:   plt.errorbar(tabc420o[i,0],tabc420o[i,1],tabc420o[i,2],marker='o',markersize=5,color=qmccolor,label="QMC")
    else:    plt.errorbar(tabc420o[i,0],tabc420o[i,1],tabc420o[i,2],marker='o',markersize=5,color=qmccolor)

plt.plot(tabc420[:,0],tabc420[:,1],color=qmccolor,linewidth=2*width,linestyle="--",markerfacecolor='None')
plt.plot(tabc420o[:,0][::2],tabc420o[:,1][::2],color=qmccolor,linewidth=1.5*width,linestyle='-')


upper = tdltabc[:,1]+tdltabc[:,2]
lower = tdltabc[:,1]-tdltabc[:,2]

upperfitparam = np.polyfit(tdltabc[:,0],upper,2)
lowerfitparam = np.polyfit(tdltabc[:,0],lower,2)

upperfit = np.polyval(upperfitparam,tdltabc[:,0])
lowerfit = np.polyval(lowerfitparam,tdltabc[:,0])

#plt.plot(tdltabc[:,0],upper)
#plt.plot(tdltabc[:,0],lower)


err = 0
for i in range(len(upperfit)):
    err += abs(upperfit[i]-upper[i]) + abs(lowerfit[i]-lower[i])

print(err)
plt.fill_between(tdltabc[:,0],upperfit,lowerfit,color='grey',alpha=0.25)


#plt.errorbar(tdltabc[:,0][::2],tdltabc[:,1][::2],tdltabc[:,2][::2],color='m',label="QMC     TDL",marker='o',markersize=5)

#plt.errorbar(tdltabc[:,0],tdltabc[:,1],tdltabc[:,2],label="TDL-TABC",color='k',linestyle='-',linewidth=3*width)
#plt.errorbar(tdltabco[:,0],tdltabco[:,1],tdltabco[:,2],label="TDL-TABC-wrong",color='grey',linestyle='--',linewidth=width)

#for i in range(len(tdltabc)):
#    plt.errorbar(tdltabc[i,0],tdltabc[i,1],tdltabc[i,2],color='r',linestyle='-',linewidth=width*6,capsize=2.4)




#x = np.arange(0,0.15,0.01)
#y =  0.0826*x + 0.03441

#print(x,y)

#plt.plot(x,y,linestyle='-',color='r',label='TDL 0.034(1)',linewidth=0.6)

"""
flag = 0
for ele in qmc3:
    if flag==0:
        plt.errorbar(ele[0],ele[1],ele[2],label="qmc-12x16-mu2.19",color='b',marker='o',linewidth=1.5*width)
        flag += 1
    else:
        plt.errorbar(ele[0],ele[1],ele[2],color='b',marker='o',linewidth=1.5*width)


#plt.errorbar(tdl[:,0],tdl[:,1],tdl[:,2],label="tdl",color='k',linewidth=1.5*width)
#plt.errorbar(qmc22[:,0],qmc22[:,1],qmc22[:,2],label="qmc-8x24",color='darkgreen',linewidth=1.5*width)
#plt.errorbar(qmc3[:,0],qmc3[:,1],qmc3[:,2],label="qmc-10x16",color='c',linewidth=1.5*width)
#plt.errorbar(qmc4[:,0],qmc4[:,1],qmc4[:,2],label="qmc-12x16",color='b',linewidth=1.5*width)

#plt.errorbar(qmc00[:,0],qmc00[:,1],qmc00[:,2],label="qmc-4x16-pbc",color='gold',linewidth=1.5*width)
#plt.errorbar(qmc01[:,0],qmc01[:,1],qmc01[:,2],label="qmc-8x16-pbc",color='y',linewidth=1.5*width)
#plt.errorbar(qmc02[:,0],qmc02[:,1],qmc02[:,2],label="qmc-12x16-pbc",color='olive',linewidth=1.5*width)
#plt.errorbar(qmc03[:,0],qmc03[:,1],qmc03[:,2],label="qmc-4x24-pbc",color='orange',linewidth=1.5*width)

#plt.errorbar(dmrg0[:,0],dmrg0[:,1],dmrg0[:,2],label="dmrg-4x16",color='r',linewidth=0.5*width,linestyle="--")
#plt.errorbar(dmrg1[:,0],dmrg1[:,1],dmrg1[:,2],label="dmrg-6x16",color='orange',linewidth=0.5*width,linestyle="--")
#plt.errorbar(qmc3[:,0],qmc3[:,1],qmc3[:,2],label="qmc-12x20",color='c',linewidth=1.5*width)

#plt.errorbar(qmcinf[:,0],qmcinf[:,1],qmcinf[:,2],label="qmc-infx16",color='k',linewidth=width)
#plt.errorbar(qmcinfpbc[:,0],qmcinfpbc[:,1],qmcinfpbc[:,2],label="qmc-infx16-pbc",color='gray',linewidth=width)
#plt.errorbar(qmc3[:,0],qmc3[:,1],qmc3[:,2],label="qmc-iter3",color='green',linewidth=width)
#plt.errorbar(qmc4[:,0],qmc4[:,1],qmc4[:,2],label="qmc-iter4",color='c',linewidth=width)

#plt.errorbar(qmc[:,0],qmc[:,1],qmc[:,2],label="qmc-combine",color='b',linewidth=width)
#plt.plot(hf[:,0],hf[:,1],linestyle="--",color='green',linewidth=0.8*width,label="twf-iter4")
#for i in range(len(qmc5)):
#    if i==0: plt.errorbar(qmc5[i,0],qmc5[i,1],qmc5[i,2],marker='s',markersize=3,color='c',label="QMC-632-OBC")
#    else: plt.errorbar(qmc5[i,0],qmc5[i,1],qmc5[i,2],marker='s',markersize=3,color='c')

"""

#plt.title("1/5 doping, t'=-0.2, U=8,   TABC",fontsize=21)

plt.tick_params(axis='both', which='major', labelsize=15)
plt.xlim([-0.005,0.23])
plt.ylim([-0.001,0.059])
plt.xlabel(r"$h_d$",fontsize=15)
plt.ylabel(r"$\Delta$",fontsize=15)
plt.legend(loc=2,fontsize=15,ncol=1,framealpha=1.0)

plt.savefig("pairing_benchmark.pdf")
