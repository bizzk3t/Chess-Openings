
import json
from collections import deque


class DGraph:
    def __init__(self, d):
        self.adjlist = d
        self.genEdgeSet()

    def genEdgeSet(self):
        self.edges = set()
        for u in self.adjlist:
            for v in self.adjlist[u]:
                self.edges.add((u,v)) 
    
    def addNode(self,label):
        self.adjlist[label] = {}

    def addEdge(self, u, v, wt):
        if (u in self.adjlist and v in self.adjlist):
            self.adjlist[u][v] = wt
            self.edges.add((u,v))

    def removeEdge(self, u, v):
        self.adjlist[u].pop(v, None)
        if ((u,v) in self.edges):    
            self.edges.remove((u,v))

    def getEdgeWt(self, u, v):
        return self.adjlist[u][v]

    def getNeighbors(self, u):
        return self.adjlist[u].keys()

    def getEdgeSet(self):
        return self.edges

    def getNodeSet(self):
        return self.adjlist.keys()
    
    def __repr__(self):
        return str(self.adjlist)


    def drawDOT(self):
        openings_data = open("openings.json")
        openings = json.load(openings_data)

        thenodes = self.getNodeSet()
        i = 0
        nodes = {}
        total = ''
        for u in thenodes:
            nodes[str(u)]='a_'+str(i)
            i = i+1
        

        total = total + "digraph mygraph {"
        for n in nodes.keys():
            #total = total + nodes[n] + ' [label="'+n+'\n'+openings[n]['name']+'\n'+str(openings[n]['moves']) + '"]\n'
            total = total + nodes[n] + ' [label="'
            total = total + n +'\n'
            total = total + openings[n]['name']+'\n'
            for z in range(len(openings[n]['moves'])):
                if z % 2 == 0:
                    total = total + str((z//2)+1) + '. ' + openings[n]['moves'][z] + ' '
                else:
                    total = total +  openings[n]['moves'][z] + ' '

            total = total + '"]\n'


        for e in self.getEdgeSet(): 
            (u,v) = e 
            total = total + nodes[str(u)] + ' -> ' + nodes[str(v)] + ' [label="' + str(self.getEdgeWt(u,v)) + '"]\n'
        total = total + '}'
        return total





    def __getitem__(self, key):
        return self.adjlist[key]

    def reachable_from(self, u):
        # return set of nodes reachable from u.  
        pass

    # BOOM
    def dfs(self, visited):
        self.clock = 0
        for v in self.getNodeSet():
            visited[v] = False
    
        for v in self.getNodeSet():
            if (not visited[v]):
                self.explore(v, visited)
            

    def explore(self, u, visited):
        visited[u] = {} 
        self.previsit(u, visited)
        for v in self.getNeighbors(u):
            if (not visited[v]):
                self.explore(v, visited)
        self.postvisit(u, visited)

    def previsit(self, u, visited):
        visited[u]['pre'] = self.clock
        self.clock += 1



    def postvisit(self, u, visited):
        visited[u]['post'] = self.clock
        self.clock += 1

    # BOOM!
    def bfs(self, s, dist):
        dist[s] = 0
        Q = deque([s])
        while (len(Q) > 0):
            u = Q.popleft()
            for v in self.getNeighbors(u):
                if (v not in dist):
                    Q.append(v)
                    dist[v] = dist[u]+1

        




def trygraph():
    G = DGraph({"A00":{"A01":1},"A06":{"A07":1,"A09":1}})
    return G



