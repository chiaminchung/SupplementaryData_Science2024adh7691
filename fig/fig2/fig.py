import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.pyplot import MultipleLocator
import sys
sys.path.append('../../py/')
import plotsetting2 as ps

ps.set_plot_init ({'axes.linewidth':1.5})

fig,axs = plt.subplots (ncols=4, nrows=4, figsize=(5.5,4.5),# sharex='col',
                        gridspec_kw=dict(width_ratios=[0.36,1.67,1.67,1.67], height_ratios=[0.31,1.33,1.33,1.33],
                        wspace=0, hspace=0, left=0.11, bottom=0.11,right=0.91,top=0.97))

axss = [axs[1,1],axs[1,2],axs[1,3],axs[2,1],axs[2,2],axs[2,3],axs[3,1],axs[3,2],axs[3,3]]
for ax in axss:
    ps.set_tick_size (ax, major_size=5, major_width=1, minor_size=3, minor_width=1)

for ax in [axs[0,0],axs[0,1],axs[0,2],axs[0,3],axs[1,0],axs[2,0],axs[3,0]]:
    ax.set_axis_off()
    ax.set_xticks([])
    ax.set_yticks([])

ps.set_tick_inteval (axs[3,1].xaxis, major_itv=8, minor_itv=4)
ps.set_tick_inteval (axs[3,2].xaxis, major_itv=12, minor_itv=6)
ps.set_tick_inteval (axs[3,3].xaxis, major_itv=16, minor_itv=8)
ps.set_tick_inteval (axs[1,3].yaxis, major_itv=0.2, minor_itv=0.1)
ps.set_tick_inteval (axs[2,3].yaxis, major_itv=0.2, minor_itv=0.1)
ps.set_tick_inteval (axs[3,3].yaxis, major_itv=0.2, minor_itv=0.1)

ps.text (axs[1,3], 1.1, 0.5, '$4$', fontsize=12, color='b')
ps.text (axs[2,3], 1.1, 0.5, '$6$', fontsize=12, color='b')
ps.text (axs[3,3], 1.1, 0.5, '$8$', fontsize=12, color='b')
ps.text (axs[0,1], 0.5, 0.5, '$16$', fontsize=12, color='b')
ps.text (axs[0,2], 0.5, 0.5, '$24$', fontsize=12, color='b')
ps.text (axs[0,3], 0.5, 0.5, '$32$', fontsize=12, color='b')
ps.text (axs[0,3], 0.9, 0.5, '$L_x$', fontsize=14, color='b')
ps.text (axs[0,3], 1.1, -0.4, '$L_y$', fontsize=14, color='b')


spincolor = "k"
dmrgspin = "r"

plt.rcParams["ytick.direction"] = 'in'



words = ["1/2","1/2","1/2","2/3","3/5","2/3","2/3","3/4","2/3"]

Lx = [4,6,8]
Ly = [16,24,32]

index = 0
for lx in Lx:
    for ly in Ly:
        tempax = axss[index]
        index += 1

        
        data = np.loadtxt("spin"+str(lx)+str(ly)+".dat")
        datahole = np.loadtxt("hole"+str(lx)+str(ly)+".dat")

        spin = [0]*ly
        spinerr = [0]*ly
        hole = [0]*ly
        holeerr = [0]*ly

        
        for i in range(ly):
            temp,temp2 = [],[]
            for j in range(lx):
                temp.append(data[i,j])
                temp2.append(datahole[i,j])
            ave = np.mean(temp)
            err = np.std(temp)/(lx**0.5)
            spin[i] = ave
            spinerr[i] = err

            ave = np.mean(temp2)
            err = np.std(temp2)/(lx**0.5)
            hole[i] = ave
            holeerr[i] = err


        if (lx==6 and (ly==16 or ly==24)) or (lx==8 and ly==16 ):
            tempax.text(0,0.23,"*",fontsize=20)


        stripe_filling = words[index-1]
        if (lx==6 and ly==24) or (lx==8 and ly==16) or (lx==8 and ly==32):
            stripe_filling += ', NIPS'
        ps.text (tempax, 0.5, 0.07, stripe_filling ,fontsize=11)

        tempax.errorbar(range(1,ly+1),spin,spinerr,color=spincolor,linewidth=1.0,marker='o',markersize=1)

        if lx<=6:
            dmrg = np.loadtxt("dmrg"+str(lx)+str(ly)+".dat")[::lx]
            for i in range(ly):  dmrg[i,3] *= (-1)**(i+1)
            tempax.plot(range(1,ly+1),dmrg[:,3],color=dmrgspin,linewidth=1.0,linestyle='--',marker='+',markersize=1)
            

        tempax.axhline (color='grey',linestyle='--',linewidth=0.5)

        tempax.set_ylim([-0.39,0.39])
        tempax.set_xlim([-(ly//10),ly+ly//10])


        if lx==8:
            tempax.tick_params(axis='x',labelsize=11)
        if ly != 16: 
            tempax.tick_params(axis='y',labelsize=0,colors='white')
        else:
            tempax.tick_params(axis='y',labelsize=11,colors='k')
            #tempax.yaxis.tick_right()

        if lx==6 and ly==16:
            tempax.set_ylabel(r"$(-1)^{x+y} S_z(x,y)$",color='k',fontsize=15)
            #tempax.yaxis.set_label_position("right")

        if lx==8 and ly==24:  tempax.set_xlabel("$x$",fontsize=16)

plt.tight_layout()
fig.savefig('stripe_overall_2.pdf')
plt.show()
            
        
