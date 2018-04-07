import networkx as nx
import sys
from socialnetwork import SocialNetwork
from content import Content

import math
from collections import defaultdict
import random
from constants import *
import util
import render


def main(pop=1, nonpop=0):
    g = nx.barabasi_albert_graph(NODE_COUNT, M_PARAM, 5)
    nodes = util.define_nodes(g)
    edges = util.define_affinity(g)
    sn = SocialNetwork(g, nodes, edges)
    bar = defaultdict(int)
    impressions = defaultdict(int)
    for i in range(0, 100):
        num_share, imp = share_content(sn, pop, nonpop)
        bar[num_share] += 1
        impressions[round(imp * 100)] += 1
    render.draw_bar(bar)
    render.draw_impressions(impressions)


def share_content(sn, popular, nonpopular):
    nodes = util.get_popular_nodes(sn)
    content = Content()
    for i in range(0, nonpopular):
        sn.nodes[nodes[i]].seed_content(content)

    for i in range(0, popular):
        sn.nodes[nodes[-1-i]].seed_content(content)

    sn.nodes[math.floor(random.random() * len(nodes))].seed_content(content)

    timestep = 1
    count = popular + nonpopular + 1
    while not content.is_dead:
        probs = {}
        # Get probability for sharing
        for i in sn.nodes:
            n = sn.nodes[i]
            if content.uuid not in n.content or i not in content.shared_by:
                probs[i] = util.probability_share_content(sn, n, content)

        # Get probability of sharing
        for i in probs:
            if random.random() < probs[i]:
                sn.nodes[i].share(content, timestep)
                count += 1

        content.timestep()
        timestep += 1

    i_count = 1
    for n in sn.nodes:
        node = sn.nodes[n]
        if content.uuid in node.seen:
            i_count += 1

    print(count, " / ", NODE_COUNT, timestep,)
    print("Share vs Impression: ", count, " / ", i_count)

    return count, count*1.0 / i_count


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    else:
        main(int(sys.argv[1]), int(sys.argv[2]))
