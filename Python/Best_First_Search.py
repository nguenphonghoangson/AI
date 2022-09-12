import queue
import os
def Print_Vertex(vertex):
    with open('Out_BestFirstSearch.txt', 'a') as f:
        f.write(vertex[1]+str(vertex[0]))
        f.write('\t\t\t\t\t')
        f.close()
def Print_Neighbors(g):
    with open('Out_BestFirstSearch.txt', 'a') as f:
        if g:
            for neighbor in g:
                f.write(neighbor)
            f.write('\t\t\t\t\t')
        else: f.write('\t\t\t\t\t')
        f.close()
def Print_Visited(visited):
    with open('Out_BestFirstSearch.txt', 'a') as f:
        for v in visited:
            f.write(v)
        f.write('\t\t\t\t')
        f.close()
def Print_Implement_In_PQueue(q):
    list=[]
    while q.qsize():
        v=q.get()                                        
        list.append(v)
    with open('Out_BestFirstSearch.txt', 'a') as f:
        for v in list:
            f.write(v[1]+str(v[0])+' ')
        f.write('\n')
        f.close()
    while list:
        q.put(list.pop(0))
# def SearchDirection(storage):
#     list=[]
#     end=storage.pop()
#     list.append(end)
#     while storage:
#         v=storage.pop()
#         l=graph.get(v)
#         if l:
#             if  end in l:
#                 end=v
#                 list.append(end);
#     with open('Out_BestFirstSearch.txt', 'a') as f:
#         for i in range(len(list)-1,-1,-1):
#             f.write(list[i]+'->')


def ExportData(vertex,g,visited,q):
    Print_Vertex(vertex)
    Print_Neighbors(g)
    Print_Visited(visited)
    Print_Implement_In_PQueue(q)
def BestFirstSearch(graph,start,end,w): 
    visited,q,storage=[],queue.PriorityQueue(),[];
    q.put((w[start],start))
    while q:
        vertex=q.get()
        print(vertex)
        storage.append(vertex[1])
        if vertex[1]  not in visited:
            visited.append(vertex[1])
        g=graph.get(vertex[1]); 
        if vertex[1]==end: 
            ExportData(vertex,g,visited,q)
            break
        if g:
            for neighbor in g:
                if neighbor not in visited:
                    visited.append(neighbor)
                    q.put((w[neighbor],neighbor))
        ExportData(vertex,g,visited,q)          
if __name__ == '__main__':
        graph = {'A': ['C','E','D'], 'C': ['F'], 'F': ['B'],'I': ['G','B'], 'D': ['I','F'],'G': ['H','B'],'E':['K','G'],'H':['B']}
        w={'A':20,'B':0,'C':15,'D':6,'E':7,'F':10,'G':5,'H':3,'I':8,'K':12}
        start = 'A'
        end='B'
        os.remove('Out_BestFirstSearch.txt')
        with open('Out_BestFirstSearch.txt', 'a') as f:
            f.write('Vertex\t\t\t\tNeighbor\t\t\tVisited\t\t\t\tQueue\n')
            f.close()
        BestFirstSearch(graph,start,end,w)