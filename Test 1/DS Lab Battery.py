import csv
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

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

filename = "Input.csv"
  
dic = {1:255,2:255,3:255,4:255,5:255,6:255,7:255,8:255,9:255,10:255,11:255,12:255,13:255,14:255,15:255,16:255}

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
  

    for row in csvreader:
       source = row[2]
       index=int(source)
       if(int(dic[index])>int(row[8])):
         dic[index]=int(row[8])
       for x in range(10,31,2):
           if row[x]!='0':
               index=int(row[x])
               if(int(dic[index])>int(row[x+1])):
                 dic[index]=int(row[x+1])
               G.addEdge(source,row[x])
    G.visualize()
    dic=sorted(dic.items(), key = lambda kv:(kv[1], kv[0]))
    print(dic)   

header=["Vertices", "battery"]
with open('Output.csv', 'w') as f:
    writer = csv.writer(f)

    writer.writerow(header)
    for key, value in dic:
        writer.writerow([key, value])


    f.close()