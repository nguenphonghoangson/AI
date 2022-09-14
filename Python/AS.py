import queue
import os
from Node import Node
from Distance import Distance
def ID():
    graph=[]
    distance=[]
    with open('InputFile2.txt') as f:
            l=f.readline()
            s=l.strip().split(',')[0]
            e=l.strip().split(',')[1]
            while True:
                l = f.readline()
                if not l:
                    break
                x=Node(l.strip().split(',')[0])
                x.setneighbors(l.strip().split(',')[1])
                x.setweight(int(l.strip().split(',')[2]))
                dist=l.strip().split(',')[3].split()
                neighbors=x.neighbor.split()
                for i in range(0,len(neighbors)):
                        distance.append(Distance(x,Node(neighbors[i]),int(dist[i])))
                graph.append(x)
    return graph,s,e,distance
def ED(v,g,q):
    PV(v)
    PN(g,v)
    PIVQ(q)
def PV(v):
    with open('Out_AS.txt', 'a') as f:
        print(v.vertex+str(v.weight))
        f.write(v.vertex+str(v.weight))
        f.write('\t\t\t\t\t\n')
        f.close()
def PN(g,v):
    with open('Out_AS.txt', 'a') as f:
        if g:
            for neighbor in g:
                f.write('\t\t\t\t\t')
                f.write(neighbor)
                f.write('\t\t\t')
                f.write(str(getDistance(v,Vertex(neighbor))))
                f.write('\t\t\t')
                f.write(str(Vertex(neighbor).weight))
                f.write('\t\t\t')
                f.write(str(Vertex(neighbor).g))
                f.write('\t\t\t')
                f.write(str(Vertex(neighbor).g+Vertex(neighbor).weight))
                f.write('\n')
            f.write('\t\t\t\t')
        else: f.write('\t\t\t\t')
        f.close()
def PIVQ(q):
    list=[]
    while q.qsize():
        v=q.get()                                        
        list.append(v)
    with open('Out_AS.txt', 'a') as f:
        f.write('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')
        for v in list:
            f.write(v[1].vertex+str(v[0]))
        f.write('\n')
        f.close()
    while list:
        q.put(list.pop(0))
def SD(st,x):
    print(st)
    list,e=[],st.pop()
    list.append(e)
    while st:
        v=st.pop()
        l=Vertex(v).neighbor.split();
        if l:
            if  e in l:
                e=v
                list.append(e);
    with open('Out_AS.txt', 'a') as f:
        f.write("Direction =>")
        for i in range(len(list)-1,-1,-1):
            f.write('->'+list[i])
        print(e)
        f.write('  Do dai '+str(x.g))
    
def Vertex(x):
    n=Node(x)
    for i in range(0,len(graph)):
            if x is graph[i].vertex:
                n = graph[i]
    return n
def getDistance(n1,n2):
    for i in distance:
        if n1.vertex==i.x.vertex and n2.vertex==i.y.vertex:
            return i.dist
    return 0;
def AS():
    q,st=queue.PriorityQueue(),[];
    q.put((Vertex(s).weight,Vertex(s)))
    while q:
        v=q.get()
        print(v[1].vertex+str(v[0]))
        # print(v[1].neighbor)
        st.append(v[1].vertex)
        g=v[1].neighbor.split(); 
        print(g)
        if v[1].vertex==Vertex(e).vertex: 
            ED(v[1],g,q)
            break
        if g:
            for neighbor in g:
                    a=Vertex(neighbor)
                    x=getDistance(v[1],a)+v[1].g
                    a.setg(x)
                    f=a.weight+a.g
                    q.put((f,a))  
        ED(v[1],g,q) 
    SD(st,Vertex(e));
if __name__ == '__main__':
        os.remove('Out_AS.txt')
        graph,s,e,distance=ID()
        # for i in graph:
        #     print(i.vertex+i.neighbor+str(i.weight))
        # for i in distance:
        #     print(i.x.vertex+i.y.vertex+str(i.dist))
        # print(str(getDistance(graph[0],graph[1])))
        with open('Out_AS.txt', 'a') as f:
            f.write('TT\t\t\t\t\tTTK\t\t\tk(u,v)\t\th(v)\t\tg(v)\t\tf(v)\t\t\t\tDanh sach L\n')
            f.close()
        AS()
