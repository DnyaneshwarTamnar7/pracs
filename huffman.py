import heapq

class node:
    def __init__(self,symbol,freq,left=None,right=None):
        self.symbol=symbol
        self.freq=freq
        self.left=left
        self.right=right
        self.huff=''
    
    def __lt__(self,nxt):
        return self.freq<nxt.freq

def printNodes(node,val=''):
    newVal=val+str(node.huff)
    if node.left:
        printNodes(node.left,newVal)
    if node.right:
        printNodes(node.right,newVal)
    if (not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")


chars=['a','b','c','d','e','f']
freq=[5,9,12,13,16,45]
nodes=[]

for i in range(len(chars)):
    heapq.heappush(nodes, node(chars[i],freq[i]))

while len(nodes)>1:
    left=heapq.heappop(nodes)
    right=heapq.heappop(nodes)
    left.huff=0
    right.huff=1
    newNode=node(left.symbol+right.symbol,left.freq+right.freq,left,right)
    heapq.heappush(nodes,newNode)

printNodes(nodes[0])