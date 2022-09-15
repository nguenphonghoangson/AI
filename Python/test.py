from Node import Node 
from Distance import Distance
def getDistance(n1,n2):
    for i in distance:
        if n1.vertex==i.x.vertex and n2.vertex==i.y.vertex:
            return i.dist
    return 0;
def Vertex(x):
    n=Node(x)
    for i in range(0,len(graph)):
            if x is graph[i].vertex:
                n = graph[i]
    return n
def CreatedNote(vertex,graph):
    for i in graph:
        if vertex==i.vertex:
            return i
    v=Node(vertex)
    graph.append(v)  
    return v   
def ID():
    graph =[]
    distance=[]
    with open('InputFile2.txt') as f:
            l=f.readline()
            s=l.strip().split(',')[0]
            e=l.strip().split(',')[1]
            while True:
                l = f.readline()
                if not l:
                    break
                x=CreatedNote(l.strip().split(',')[0],graph)
                x.setneighbors(l.strip().split(',')[1])
                x.setweight(int(l.strip().split(',')[2]))
                dist=l.strip().split(',')[3].split()
                neighbors=x.neighbor.split()
                for i in range(0,len(neighbors)):
                        distance.append(Distance(x,CreatedNote(neighbors[i],graph),int(dist[i])))
            f.close()
    return graph,distance
graph,distance=ID()
for i in graph:
    print(i.vertex+str(i.weight))
# for i in distance:
#     print(i.x.vertex+i.y.vertex+str(i.y.weight)+i.y.neighbor+str(i.dist))
print(str(getDistance(graph[0],graph[1])))