import queue
import os
# Vertex: Đỉnh đang xét
# Neighbor: Đỉnh kề
# Visited: Đỉnh đã được đánh dấu
# queue: hàng đợi
def Print_Vertex(vertex):
    with open('Out_DeepFirstSearch.txt', 'a') as f:
        f.write(vertex+' ')
        f.write('\t\t\t\t\t')
        f.close()
def Print_Neighbors(g):
    with open('Out_DeepFirstSearch.txt', 'a') as f:
        if g:
            for neighbor in g:
                f.write(neighbor)
            f.write('\t\t\t\t\t')
        else: f.write('\t\t\t\t\t')
        f.close()
def Print_Visited(visited):
    with open('Out_DeepFirstSearch.txt', 'a') as f:
        for v in visited:
            f.write(v)
        f.write('\t\t\t\t')
        f.close()
def Print_Implement_In_Stack(stack):
    list=[]
    while stack.qsize():
        v=stack.get()                                        
        list.append(v)
    with open('Out_DeepFirstSearch.txt', 'a') as f:
        for v in list:
            f.write(v)
        f.write('\n')
        f.close()
    while list:
        stack.put(list.pop())
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
#     with open('Out_DeepFirstSearch.txt', 'a') as f:
#         for i in range(len(list)-1,-1,-1):
#             f.write(list[i]+'->')


def ExportData(vertex,g,visited,stack):
    Print_Vertex(vertex)
    Print_Neighbors(g)
    Print_Visited(visited)
    Print_Implement_In_Stack(stack)
def ImportData(start,end,graph):
    with open('InputFile.txt') as f:
        line=f.readline()
        start=line.strip().split(' ',1)[0]
        end=line.strip().split(' ',1)[1]
        while True:
            line = f.readline()
            if not line:
                break
            graph[line.strip().split(' ',1)[0]]=line.strip().split(' ',1)[1].split(' ')
    return graph,start,end
def DeepFirstSearch(graph,start,end):
    visited,stack,storage=[],queue.LifoQueue(),[];
    stack.put(start)
    while stack:
        vertex=stack.get()
        storage.append(vertex)
        if vertex  not in visited:
            visited.append(vertex)
        g=graph.get(vertex); 
        if vertex==end: 
            ExportData(vertex,g,visited,stack)
            break
        if g:
            for neighbor in g:
                if neighbor not in visited:
                    visited.append(neighbor)   
                    stack.put(neighbor)     
        ExportData(vertex,g,visited,stack) 
    # SearchDirection(storage);
if __name__ == '__main__':
        os.remove('Out_DeepFirstSearch.txt')
        start,end='',''
        graph =dict()
        graph,start,end =ImportData(start,end,graph)
        with open('Out_DeepFirstSearch.txt', 'a') as f:
            f.write('Vertex\t\t\t\tNeighbor\t\t\tVisited\t\t\t\tStack\n')
            f.close()
        DeepFirstSearch(graph,start,end)
