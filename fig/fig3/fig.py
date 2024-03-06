import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.lines import Line2D
import sys
sys.path.append('../../py/')
import plotsetting2 as ps



ps.set_plot_init ({'xtick.labelsize':12,'ytick.labelsize':12,'axes.linewidth':1.2})
fig = plt.figure(figsize=(5,4))

fig.subplots_adjust(left=0.12,bottom=0.12,right=0.97,top=0.97)

tempax = plt.subplot(1,1,1)

qmc = []
dmrg = []

qmc.append (np.loadtxt("0.125dopingqmc_pbc.dat"))
dmrg.append (np.loadtxt("0.125dopingdmrg_pbc.dat"))

qmc.append (np.loadtxt("0.125dopingqmc_apbc.dat"))
dmrg.append (np.loadtxt("0.125dopingdmrg_apbc.dat"))

qmc.append (np.loadtxt("0.2dopingqmc_pbc.dat"))
dmrg.append (np.loadtxt("0.2dopingdmrg_pbc.dat"))

qmc.append (np.loadtxt("0.2dopingqmc_apbc.dat"))
dmrg.append (np.loadtxt("0.2dopingdmrg_apbc.dat"))


ps.text (tempax, 0.2, 0.8, "1/8 doping",fontsize=12,bbox=dict(facecolor='w',edgecolor='k',linewidth=0.5))
ps.text (tempax, 0.8, 0.8, "1/5 doping",fontsize=12,bbox=dict(facecolor='w',edgecolor='k',linewidth=0.5))


diff = [0,0,12,12]
dd = 0.01

markers = ['o','x','o','x']



cnum = [24,24,30,30]
plabels = []

diff = 12
checklist = []


def check_same_data (x, y, mk, d=0.5):
    if x == 4 and y == 1/2:
        x -= 1*d
    elif x == 6 and y == 0.667:
        x -= 0.5*d
    elif x == 8 and y == 0.667:
        x -= 0.5*d
    elif x == 4+diff and y == 1/2:
        x -= 1*d
    elif x == 6+diff and y == 0.667:
        x -= 0.5*d
    elif x == 8+diff and y == 4/5:
        x -= 1*d
    elif x == 10+diff and y == 4/5:
        x -= 0.5*d

    while (x,y,mk) in checklist:
        x += d
    checklist.append ((x,y,mk))
    return x,y


for k in range(4):
    if k % 2 == 0: # PBC
        c = 'b'
    else:
        c = 'r'
    for i,ele in enumerate(qmc[k]):
        x,y = ele[0], ele[2]
        if k >= 2:
            x += diff
        x,y = check_same_data (x, y, 'o')
        tempax.plot (x, y, c=c, marker='o', mfc='None')

    # DMRG
    if k==1:
        x,y = dmrg[k][0], dmrg[k][2]
        if k >= 2:
            x += diff
        x,y = check_same_data (x, y, '.')
        tempax.plot (x, y, color=c, marker='.', ms=4)
        continue

    for i,ele in enumerate(dmrg[k]):
        x,y = ele[0], ele[2]
        if k >= 2:
            x += diff
        x,y = check_same_data (x, y, '.')
        tempax.plot (x, y, color=c, marker='.', ms=4)

labels = ["4","6","8","12","4","6","8","12"]
xx = [4,6,8,10, 4+diff,6+diff,8+diff,10+diff]


tempax.set_xticklabels (labels)
tempax.xaxis.set_major_locator(mticker.FixedLocator(xx))

ylabels = ["1/2","2/3","3/5","3/4","4/5","5/6","1"]
yticks = [1/2,2/3,3/5,3/4,4/5,5/6,1]
tempax.set_yticks(yticks)
tempax.set_yticklabels(ylabels)


ps.text (tempax, 0.5, -0.08, '$L_y$', fontsize=13)
tempax.set_ylabel("Stripe filling",fontsize=14)

plt.grid(True, lw=0.5)

# Legend
ax = fig.add_axes([0.43, 0.72, 0.27, 0.17], anchor='C')
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_edgecolor('gray')
    spine.set_linewidth(0.8)
legend_elements = [Line2D([0], [0], marker='o', mfc='None', c='b', ls='None', markersize=6),
                   Line2D([0], [0], marker='.', c='b', ls='None', markersize=6),
                   Line2D([0], [0], marker='o', mfc='None', c='r', ls='None', markersize=6),
                   Line2D([0], [0], marker='.', c='r', ls='None', markersize=6)]
ax.legend (handles=legend_elements, loc='center', fontsize=10, ncol=2, columnspacing=0.5, labelspacing=0.6, handletextpad=0.15, bbox_to_anchor=(0.65,0.3), frameon=False)
ps.text (ax, 0.5, 0.78, 'PBC', fontsize=10)
ps.text (ax, 0.81, 0.78, 'APBC', fontsize=10)
ps.text (ax, 0.2, 0.45, 'AFQMC', fontsize=10)
ps.text (ax, 0.23, 0.15, 'DMRG', fontsize=10)

# bars
IPS = [[4,1],[4,1/2],[4,1/4],
       [6,1],[6,1/3],[6,2/3],[6,1/6],
       [8,1],[8,1/2],[8,1/4],[8,3/4],[8,1/8],
       [12,1],[12,1/2],[12,1/3],[12,2/3],[12,1/6],[12,5/6],[12,1/12]]

w = 0.83
c = 'limegreen'
for x,y in IPS:
    if x == 12:
        x -= 2
    if y < 0.4: continue
    tempax.plot ([x-w,x+w], [y,y], c=c, lw=2.5, zorder=-1, solid_capstyle='round')
    tempax.plot ([x+diff-w,x+diff+w], [y,y], c=c, lw=2.5, zorder=-1, solid_capstyle='round')


tempax.axvline (13,c='k')
plt.tight_layout()
fig.savefig('filling_all.pdf')
plt.show()
         
            
        
