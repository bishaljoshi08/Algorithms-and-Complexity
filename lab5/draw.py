import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

header_list = ['a', 'b']
E = pd.read_csv('data/infect-hyper.edges', sep=' ', header=None, names=header_list)

G = nx.from_pandas_edgelist(E, 'a', 'b')
nx.draw(G)
plt.show()