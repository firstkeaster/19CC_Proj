import matplotlib.pyplot as plt
import numpy as np
import os

def plotFunc(*args):
    # basedir = os.path.dirname(os.path.abspath(''))
    basedir = os.path.abspath('') + '/polls'
    def f(t):
        '''A damped exponential'''
        s1 = np.cos(2 * np.pi * t)
        e1 = np.exp(-t)
        return s1 * e1

    t1 = np.arange(0.0, int(args[0]), .2)
    fig, ax = plt.subplots(figsize = (6, 4))
    l = ax.plot(t1, f(t1), 'ro')
    plt.setp(l, markersize=30)
    plt.setp(l, markerfacecolor='C0')
    # if os.path.exists(basedir + '/images/' + 'tester.png'):
    #     os.remove(basedir + '/images/' + 'tester.png')
    figName = 'figure' + str(args[0]) + '.png'
    plt.savefig(basedir + '/images/' + figName)
    return figName

