import numpy as np
import sys
import matplotlib.pyplot as plt

def get_data (fname, normalizeNp=0):
    dat = np.loadtxt (fname, skiprows=1)
    lx,ly = map(int,dat[-1,:2])
    holes = np.reshape (dat[:,2], (lx,ly))
    spins = np.reshape (dat[:,3], (lx,ly))

    if normalizeNp != 0:
        Np = (lx*ly) - np.sum(holes)
        c = Np / normalizeNp
        spins /= c
        n = 1 - holes
        n /= c
        holes = 1 - n

    return holes, spins

def stagger_sign (shape):
    a = np.ones (shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            if i%2 == j%2:
                a[i,j] *= -1
    return a

if __name__ == '__main__':
    holes, spins = get_data (sys.argv[1])

    holesx = np.mean (holes, axis=1)
    spinsx = np.mean (spins, axis=1)
    xs = range(1,len(holesx)+1)

    f,ax = plt.subplots()
    ax.plot (xs, holesx)
    f,ax = plt.subplots()
    ax.plot (xs, spinsx)
    plt.show()
