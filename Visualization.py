"""
Module containing matlab code for visualization of the Lotka Volterra model.

Adapted from:
https://github.com/scipy/scipy-cookbook/blob/master/ipython/LotkaVolterraTutorial.ipynb
"""

import matplotlib.pyplot as plt
import os


def _createfolder(folder="graphs"):
    """ Make directory named folder in current working directory,
    if it doesn't exist. Returns name of folder.
    """
    if not os.path.isdir(folder):
        os.mkdir(folder)

    return folder


def evolution(t, X, savefig=True, showfig=True):
    """ Simple function to plot temporal evolution of X. """
    rabbits, foxes = X.T

    fig1 = plt.figure()
    plt.plot(t, rabbits, "r-", label="Rabbits")
    plt.plot(t, foxes, "b-", label="Foxes")

    plt.grid()
    plt.legend(loc="best")
    plt.xlabel("time")
    plt.ylabel("population")
    plt.title("Evolution of fox and rabbit populations")

    if savefig:
        foldername = _createfolder()
        fig1.savefig(os.path.join(foldername, "rabbits_and_foxes_1.png"))

    if showfig:
        plt.show()
