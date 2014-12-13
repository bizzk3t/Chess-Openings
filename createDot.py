import json
from pprint import pprint
import DGraph
import UGraph

if __name__ == "__main__":
    tree_data = open("tree.json")
    tree = json.load(tree_data)

    G = DGraph.DGraph(tree)
    U = UGraph.UGraph(tree)
    print len(tree)
    print len(G.getNodeSet())
    print len(U.getNodeSet())
    #print DGraph.trygraph()
    #print G['D45']
    #G.drawDOT()
    #G.drawDOT()
	
