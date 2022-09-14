class Node: 
    def __init__ (self,vertex,neighbor='',weight=0,g=0):
        self.vertex = vertex
        self.neighbor = neighbor
        self.weight =weight 
        self.g=g
    def setneighbors (self,neighbor):
        self.neighbor = neighbor
    def setweight (self,weight):
        self.weight = weight
    def setg (self,g):
        self.g = g
    def __eq__(self, other):
        if(other.vertex>self.vertex):
            return self.vertex < other.vertex
        else: 
            return self.vertex > other.vertex 
        return self.vertex == other.vertex

