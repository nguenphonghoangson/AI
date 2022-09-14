import queue
import os
from Node import Node
def ID():
    graph =[]
    with open('InputFile1.txt') as f:
        l=f.readline()
        s=l.strip().split(',')[0]
        e=l.strip().split(',')[1]
        while True:
            l = f.readline()
            if not l:
                break
            graph.append(Node(l.strip().split(',')[0],l.strip().split(',')[1],int(l.strip().split(',')[2])))
    return graph,s,e
def ED(v,g,vt,q):
    PV(v)
    PN(g)
    PVT(vt)
    PIVQ(q)
def PV(v):
    with open('Out_BestFirstSearch.txt', 'a') as f:
        print(v.vertex+str(v.weight))
        f.write(v.vertex+str(v.weight))
        f.write('\t\t\t\t\t')
        f.close()
def PN(g):
    with open('Out_BestFirstSearch.txt', 'a') as f:
        if g:
            for neighbor in g:
                f.write(neighbor)
            f.write('\t\t\t\t\t')
        else: f.write('\t\t\t\t\t')
        f.close()
def PVT(vt):
    with open('Out_BestFirstSearch.txt', 'a') as f:
        for v in vt:
            f.write(v)
        f.write('\t\t\t\t')
        f.close()
def PIVQ(q):
    list=[]
    while q.qsize():
        v=q.get()                                        
        list.append(v)
    with open('Out_BestFirstSearch.txt', 'a') as f:
        for v in list:
            f.write(v[1].vertex+str(v[0]))
        f.write('\n')
        f.close()
    while list:
        q.put(list.pop(0))
def SD(st):
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
    with open('Out_BestFirstSearch.txt', 'a') as f:
        f.write("Direction =>")
        for i in range(len(list)-1,-1,-1):
            f.write('->'+list[i])
def Vertex(x):
    n=Node(x)
    for i in range(0,len(graph)):
            if x is graph[i].vertex:
                n = graph[i]
    return n
def BFS():
    vt,q,st=[],queue.PriorityQueue(),[];
    q.put((Vertex(s).weight,Vertex(s)))
    while q:
        v=q.get()[1]
        st.append(v.vertex)
        if v.vertex  not in vt:
            vt.append(v.vertex)
        g=v.neighbor.split(); 
        if v.vertex==Vertex(e).vertex: 
            ED(v,g,vt,q)
            break
        if g:
            for neighbor in g:
                if neighbor not in vt:
                    vt.append(neighbor)
                    a=Vertex(neighbor)  
                    q.put((Vertex(neighbor).weight,Vertex(neighbor)))     
        ED(v,g,vt,q) 
    SD(st);
if __name__ == '__main__':
        os.remove('Out_BestFirstSearch.txt')
        graph,s,e =ID()
        with open('Out_BestFirstSearch.txt', 'a') as f:
            f.write('TT\t\t\t\t\tTTK\t\t\tk(u,v)\t\th(v)\t\tg(v)\t\tf(v)\t\t\tDanh sach L1\t\t\tDanh sach L\n')
            f.close()
        BFS()
