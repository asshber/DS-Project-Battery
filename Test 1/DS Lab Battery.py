import csv
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


class GraphVisualization:
   
    def __init__(self):
        self.edgelist = []
   
    def addEdge(self, s, d):
        tempedge = [s, d]
        self.edgelist.append(tempedge)
          

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.edgelist)
        nx.draw_networkx(G)
        plt.show()
  

G = GraphVisualization()

filename = "test.csv"
  
arr=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
  

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
  

    for row in csvreader:
       source = row[2]
       index=int(source)
       arr[index-1]=row[8]
       for x in range(10,31,2):
           if row[x]!='0':
               index=int(row[x])
               arr[index-1]=int(row[x+1])
               G.addEdge(source,row[x])
    G.visualize()
    print(arr)

            



    