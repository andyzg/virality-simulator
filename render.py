from constants import *
import matplotlib.pyplot as plt


def draw_graph(g):
    nx.draw_networkx(g, **DRAW_PROPERTIES)
    plt.axis('off')
    plt.show()
