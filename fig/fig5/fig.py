import sys, os
import matplotlib.pyplot as plt
import numpy as np
sys.path.append('../../py/')
import plotsetting2 as ps
from matplotlib.patches import Ellipse

def plot_outside (ax):
    qmccolor = 'k'
    dmrgcolor = 'r'

    tabc420 = np.loadtxt("outside/tabcaverage420.dat")
    tabc420o = np.loadtxt("outside/tabcaverage420_opbc.dat")
    tabc620 = np.loadtxt("outside/tabcaverage620.dat")
    tabc6202 = np.loadtxt("outside/tabcaverage620_smooth.dat")
    tabc620o = np.loadtxt("outside/tabcaverage620_o.dat")

    tabc820 = np.loadtxt("outside/tabcaverage820.dat")
    tabc820o = np.loadtxt("outside/tabcaverage820_o.dat")
    tabc1220 = np.loadtxt("outside/tabcaverage1220.dat")
    tabc1220o = np.loadtxt("outside/tabcaverage1220_o.dat")
    tabc1620 = np.loadtxt("outside/tabcaverage1620.dat")
    tabc1620o = np.loadtxt("outside/tabcaverage1620_o.dat")

    tdltabc = np.loadtxt("outside/tabcaveragetdl.dat")
    tdltabco = np.loadtxt("outside/tabcaveragetdl_o.dat")

    mk = 's'
    dmrgx = np.array([0.0075,0.0175,0.0275,0.0425,0.0525,0.0625,0.0725])*2*2**0.5
    dmrgy = [0.00751,0.01730,0.02681,0.03794,0.04401,0.04971,0.05457]
    dmrge = [0.00036,0.00146,0.00198,0.00256,0.00281,0.00302,0.00307]
    ax.errorbar (dmrgx, dmrgy, dmrge, label="DMRG", color=dmrgcolor, marker=mk, markersize=6, capsize=2.4,ls='-', lw=1.2,mew=2,elinewidth=1.5)

    qmcx, qmcy, qmce = [],[],[]
    for i in [2,6,10,16,20,24,28]:
        qmcx.append (tabc420o[i,0])
        qmcy.append (tabc420o[i,1])
        qmce.append (tabc420o[i,2])
    ax.errorbar (qmcx, qmcy, qmce, marker='o',markersize=7,color=qmccolor,label="AFQMC",capsize=2.4,ls='-',lw=1.2, mew=2,elinewidth=1.5)


    upper = tdltabc[:,1]+tdltabc[:,2]
    lower = tdltabc[:,1]-tdltabc[:,2]

    upperfitparam = np.polyfit(tdltabc[:,0],upper,2)
    lowerfitparam = np.polyfit(tdltabc[:,0],lower,2)

    upperfit = np.polyval(upperfitparam,tdltabc[:,0])
    lowerfit = np.polyval(lowerfitparam,tdltabc[:,0])


    err = 0
    for i in range(len(upperfit)):
        err += abs(upperfit[i]-upper[i]) + abs(lowerfit[i]-lower[i])


    ax.tick_params(axis='both', which='major', labelsize=15)
    ax.set_xlim([0,0.23])
    ax.set_ylim([0,0.06])
    ax.set_xlabel(r"$h_d$",fontsize=18)
    ax.set_ylabel(r"$\Delta_d$",fontsize=18)
    ax.legend(loc=2,fontsize=15,ncol=1,framealpha=1.0)

def plot_inset (ax):
    ps.set_frame_line_width (ax, 1.5)

    dmrg = np.loadtxt("inset/dmrg-ground.dat")
    dmrge = np.loadtxt("inset/dmrg-excited.dat")
    dmrgel = np.loadtxt("inset/dmrg-excitedline.dat")

    qmc0 = np.loadtxt("inset/qmcpairing-ground.dat")

    clist = ['r','orange','m','g','b','c','olive','grey','y']


    qmccolor = 'k'
    dmrgcolor = 'r'

    gsms = 4
    esms = 4

    ax.errorbar(2*qmc0[:,0],qmc0[:,1],qmc0[:,2],label="QMC-ground",color=qmccolor,linewidth=0.9,marker='o',markersize=gsms)

    kx_list = ['00','05','15','25','35','45','50']

    for kx in kx_list:
        qmc70 = np.loadtxt("inset/energyqmc"+kx+"-70.dat")
        qmc75 = np.loadtxt("inset/energyqmc"+kx+"-75.dat")
        for i in range(len(qmc70)):
            x = int(kx)*0.01
            y = (qmc70[i,1] - qmc75[i,1])/(0.005)/2.8284/156
            err = (qmc70[i,2]**2 + qmc75[i,2]**2 )**0.5 / (0.005)/2.8284/156
      
            print(round(x,2),y,err)

            if kx=='35' and i==0:  ax.plot(2*x,y,label="QMC-excited",marker='o',color=qmccolor,markersize=esms,linewidth=0)
            else:  ax.plot(2*x,y,marker='o',mfc='None',color=qmccolor,markersize=esms)


    mk = 's'
    ax.errorbar(dmrgel[:,0],dmrgel[:,1],dmrgel[:,2],color=dmrgcolor,linestyle='--',label="DMRG-first excited",linewidth=0.8,marker=mk,markersize=esms,capsize=2.4,mfc='None')
    ax.errorbar(dmrg[:,0],dmrg[:,1],dmrg[:,2],label="DMRG-ground",color=dmrgcolor,linewidth=1.2,marker=mk,markersize=gsms,capsize=2.4)

    upper = np.loadtxt("inset/upperp.dat")
    lower = np.loadtxt("inset/lowerp.dat")


    ax.fill_between(2*upper[:,0],lower[:,1],upper[:,1],color=qmccolor,alpha=0.1)

    ax.set_xlim([-0.03,1.03])
    ax.set_ylim([0.032,0.074])
    ax.set_xlabel(r"$k_y/\pi$",fontsize=12)
    ax.set_ylabel(r"$\Delta_d$",fontsize=12)
    ax.tick_params(axis='both', which='major', labelsize=12)

    ps.text (ax, 0.4, 0.8, 'low lying states', fontsize=14)

if __name__ == '__main__':
    fig, ax = plt.subplots(figsize=(6,4.8))
    plot_outside (ax)
    ps.set_tick_size (ax, major_size=8, major_width=1.5, minor_size=6, minor_width=1)
    ps.set_tick_inteval (ax.yaxis, 0.02, 0.01)
    ps.set_tick_inteval (ax.xaxis, 0.05, 0.025)

    p = Ellipse((0.0725*2*2**0.5, 0.0535), 0.022, 0.012, facecolor='None',edgecolor='k')
    ax.add_patch (p)
    ax.annotate("", xy=(0.18, 0.032), xytext=(0.0725*2*2**0.5, 0.048),
                arrowprops=dict(arrowstyle="-|>, head_width=0.2, head_length=1",color='k',lw=1,ls='-'))

    ax = fig.add_axes([0.57, 0.265, 0.37, 0.33], anchor='C')
    plot_inset (ax)

    plt.tight_layout()
    plt.show()
