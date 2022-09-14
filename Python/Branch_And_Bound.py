import queue
import os
from traceback import print_tb
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
def ED(v,g,stack,l1):
    PV(v)
    PN(g,v)
    DSL1(l1)
    PIVS(stack)
def DSL1(l1):
    with open('Out_BAB.txt', 'a') as f:
        f.write('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')
        while l1:
            x=l1.pop()
            f.write(x.vertex+str(x.weight+x.g))
        f.write('\t\t\t')
def PV(v):
    with open('Out_BAB.txt', 'a') as f:
        print(v.vertex+str(v.weight))
        f.write(v.vertex+str(v.weight+v.g))
        f.close()
def PN(g,v):
    with open('Out_BAB.txt', 'a') as f:
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
def PIVS(stack):
    list=[]
    while stack.qsize():
        v=stack.get()                                        
        list.append(v)
    with open('Out_BAB.txt', 'a') as f:
        for v in list:
            f.write(v.vertex+str(v.weight+v.g))
        f.write('\n')
        f.close()
    while list:
        stack.put(list.pop())
def SD(st,x):
    print(st)
    list,e,st1=[],st.pop(),[]
    list.append(e)
    while st:
        v=st.pop()
        l=Vertex(v).neighbor.split();
        st1.append(v)
        if l:
            if  e in l:
                e=v
                list.append(e);
    while st1:
        st.append(st1.pop())
    with open('Out_BAB.txt', 'a') as f:
        f.write("Direction =>")
        for i in range(len(list)-1,-1,-1):
            f.write('->'+list[i])
        print(e)
        f.write('  Do dai '+str(x.g)+'\n')
def Vertex(x):
    n=Node(x)
    for i in range(0,len(graph)):
            if x is graph[i].vertex:
                n = graph[i]
    return n
def getWeight(e):
      return e.weight+e.g
def getDistance(n1,n2):
    for i in distance:
        if n1.vertex==i.x.vertex and n2.vertex==i.y.vertex:
            return i.dist
    return 0;
def BAB():
    stack,st,list,l1=queue.LifoQueue(),[],[],[];
    cost=0
    stack.put(Vertex(s))
    while stack:
        v=stack.get()
        st.append(v.vertex)
        g=v.neighbor.split(); 
        if v.vertex==Vertex(e).vertex:
            if(cost==0):
                cost=v.weight+v.g
                ED(v,g,stack,l1)
                SD(st,x);
                continue
            else:
                if((v.weight+v.g)<=cost):
                    ED(v,g,stack,l1)
                    SD(st,x);
                    continue
        if g:
            for neighbor in g: 
                    a=Vertex(neighbor)
                    x=getDistance(v,a)+v.g
                    a.setg(x)
                    f=a.weight+a.g  
                    list.append(a)
            list.sort(key=getWeight)
            while list:
                x=list.pop()
                l1.append(x)
                stack.put(x)  
        ED(v,g,stack,l1) 
if __name__ == '__main__':
        os.remove('Out_BAB.txt')
        graph,s,e,distance=ID()
        with open('Out_BAB.txt', 'a') as f:
            f.write('TT\t\t\t\t\tTTK\t\t\tk(u,v)\t\th(v)\t\tg(v)\t\tf(v)\t\t\tDanh sach L1\t\t\tDanh sach L\n')
            f.close()
        BAB()
