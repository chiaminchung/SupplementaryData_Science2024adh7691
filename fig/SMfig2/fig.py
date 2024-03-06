import numpy as np
import sys, glob, os, copy
sys.path.append ('../../py/')
import matplotlib.pyplot as plt
import plotsetting2 as ps
import hsz_dmrg, hsz_qmc, hsz_plot
import plotlatt as hsz
from matplotlib.ticker import MultipleLocator
from matplotlib.legend_handler import HandlerTuple
from matplotlib.lines import Line2D

def plot_hszx (axh, axs, holes_dmrg, spins_dmrg, holes_qmc, herr_qmc, spins_qmc, serr_qmc, **args):
    sign = hsz_dmrg.stagger_sign (np.shape(spins_dmrg))
    spins_dmrg = sign * spins_dmrg
    spins_qmc = sign * spins_qmc

    # DMRG
    ph1 = hsz_plot.plot_hszx (holes_dmrg, axh, marker=args['mk'], c=args['c'], ls='-', label=args['lb'], lw=1, ms=6)
    ps1 = hsz_plot.plot_hszx (spins_dmrg, axs, marker=args['mk'], c=args['c'], ls='-', label=args['lb'], lw=1, ms=6)

    # QMC
    ph2 = hsz_plot.errorbar_hszx (holes_qmc, herr_qmc, axh, marker=args['mk'], c=args['c'], mfc='None', mew=2, ls='--', lw=1, ms=12)
    ps2 = hsz_plot.errorbar_hszx (spins_qmc, serr_qmc, axs, marker=args['mk'], c=args['c'], mfc='None', mew=2, ls='--', lw=1, ms=12)
    #if np.amax(spins_qmc) > 0 and np.amin(spins_qmc) < 0:
    axs.axhline (0, ls='--', c='gray')

    return ph1, ps1, ph2, ps2

def plot (axh, axs, dmrg_file, qmc_dir, lx, ly, **args):
    # Get data
    # DMRG
    holes_dmrg, spins_dmrg = hsz_dmrg.get_data (dmrg_file)
    # QMC
    fname_spin = glob.glob (qmc_dir+'/spin_qmc.data')[0]
    fname_hole = glob.glob (qmc_dir+'/hole_qmc.data')[0]
    holes_qmc, herr_qmc = hsz_qmc.get_data (fname_hole, lx, ly)
    spins_qmc, serr_qmc = hsz_qmc.get_data (fname_spin, lx, ly)

    return plot_hszx (axh, axs, holes_dmrg, spins_dmrg, holes_qmc, herr_qmc, spins_qmc, serr_qmc, **args)

def plot_hszx2 (axh, axs, holes_dmrg, spins_dmrg, holes_qmc, herr_qmc, spins_qmc, serr_qmc, stag_qmc=False, spin_sign_dmrg=1., **args):
    sign = hsz_dmrg.stagger_sign (np.shape(spins_dmrg))
    spins_dmrg = spin_sign_dmrg * sign * spins_dmrg
    if stag_qmc:
        spins_qmc = sign * spins_qmc

    # DMRG
    hsz_plot.plot_hszx (holes_dmrg, axh, marker=args['mk'], ls='--')
    hsz_plot.plot_hszx (spins_dmrg, axs, marker=args['mk'], ls='--')

    # QMC
    hsz_plot.plot_hszx (holes_qmc, axh, marker=args['mk'], mfc='None', ls=':')
    hsz_plot.plot_hszx (spins_qmc, axs, marker=args['mk'], mfc='None', ls=':')

    axs.axhline (0, ls='--', c='k')

def plot2 (axh, axs, dmrg_file, qmc_spin_file, qmc_hole_file, lx, ly, stag_qmc=False, spin_sign_dmrg=1., **args):
    # Get data
    # DMRG
    Np = lx*ly*4/5
    holes_dmrg, spins_dmrg = hsz_dmrg.get_data (dmrg_file, normalizeNp=Np)
    # QMC
    try:
        holes_qmc, herr_qmc = hsz_qmc.get_data (qmc_hole_file, lx, ly)
        spins_qmc, serr_qmc = hsz_qmc.get_data (qmc_spin_file, lx, ly)
    except:
        holes_qmc = hsz_qmc.get_data2 (qmc_hole_file)
        spins_qmc = hsz_qmc.get_data2 (qmc_spin_file)
        herr_qmc = None
        serr_qmc = None

    plot_hszx2 (axh, axs, holes_dmrg, spins_dmrg, holes_qmc, herr_qmc, spins_qmc, serr_qmc, **args)

def set_tick_size (ax):
    ax.tick_params(axis='x', which='major', size=8, width=1.5)
    ax.tick_params(axis='y', which='major', size=8, width=1.5)
    ax.tick_params(axis='x', which='minor', size=6, width=1)
    ax.tick_params(axis='y', which='minor', size=6, width=1)

if __name__ == '__main__':
    fig,ax = plt.subplots (nrows=2, ncols=2, figsize=(12,8), sharex=True, sharey='row',
                         gridspec_kw=dict(wspace=0.04, hspace=0, left=0.12, top=0.98, right=0.98, bottom=0.1))

    ax[1,0].spines['top'].set_visible(False)
    ax[1,1].spines['top'].set_visible(False)
    ax[0,0].spines['bottom'].set_linewidth(2)
    ax[0,1].spines['bottom'].set_linewidth(2)

    ax[0,0].tick_params(axis='y', which='major', labelsize=26)
    ax[1,0].tick_params(axis='y', which='major', labelsize=26)
    ax[1,0].tick_params(axis='x', which='major', labelsize=26)
    ax[1,1].tick_params(axis='x', which='major', labelsize=26)
    set_tick_size (ax[0,0])
    set_tick_size (ax[1,0])
    set_tick_size (ax[0,1])
    set_tick_size (ax[1,1])

    phd1, psd1, phq1, psq1 = plot (ax[0,0], ax[1,0],
          dmrg_file='hub16x4_U8_tp0.2_n0.875_edgeh0.25_hsz.dat',
          qmc_dir='tp0.2_n0.875_QMC_416pbc',
          lx=16, ly=4, c='royalblue', lb='$16\\times 4$ PBC', mk='o')

    phd2, psd2, phq2, psq2 = plot (ax[0,1], ax[1,1],
          dmrg_file='hub16x4_U8_tp0.2_n0.875_edgeh0.25_hsz.dat',
          qmc_dir='tp0.2_n0.875_QMC_416apbc',
          lx=16, ly=4, c='tab:red', lb='$16\\times 4$ APBC', mk='o')

    phd3, psd3, phq3, psq3 = plot (ax[0,1], ax[1,1],
          dmrg_file='hub16x6_U8_tp0.2_n0.875_edgeh0.25_hsz.dat',
          qmc_dir='tp0.2_n0.875_QMC_616pbc',
          lx=16, ly=6, c='royalblue', lb='$16\\times 6$ PBC', mk='^')

    phd4, psd4, phq4, psq4 = plot (ax[0,0], ax[1,0],
          dmrg_file='hub16x6_U8_tp0.2_n0.875_apbc_edgeh0.25_hsz.dat',
          qmc_dir='tp0.2_n0.875_QMC_616apbc',
          lx=16, ly=6, c='tab:red', lb='$16\\times 6$ APBC', mk='^')

    ax[0,0].set_ylabel ('$n(x,y)-1$',fontsize=26)
    ax[0,0].yaxis.set_label_coords(-0.17,0.5)
    ax[1,0].set_ylabel ('$(-1)^{x+y} S_z(x,y)$',fontsize=26)
    ax[1,0].set_xlabel ('$x$',fontsize=26)
    ax[1,1].set_xlabel ('$x$',fontsize=26)
    ax[0,1].yaxis.tick_right()
    ax[1,1].yaxis.tick_right()
    ax[0,0].set_ylim(ymin=0)
    ax[0,0].set_yticks([0,0.1,0.2])
    ax[0,0].set_yticks([0.05,0.15], minor=True)
    ax[0,0].set_yticklabels(['','$0.1$','$0.2$'])
    ax[0,0].xaxis.tick_top()
    ax[0,1].xaxis.tick_top()
    ps.set_tick_inteval (ax[1,0].xaxis, 4, 2)
    ps.set_tick_inteval (ax[1,1].xaxis, 4, 2)
    ps.set_tick_inteval (ax[1,0].yaxis, 0.2, 0.1)

    # Legend
    ax0 = fig.add_axes([0.22, 0.525, 0.21, 0.16], anchor='C')
    ax0.set_xticks([])
    ax0.set_yticks([])
    ax0.spines['bottom'].set_color('gray')
    ax0.spines['top'].set_color('gray') 
    ax0.spines['right'].set_color('gray')
    ax0.spines['left'].set_color('gray')
    legend_elements = [Line2D([0], [0], color='royalblue', marker='o', markersize=7.5, ls='None', label=''),
                       Line2D([0], [0], color='tab:red', marker='^', markersize=8, ls='None', label='')]
    ax0.legend (handles=legend_elements, ncol=1, frameon=False, columnspacing=0.8, labelspacing=1., loc='center right', bbox_to_anchor=(0.3, 0.31))
    ps.text (ax0, 0.5, 0.8, "\\textbf{N\\'{e}el AFM}", fontsize=26)
    ps.text (ax0, 0.5, 0.48, '$16\\times 4$ $\mathrm{PBC}$', fontsize=22, c='royalblue')
    ps.text (ax0, 0.54, 0.16, '$16\\times 6$ $\mathrm{APBC}$', fontsize=22, c='tab:red')
    
    ax0 = fig.add_axes([0.66, 0.525, 0.21, 0.16], anchor='C')
    ax0.set_xticks([])
    ax0.set_yticks([])
    ax0.spines['bottom'].set_color('gray')
    ax0.spines['top'].set_color('gray') 
    ax0.spines['right'].set_color('gray')
    ax0.spines['left'].set_color('gray')
    legend_elements = [Line2D([0], [0], color='tab:red', marker='o', markersize=7.5, ls='None', label=''),
                       Line2D([0], [0], color='royalblue', marker='^', markersize=8, ls='None', label='')]
    ax0.legend (handles=legend_elements, ncol=1, frameon=False, columnspacing=0.8, labelspacing=1., loc='center right', bbox_to_anchor=(0.3, 0.31))
    ps.text (ax0, 0.5, 0.8, '\\textbf{Filled stripes}', fontsize=26)
    ps.text (ax0, 0.54, 0.48, '$16\\times 4$ $\mathrm{APBC}$', fontsize=22, c='tab:red')
    ps.text (ax0, 0.5, 0.16, '$16\\times 6$ $\mathrm{PBC}$', fontsize=22, c='royalblue')


    fig.tight_layout()
    plt.show()
