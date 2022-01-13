# importing csv module
import csv
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


class GraphVisualization:
   
    def __init__(self):
        self.visual = []
   
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
          

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
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
       for x in range(10,30,2):
           if row[x]!='0':
               index=int(row[x])
               arr[index-1]=int(row[x+1])
               G.addEdge(source,row[x])


            



    G.visualize()
    print(arr)