# importing csv module
import csv
import networkx as nx
import matplotlib.pyplot as plt

bettery=[]
battery = [0 for i in range(10)] 

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
  

  

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
  

    for row in csvreader:
       source = row[2]
       for x in range(10,30,2):
           if row[x]!='0':
               G.addEdge(source,row[x])


            



    G.visualize()
