import json
from pprint import pprint
import DGraph
import UGraph

if __name__ == "__main__":
    tree_data = open("le.json")
    tree = json.load(tree_data)

    G = DGraph.DGraph(tree)
    #print G.getNodeSet()
    le = open("le.dot", 'w')
    k = G.drawDOT()
    print k
    le.write(k)
	
