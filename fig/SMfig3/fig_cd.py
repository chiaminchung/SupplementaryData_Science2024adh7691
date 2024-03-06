import pylab as plt
import numpy as np
import sys
sys.path.append('../../py/')
import plotsetting as ps

def stagger_sign (shape):
    a = np.ones (shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            if i%2 == j%2:
                a[i,j] *= -1
    return a

def plot_x (ax, lx, ly, hsz, abss=False, stagger=False, **args):
    assert lx*ly == len(hsz), 'Sizse not match'
    hszlatt = np.array (hsz).reshape (lx,ly)
    if stagger:
        sign = stagger_sign ((lx,ly))
        hszlatt *= sign
        if np.max(hszlatt) > 0 and np.min(hszlatt) < 0:
            ax.axhline (0,ls='--',c='k')
    hszlatt = np.transpose (hszlatt)    # first index is for x
    xs = range(1,lx+1)
    hszy = np.mean (hszlatt, axis=0)
    ax.plot (xs, hszy, **args)

f1 = 'hub20x4_U8_tp-0.2_mu1.0_delta_0.0075_2sqrt2.out_hsz.dat'
f2 = 'hub20x4_U8_tp-0.2_mu1.0_delta_0.0075_2sqrt2_2.out_hsz.dat'
f3 = 'hub20x4_U8_tp-0.2_mu1.0_delta_0.0075_2sqrt2_3.out_hsz.dat'

hsz1 = np.loadtxt (f1, skiprows=1)[:,3]
hsz2 = np.loadtxt (f2, skiprows=1)[:,3]
hsz3 = np.loadtxt (f3, skiprows=1)[:,3]

plt.rcParams.update({'xtick.labelsize':24})
plt.rcParams.update({'ytick.labelsize':24})

fig, axs = plt.subplots (figsize=(7,7), nrows=2, sharex=True, sharey=True)
plot_x (axs[0], 20, 4, hsz1, stagger=True, marker='o', label='GS')
plot_x (axs[0], 20, 4, hsz2, stagger=True, marker='o', label='1st ES')
plot_x (axs[1], 20, 4, hsz3, stagger=True, marker='o', label='2nd ES', c='tab:green')
ps.set_tick_inteval (axs[0].xaxis, 4, 1)
ps.set_tick_inteval (axs[0].yaxis, 0.2, 0.1)
axs[0].set_ylim (-0.3,0.25)
axs[1].set_xlabel('$x$')
axs[0].set_ylabel('$(-1)^{x+y} S_z(x,y)$')
axs[1].set_ylabel('$(-1)^{x+y} S_z(x,y)$')
ps.text(axs[0],0.05,0.9,'(c)',fontsize=26)
ps.text(axs[1],0.05,0.9,'(d)',fontsize=26)
fig.tight_layout()
#fig.savefig('pin.pdf')
plt.show()
