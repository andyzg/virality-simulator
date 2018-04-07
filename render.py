import networkx as nx
from constants import *
import matplotlib.pyplot as plt


def draw_graph(g):
    nx.draw_networkx(g, **DRAW_PROPERTIES)
    plt.axis('off')
    plt.show()


def draw_bar(bar):
    a = plt.plot([1,2,1])
    plt.subplot(121)
    x = []
    height = []
    for i in bar:
        x.append(i)
        height.append(bar[i])
    plt.bar(x, height)
    plt.xlabel('Number of shares')
    plt.xlim([-10, NODE_COUNT + 10])
    plt.title('Shares for each content seeded')
    plt.ylabel('Simulation count')


def draw_impressions(bar):
    a = plt.subplot(122)
    x = []
    height = []
    for i in bar:
        x.append(i)
        height.append(bar[i])
    plt.bar(x, height)
    plt.xlabel('% Share / View')
    plt.title('% Share vs View for each content seeded')
    plt.ylabel('Simulation count')
    plt.xlim([0, 100])
    plt.show()
