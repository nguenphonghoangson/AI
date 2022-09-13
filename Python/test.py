from cmath import e
from node import node
def getWeight(e):
      return e.weight
graph=[]
graph.append(node('A', 'B', 1))
graph.append(node('A', 'B', 4))
graph.append(node('A', 'B', 10))
graph.append(node('A', 'B', 12))
graph.sort(key=getWeight)
for i in graph:
    print(i.weight)
print(graph.pop().weight)