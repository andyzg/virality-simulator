from constants import *
import matplotlib.pyplot as plt


def draw_graph(g):
    nx.draw_networkx(g, **DRAW_PROPERTIES)
    plt.axis('off')
    plt.show()


def draw_bar(bar):
    x = []
    height = []
    for i in bar:
        x.append(i)
        height.append(bar[i])
    plt.bar(x, height)
    plt.show()
