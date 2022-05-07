from matplotlib import pyplot as plt
import pandas as pd
import networkx as nx

names = ['3elt_dual', '3elt', '176bit', 'fb-pages-government', 'fb-pages-politician']
for name in names:
    header_list = ['a', 'b']
    E = pd.read_csv(f'./data/{name}.edges', sep=' ', header=None, names=header_list)

    G = nx.from_pandas_edgelist(E, 'a', 'b')

    nodes = list(G.nodes)
    edges = list(G.edges)

    def getmaxdegree():
        max = 0
        for node in nodes:
            if len(G.adj[node]) > max:
                max = len(G.adj[node])
        return max

    #degree distribution
    degrees = {}
    for i in range(0, getmaxdegree()+1):
        degrees[i] = 0
    for node in nodes:
        degrees[len(G.adj[node])] += 1
    frac = {}
    for i in range(0, getmaxdegree()+1):
        frac[i] = degrees[i]/len(nodes)
    k = frac.keys()
    Pk = frac.values()
    plt.figure("Degree distribution")
    plt.title(f"{name}")
    plt.xlabel('k')
    plt.ylabel('P(k)')
    plt.plot(k,Pk)
    plt.show()

