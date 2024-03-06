import matplotlib.pyplot as plt
import sys
sys.path.append('../../py/')
import plotlatt as hszplt
import numpy as np
from scipy.interpolate import interp1d
import plotsetting2 as ps
from matplotlib.ticker import MultipleLocator

def plot_hszlatt (ax, dirr, lx, ly):
    ax.set_axis_off()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')

    hs = np.loadtxt (dirr+'/hole_qmc.data')[:,0]
    szs = np.loadtxt (dirr+'/spin_qmc.data')[:,0]

    hszplt.plot_square_latt (ax, lx, ly)

    xs, ys = hszplt.get_xys (lx, ly)
    hszplt.plot_hsz (ax, xs, ys, hs, szs, AFDomain=True, showtext=False)

def plot_pd (ax):
    datapos = np.loadtxt("qmc_TDL/alldatapos.dat")
    dataneg = np.loadtxt("qmc_TDL/alldataneg.dat")

    curvepos = np.loadtxt("qmc_TDL/poscurve.dat")
    curveneg = np.loadtxt("qmc_TDL/negcurve.dat")


    x = np.array([0.001*i for i in range(400)])


    curve_smooth_neg = interp1d(curveneg[:,0],curveneg[:,1],kind='cubic')
    curve_smooth_pos = interp1d(curvepos[:,0],curvepos[:,1],kind='cubic')

    c = 'k'
    for i in range(len(dataneg)):
        if i==0:   ax.errorbar(dataneg[i,0],dataneg[i,1],dataneg[i,2],color=c,capsize=2.4,linewidth=1.5,elinewidth=1.5,marker='o',mfc='w',mew=2.5, ms=8)
        else:      ax.errorbar(dataneg[i,0],dataneg[i,1],dataneg[i,2],color=c,capsize=2.4,linewidth=1.5,elinewidth=1.5,marker='o',mfc='w',mew=2.5, ms=8)

    for i in range(len(datapos)):
        if i==0:   ax.errorbar(-datapos[i,0],datapos[i,1],datapos[i,2],color=c,capsize=2.4,linewidth=1.5,elinewidth=1.5,marker='o',mfc='w',mew=2.5, ms=8)
        else:      ax.errorbar(-datapos[i,0],datapos[i,1],datapos[i,2],color=c,capsize=2.4,linewidth=1.5,elinewidth=1.5,marker='o',mfc='w',mew=2.5, ms=8)



    ax.plot(x,curve_smooth_neg(x), color=c,label=r"$t'=-0.2$",linewidth=1.8,linestyle='-' )
    ax.plot(-x,curve_smooth_pos(x), color=c,label=r"$t'=+0.2$",linewidth=1.8,linestyle='-' )


    X = [-0.3,-0.15,0,0.15,0.3]
    labels = ["$0.3$","$0.15$","$0$","$0.15$","$0.3$"]
    Y = [0,0.01,0.02,0.03]


    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.set_xticklabels(labels)
    ax.set_xticks(X)
    ax.set_yticks(Y)
    ps.set_tick_inteval (ax.yaxis, 0.01, 0.005)
    ax.xaxis.set_minor_locator(MultipleLocator(0.05))

    ax.set_ylim([0,0.021])
    ax.set_xlim([-0.35,0.35])

    ax.set_xlabel("$\\delta$",fontsize=22)
    ax.set_ylabel("$\Delta_d$",fontsize=22)#,loc="top", rotation="horizontal")
    ax.tick_params(axis='x', which='major', labelsize=20, size=8, width=1.5)
    ax.tick_params(axis='y', which='major', labelsize=20, size=8, width=1.5)
    ax.tick_params(axis='x', which='minor', size=5, width=1)
    ax.tick_params(axis='y', which='minor', size=5, width=1)
    ax.axvline (0,c='k',lw=1)

    ps.text (ax,0.7,0.06,"hole doped",fontsize=18, color='k')
    ps.text (ax,0.28,0.06,"electron doped",fontsize=18, color='k')

    ps.text (ax,0.36,0.37,'A',fontsize=18, fontdict={'family': 'Sans'})#, fontweight='bold')
    ps.text (ax,0.63,0.81,'B',fontsize=18, fontdict={'family': 'Sans'})#, fontweight='bold')
    ps.text (ax,0.83,0.76,'C',fontsize=18, fontdict={'family': 'Sans'})#, fontweight='bold')

if __name__ == '__main__':
    fig,ax0 = plt.subplots()
    plot_pd (ax0)
    plt.tight_layout()

    fig1,ax1 = plt.subplots(figsize=(14,6))
    plot_hszlatt (ax1, dirr='tp0.2_n0.875_828apbc/', lx=28, ly=8)
    ax1.set_title ('(a)')

    fig2,ax2 = plt.subplots(figsize=(12,6))
    plot_hszlatt (ax2, dirr='tp-0.2_n0.875_824PBC/', lx=24, ly=8)
    ax2.set_title ('(b)')

    fig3,ax3 = plt.subplots(figsize=(18,6))
    plot_hszlatt (ax3, dirr='tp-0.2_n0.8_840PBC/', lx=40, ly=8)
    ax3.set_title ('(c)')

    plt.show()
