import pandas as pd
import networkx as nx

names = ['3elt_dual', '3elt', '176bit', 'fb-pages-government', 'fb-pages-politician','infect-hyper']
for name in names:

    header_list = ['a', 'b']
    E = pd.read_csv(f'./data/{name}.edges', sep=' ', header=None, names=header_list)

    G = nx.from_pandas_edgelist(E, 'a', 'b')

    nodes = list(G.nodes)
    edges = list(G.edges)
    print()
    print("*"*20+name+"*"*20)
    #no of nodes and edges
    edges_no = len(edges)
    nodes_no = len(nodes)
    print("Number of nodes is : {} and Number of edges is : {}".format(nodes_no,edges_no))

    #average degeree
    total = 0
    for node in nodes:
        total += len(G.adj[node])
    average = int(total/nodes_no)
    print(f"Average degree is : {average}")

    #density
    if nodes_no > 1:
        density = 2*edges_no/(nodes_no*(nodes_no-1))   
    else:
        density = 0
    print(f"Density of the graph is : {density}")


    # diameter
    try:
        diameter = nx.diameter(G)
        print(f"The diameter of the graph is {diameter}")
    except:
        print("Diameter can't be determined as it is disconnected.")



    # clustering coefficient
    clustering_coefficient = []
    for node in nodes:
        neighbour = G.adj[node]
        k=len(neighbour)
        if k <= 1:
            clustering_coefficient.append(0)
        else:
            e = 0
            for u in neighbour:
                for v in neighbour:
                    if G.has_edge(u,v):
                        e = e+1
            e = e/2
            clustering_coefficient.append((2 *e)/(k*(k-1)))
    print(f"Average clustering coefficient is : {sum(clustering_coefficient)/len(clustering_coefficient)}")


        





