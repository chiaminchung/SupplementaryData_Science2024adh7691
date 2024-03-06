import pylab as pl
import numpy as np
import sys
sys.path.append('../../py/')
import plotsetting as ps

f1 = 'hub20x4_U8_tp-0.2_mu1.0.dat'
f2 = 'hub20x4_U8_tp-0.2_mu1.0_1st.dat'
f3 = 'hub20x4_U8_tp-0.2_mu1.0_2nd.dat'
f4 = 'hub20x4_U8_tp-0.2_mu1.1.dat'
qmc_en_file = 'energyqmc_1.0.dat'
qmc_pair_file = 'pairingqmc_1.0.dat'

dat1 = np.loadtxt (f1, skiprows=1)
dat2 = np.loadtxt (f2, skiprows=1)
dat3 = np.loadtxt (f3, skiprows=1)
dat4 = np.loadtxt (f4, skiprows=1)
qmc_pair = np.loadtxt (qmc_pair_file)
qmc_en = np.loadtxt (qmc_en_file)

f,axs = pl.subplots (figsize=(7,7), nrows=2, sharex=True)

ms = 7
axs[0].errorbar (dat1[:-1,0], dat1[:-1,1], dat1[:-1,2], marker='o', ms=ms, label='DMRG GS')
axs[0].errorbar (dat2[:-1,0], dat2[:-1,1], dat2[:-1,2], marker='s', ms=ms, label='DMRG 1st ES')
axs[0].errorbar (dat3[:,0], dat3[:,1], dat3[:,2], marker='^', ms=ms, label='DMRG 2nd ES')
axs[0].errorbar (qmc_pair[:-3,0], qmc_pair[:-3,1], qmc_pair[:-3,2], marker='x', ms=ms, mew=2, label='QMC GS')
axs[0].legend(fontsize=16,loc='lower right')
axs[0].set_ylabel ('$\\Delta_d$')
ps.text (axs[0],0.1,0.9,'(a)',fontsize=28)
ps.set (axs[0])

axs[1].errorbar (dat1[:-1,0], dat1[:-1,5], dat1[:-1,6], marker='o', ms=ms, label='GS')
axs[1].errorbar (dat2[:-1,0], dat2[:-1,4], dat2[:-1,5], marker='s', ms=ms, label='1st')
axs[1].errorbar (dat3[:,0], dat3[:,4], dat3[:,5], marker='^', ms=ms, label='2nd')
axs[1].errorbar (qmc_en[1:-3,0]*2*2**0.5, qmc_en[1:-3,1]/80-1., qmc_en[1:-3,2]/80, marker='x', ms=ms, mew=2, label='QMC GS')
axs[1].set_xlabel ('$h_d$')
axs[1].set_ylabel ('$E/N$')
ps.text (axs[1],0.9,0.9,'(b)',fontsize=28)
ps.set (axs[1])

ps.set_tick_inteval (axs[1].xaxis, 0.05, 0.01)

#f.savefig('compare.pdf')
pl.show()
