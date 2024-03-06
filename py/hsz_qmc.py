import numpy as np
import sys

def get_data2 (fname):
    dat = np.loadtxt (fname)
    shape = np.shape(dat)
    dat = np.reshape (dat, shape)
    return dat

def get_data (fname, lx, ly):
    rdat = np.loadtxt (fname)
    dat = np.reshape (rdat[:,0], (lx,ly))
    err = np.reshape (rdat[:,1], (lx,ly))
    return dat, err

if __name__ == '__main__':
    dat = get_data (sys.argv[1])
    datx = np.mean (dat, axis=1)
    xs = range(1,len(datx)+1)

    f,ax = plt.subplots()
    ax.plot (xs, datx)
    plt.show()
