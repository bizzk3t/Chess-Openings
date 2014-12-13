
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
        openings_data = open('openings.json')
        openings = json.load(openings_data)

        thenodes = self.getNodeSet()
        i = 0
        nodes = {}
        total = ''
        for u in thenodes:
            #nodes[str(u)]='a_'+str(i)
            nodes[str(u)]=str(u)
            i = i+1
        
        moves = {   1:'{rank=same;MOVE_01;',2:'{rank=same;MOVE_02;',
                    3:'{rank=same;MOVE_03;',4:'{rank=same;MOVE_04;',
                    5:'{rank=same;MOVE_05;',6:'{rank=same;MOVE_06;',
                    7:'{rank=same;MOVE_07;',8:'{rank=same;MOVE_08;',
                    9:'{rank=same;MOVE_09;',10:'{rank=same;MOVE_10;',
                    11:'{rank=same;MOVE_11;',12:'{rank=same;MOVE_12;',
                    13:'{rank=same;MOVE_13;',14:'{rank=same;MOVE_14;',
                    15:'{rank=same;MOVE_15;',16:'{rank=same;MOVE_16;',
                    17:'{rank=same;MOVE_17;',18:'{rank=same;MOVE_18;',
                    19:'{rank=same;MOVE_19;',20:'{rank=same;MOVE_20;',
                    21:'{rank=same;MOVE_21;',22:'{rank=same;MOVE_22;',
                    23:'{rank=same;MOVE_23;',24:'{rank=same;MOVE_24;',
                    25:'{rank=same;MOVE_25;',26:'{rank=same;MOVE_26;',
                    27:'{rank=same;MOVE_27;',28:'{rank=same;MOVE_28;',
                    29:'{rank=same;MOVE_29;',30:'{rank=same;MOVE_30;'
                }

        total = total + 'digraph mygraph {\n'
        total = total + 'MOVE_01 [label="1." shape="box"]\n'
        total = total + 'MOVE_02 [label="1..." shape="box"]\n'
        total = total + 'MOVE_03 [label="2." shape="box"]\n'
        total = total + 'MOVE_04 [label="2..." shape="box"]\n'
        total = total + 'MOVE_05 [label="3." shape="box"]\n'
        total = total + 'MOVE_06 [label="3..." shape="box"]\n'
        total = total + 'MOVE_07 [label="4." shape="box"]\n'
        total = total + 'MOVE_08 [label="4..." shape="box"]\n'
        total = total + 'MOVE_09 [label="5." shape="box"]\n'
        total = total + 'MOVE_10 [label="5..." shape="box"]\n'
        total = total + 'MOVE_11 [label="6." shape="box"]\n'
        total = total + 'MOVE_12 [label="6..." shape="box"]\n'
        total = total + 'MOVE_13 [label="7." shape="box"]\n'
        total = total + 'MOVE_14 [label="7..." shape="box"]\n'
        total = total + 'MOVE_15 [label="8." shape="box"]\n'
        total = total + 'MOVE_16 [label="8..." shape="box"]\n'
        total = total + 'MOVE_17 [label="9." shape="box"]\n'
        total = total + 'MOVE_18 [label="9..." shape="box"]\n'
        total = total + 'MOVE_19 [label="10." shape="box"]\n'
        total = total + 'MOVE_20 [label="10..." shape="box"]\n'
        total = total + 'MOVE_21 [label="11." shape="box"]\n'
        total = total + 'MOVE_22 [label="11..." shape="box"]\n'
        total = total + 'MOVE_23 [label="12." shape="box"]\n'
        total = total + 'MOVE_24 [label="12..." shape="box"]\n'
        total = total + 'MOVE_25 [label="13." shape="box"]\n'
        total = total + 'MOVE_26 [label="13..." shape="box"]\n'
        total = total + 'MOVE_27 [label="14." shape="box"]\n'
        total = total + 'MOVE_28 [label="14..." shape="box"]\n'
        total = total + 'MOVE_29 [label="15." shape="box"]\n'
        total = total + 'MOVE_30 [label="15..." shape="box"]\n'

        total = total + 'MOVE_01->MOVE_02->MOVE_03->MOVE_04->MOVE_05->MOVE_06->MOVE_07->MOVE_08->MOVE_09->MOVE_10->'
        total = total + 'MOVE_11->MOVE_12->MOVE_13->MOVE_14->MOVE_15->MOVE_16->MOVE_17->MOVE_18->MOVE_19->MOVE_20->'
        total = total + 'MOVE_21->MOVE_22->MOVE_23->MOVE_24->MOVE_25->MOVE_26->MOVE_27->MOVE_28->MOVE_29->MOVE_30\n'

        for n in sorted(nodes.keys()):
            #total = total + nodes[n] + ' [label="'+n+'\n'+openings[n]['name']+'\n'+str(openings[n]['moves']) + '"]\n'
            total = total + nodes[n] + ' [label="'
            total = total + n +'\\n'
            total = total + openings[n]['name']+'\\n'
            for z in range(len(openings[n]['moves'])):
                if z % 2 == 0:
                    total = total + str((z//2)+1) + '. ' + openings[n]['moves'][z] + ' '
                else:
                    total = total +  openings[n]['moves'][z] + ' '
            #print len(openings[n]['moves']), n, openings[n]['moves']
            moves[len(openings[n]['moves'])] = moves[len(openings[n]['moves'])] + n + ';'
            total = total + '" style="filled"'

            num = n[0]
            if num == 'A':
                total = total + ' color="red"]\n'
            elif num == 'B':
                total = total + ' color="green"]\n'
            elif num == 'C':
                total = total + ' color="blue"]\n'
            elif num == 'D':
                total = total + ' color="yellow"]\n'
            elif num == 'E':
                total = total + ' color="orange"]\n'
            else:
                total = total + ']\n'

        for x in moves.values():
            total = total + x + '}\n'




        for e in self.getEdgeSet(): 
            (u,v) = e 
            #total = total + nodes[str(u)] + ' -> ' + nodes[str(v)] + ' [label="' + str(self.getEdgeWt(u,v)) + '"]\n'
            total = total + nodes[str(u)] + ' -> ' + nodes[str(v)] + ';\n'
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



