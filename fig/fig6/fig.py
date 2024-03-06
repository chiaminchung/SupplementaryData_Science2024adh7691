import drawpairing as draw1
import drawpairingtdlqua as draw2
import sys
import matplotlib.pyplot as plt
sys.path.append('../../py')
import plotsetting2 as ps
from matplotlib.patches import ConnectionPatch

fig,axs = plt.subplots (nrows=2, figsize=(6,6))
ps.set_frame_line_width (axs[0], 1.5)
ps.set_frame_line_width (axs[1], 1.5)

draw1.plot (axs[0])
draw2.plot (axs[1])
con = ConnectionPatch ((0.04,0.3), (0.29,0.53), coordsA=axs[0].transAxes, coordsB=axs[1].transAxes,
                      arrowstyle="]->,widthA=0.5, lengthA=0.2", shrinkA=5, shrinkB=5,
                      mutation_scale=20, fc="k", color='gray',
                      connectionstyle="bar,angle=0,fraction=-0.45")
fig.add_artist(con)

# legend
handles, labels = axs[0].get_legend_handles_labels()
handles = [h[0] for h in handles]
axs[0].legend(handles, labels, fontsize=13)

ps.text (axs[0], 0.14, 0.9, 'A', fontsize=16)
ps.text (axs[1], 0.14, 0.9, 'B', fontsize=16)

ps.set_tick_inteval (axs[0].yaxis, 0.01, 0.005)
ps.set_tick_inteval (axs[1].yaxis, 0.02, 0.01)
ps.set_tick_inteval (axs[1].xaxis, 0.02, 0.01)
ps.set_tick_size (axs[0], major_size=6, major_width=1, minor_size=5, minor_width=1)
ps.set_tick_size (axs[1], major_size=6, major_width=1, minor_size=5, minor_width=1)

plt.tight_layout()
#fig.savefig('qmc_extra.pdf')
plt.show()
