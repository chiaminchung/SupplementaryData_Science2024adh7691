import matplotlib.pyplot as pl
from matplotlib.ticker import MultipleLocator, LogLocator
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib as mpl
import numpy as np
from matplotlib.transforms import blended_transform_factory

# Run this function at the beginning
def set_plot_init (paradict=dict()):
    # checkout pl.rcParams.keys() for more options
    #pl.rcParams.update({'font.family': 'DejaVu Sans'})
    #pl.rcParams.update({'font.family': 'Times New Roman'})
    #pl.rcParams.update({'font.family': 'Sans'})
    #pl.rcParams.update({'font.serif': ['Computer Modern']})
    pl.rcParams.update({'text.usetex': True})
    pl.rcParams.update({'legend.fontsize': 14})
    pl.rcParams.update({'axes.titlesize': 20})
    pl.rcParams.update({'axes.labelsize':20})
    pl.rcParams.update({'xtick.labelsize':20})
    pl.rcParams.update({'ytick.labelsize':20})
    pl.rcParams['axes.linewidth'] = 2
    for key,val in paradict.items():
        pl.rcParams.update({key: val})

set_plot_init ()

def get_default_colors ():
    prop_cycle = pl.rcParams['axes.prop_cycle']
    colors = prop_cycle.by_key()['color']
    return colors

# Run this function at the end
def set (axs=[],fontsize=22,tick_length=6):
    set_plot (axs,fontsize,tick_length)

def set_plot (axs=[],fontsize=22,tick_fontsize=22,tick_length=6):
    if type(axs) not in [list, tuple]: axs = [axs]
    if len(axs) == 0: axs = [pl.gca()]
    for ax in axs:
        # Set the xy-label font
        for xyax in (ax.xaxis, ax.yaxis):
            xyax.label.set_size (fontsize)
            xyax.get_offset_text().set_size(fontsize)
        # Set the tick labels font
        for tick in (ax.get_xticklabels() + ax.get_yticklabels()):
            tick.set_fontsize (tick_fontsize)
        # Set tick para
        ax.tick_params (length=tick_length)
        ax.minorticks_on()

        f = ax.get_figure()
        f.tight_layout()
        f.subplots_adjust()

def set_tick_inteval (xyaxis, major_itv, minor_itv=None):
# xyaxis should be ax.xaxis or ax.yaxis
    xyaxis.set_major_locator(MultipleLocator(major_itv))
    if minor_itv != None:
        xyaxis.set_minor_locator(MultipleLocator(minor_itv))

def set_tick_inteval_log (xyaxis, major_itv, minor_itv=None):
# xyaxis should be ax.xaxis or ax.yaxis
    xyaxis.set_major_locator(LogLocator(base=major_itv))
    if minor_itv != None:
        xyaxis.set_minor_locator(LogLocator(base=minor_itv))

def set_tick_size (ax, which='both', major_size=8, major_width=1.5, minor_size=6, minor_width=1):
    ax.tick_params(axis=which, which='major', size=major_size, width=major_width)
    ax.tick_params(axis=which, which='minor', size=minor_size, width=minor_width)

def set_axis_color (ax, xy, c):
# xy should be 'x' or 'y'
    if xy == 'x': xyaxis = ax.xaxis
    elif xy == 'y': xyaxis = ax.yaxis
    xyaxis.label.set_color (c)
    ax.tick_params(axis=xy, colors=c)

def set_label_position (xyaxis, x, y):
    xyaxis.set_label_coords (x, y)

def set_frame_line_width (ax, lw):
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(lw)

def text (ax, x, y, t, **args):
    return ax.text (x, y, t, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, **args)

def arrow (ax, x1, y1, x2, y2, style='->'):
    tform = blended_transform_factory(ax.transAxes, ax.transAxes)
    ax.annotate("", xy=(x1, y1), xytext=(x2, y2), arrowprops=dict(arrowstyle=style), xycoords=tform, textcoords=tform)

def pdf_combine (fname):
    return PdfPages (fname)

# set the colormap and centre the colorbar
class MidpointNormalize (mpl.colors.Normalize):
    """Normalise the colorbar."""
    def __init__(self, vmin=None, vmax=None, vzero=None, clip=False):
        self.midpoint = vzero
        mpl.colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return np.ma.masked_array(np.interp(value, x, y), np.isnan(value))
