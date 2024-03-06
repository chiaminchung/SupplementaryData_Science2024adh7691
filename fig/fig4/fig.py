import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('../../py/')
import plotsetting2 as ps
import plotlatt as hszplt
import matplotlib.ticker as mticker
from matplotlib.lines import Line2D

def plot_data (ax):
    tabc = np.loadtxt("0075tabc.dat")[1:]
    xx = [0.45,-0.01]
    derr = 0.00374
    yy1 = [0.004-derr,0.015-derr]
    yy2 = [0.004+derr,0.015+derr]

    # TABC band
    ax.fill_between(xx,yy1,yy2,color='grey',alpha=0.2)
    dat = np.loadtxt('tabcaverage0.021.dat')
    ax.errorbar(1./dat[:,0],dat[:,1],dat[:,2],ls='None',c='grey',marker='.',capsize=2.,ms=8)
    ps.text (ax, 0.1, 0.26, 'TABC', fontsize=18, c='k', alpha=0.8)

    ms1, ms2 = 11, 12
    p2 = ax.errorbar(1/6,0.03356,0.00164, marker='o',color='b',markerfacecolor='None',mew=2,ms=ms1,ls='None',capsize=2.4)    # QMC, PBC
    p3 = ax.errorbar(1/6,0.01031,0.00151, marker='o',color='r',markerfacecolor='None',mew=2,ms=ms1,ls='None',capsize=2.4)    # QMC, APBC
    p4 = ax.errorbar(1/6,0.02953,0.00189, marker='.',color='b',ms=ms2,ls='None',capsize=2.4)    # DMRG, PBC
    p5 = ax.errorbar(1/6,0.01975,0.00276, marker='.',color='r',ms=ms2,ls='None',capsize=2.4)    # DMRG, APBC


    p6 = ax.errorbar(1/4,0.00595,0.00193,marker='o',color='b',markerfacecolor='None',mew=2,ms=ms1,ls='None',capsize=2.4)    # QMC, PBC
    p7 = ax.errorbar(1/4,0.01036,0.00027,marker='.',color='b',ms=ms2,ls='None',capsize=2.4)    # DMRG, PBC

    p8 = ax.errorbar(1/4,0.04763,0.00195,marker='o',color='r',markerfacecolor='None',mew=2,ms=ms1,ls='None',capsize=2.4)    # QMC, APBC
    p9 = ax.errorbar(1/4,0.04244,0.00082,marker='.',color='r',ms=ms2,ls='None',capsize=2.4)    # DMRG, APBC

    x1,x2,x3,x4 = 1/4,1/6,1/6.3,1/8
    y1,y2 = 0.5*(0.00595+0.01036), 0.5*(0.03356+0.02953)
    slop = (y2-y1)/(1/4-1/6)
    y3 = y2 - slop*(x3-1/6)
    y4 = y2 - slop*(x4-1/6)
    ax.annotate("", xy=(x4, y4), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>, head_width=0.5, head_length=2",color='b',lw=2,ls=':',alpha=0.3))
    y1,y2 = 0.5*(0.04763+0.04244), 0.5*(0.01031+0.01975)
    slop = (y2-y1)/(1/4-1/6)
    y3 = y2 - slop*(x3-1/6)
    y4 = y2 - slop*(x4-1/6)
    ax.annotate("", xy=(x4, y4), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>, head_width=0.5, head_length=2",color='r',lw=2,ls=':',alpha=0.3))


    ax.set_xlim([0,0.3])
    ax.set_ylim([-0.001,0.051])
    ax.set_xlabel("$1/L_y$",fontsize=22)
    ax.set_ylabel(r"$\Delta_d$",fontsize=22)


    # Legend
    ax = fig.add_axes([0.58, 0.55, 0.15, 0.18], anchor='C')
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_edgecolor('gray')
        spine.set_linewidth(0.8)
    legend_elements = [Line2D([0], [0], marker='o', mfc='None', c='b', ls='None', mew=1.5, markersize=ms1),
                       Line2D([0], [0], marker='.', c='b', ls='None', markersize=ms2),
                       Line2D([0], [0], marker='o', mfc='None', c='r', ls='None', mew=1.5, markersize=ms1),
                       Line2D([0], [0], marker='.', c='r', ls='None', markersize=ms2)]
    ax.legend (handles=legend_elements, loc='center', fontsize=10, ncol=2, columnspacing=2.2, labelspacing=1.5, handletextpad=0.15, bbox_to_anchor=(0.67,0.3), frameon=False)
    ps.text (ax, 0.5, 0.78, 'PBC', fontsize=16)
    ps.text (ax, 0.83, 0.78, 'APBC', fontsize=16)
    ps.text (ax, 0.18, 0.45, 'AFQMC', fontsize=16)
    ps.text (ax, 0.18, 0.15, 'DMRG', fontsize=16)


def plot_hszlatt (ax, dirr, lx, ly):
    #   ax.set_axis_off()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')

    hs = np.loadtxt (dirr+'/hole_qmc.data')[:,0]
    szs = np.loadtxt (dirr+'/spin_qmc.data')[:,0]

    hszplt.plot_square_latt (ax, lx, ly)

    xs, ys = hszplt.get_xys (lx, ly)
    hszplt.plot_hsz (ax, xs, ys, hs, szs, AFDomain=True, showtext=False)


fig,axs = plt.subplots (ncols=2, nrows=2, figsize=(13,5), sharex='col',
                        gridspec_kw=dict(width_ratios=[4.7,3], wspace=0.04, hspace=0.07, bottom=0.17, left=0.01, right=0.92, top=0.96))
gs = axs[0,1].get_gridspec()
axs[0,1].remove()
axs[1,1].remove()
ax0 = fig.add_subplot (gs[:,1])
ax0.yaxis.tick_right()
ax0.yaxis.set_label_position("right")
ax0.yaxis.set_ticks_position("both")
plot_data (ax0)

ax1, ax2 = axs[0,0], axs[1,0]
lx,ly = 32, 8
plot_hszlatt (ax1, dirr='tp0.2_n0.875_QMC_828apbc/', lx=lx, ly=ly)
lx,ly = 28, 8
plot_hszlatt (ax2, dirr='tp0.2_n0.875_QMC_828pbc/', lx=lx, ly=ly)
ax1.set_xlim (7,22)
ax1.set_ylim (ymin=2,ymax=6)
ax2.set_ylim (ymin=2,ymax=6)
ps.text (ax1, 0.04, 0.85, 'A', fontsize=22, bbox=dict(facecolor='w', edgecolor='None'))
ps.text (ax2, 0.04, 0.85, 'B', fontsize=22, bbox=dict(facecolor='w', edgecolor='None'))
ps.text (ax0, 0.07, 0.92, 'C', fontsize=22, bbox=dict(facecolor='w', edgecolor='None'))

# Scale
hszplt.plot_square_latt (ax2, 10, 2)
hszplt.plot_circle (ax2, 8, 1.2, h=0.15, hmax=0.3, alpha=0.5, clip_on=False)
ps.text (ax2, 0.17, -0.23, '$0.15$', fontsize=18)
hszplt.plot_szi (ax2, 11, 1.2, sz=0.15, szmax=0.3, clip_on=False)
ps.text (ax2, 0.35, -0.23, '$0.15$', fontsize=18)


labels = ["$1/\infty$","$1/12$","$1/6$","$1/4$"]
xx = [0,1/12,1/6,1/4]
ax0.set_ylim (ymin=0)
ps.set_tick_inteval (ax0.yaxis, 0.02, 0.01)
ax0.set_xticklabels (labels)
ax0.xaxis.set_major_locator(mticker.FixedLocator(xx))
ps.set_tick_size (ax0, major_size=8, major_width=1.5, minor_size=7, minor_width=1)

#fig.savefig('electron_doped_tabc.pdf')
plt.show()
