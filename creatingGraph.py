from collections import defaultdict
from collections import deque
import heapq

def addEdge(graph_elements,vertex,node):
      graph_elements[vertex].append(node)
def bfs(graph_elements,start,visited):

    queue=deque()
    queue.append(start)
    traversal=[]
    visited[start]=1
    while(len(queue)!=0):
       hold=queue.popleft()
       traversal.append(hold)
       for i in graph_elements[hold]:
           if(visited[i]==0):
             queue.append(i)
             visited[i]=1
    return traversal
def dfs(graph_elements,start,visited,traversal):
    if(start is None):
       return
    print(start)
    traversal.append(start)
    visited[start]=1
    for i in graph_elements[start]:
        if(visited[i]==0):
          dfs(graph_elements,i,visited,traversal)

    return
def dk(graph_elements,start,visited):
    dt={vertex:999 for vertex in graph_elements}
    dt[start]=0
    pq=[[0,start]]

    while(len(pq)!=0):
       heapq.heapify(pq)
       d,v=heapq.heappop(pq)
       if(visited[v]==1):
          continue
       visited[v]=1 #we cannot change the value of those elements which are being popped out
       for node,weight in graph_elements[v].items():
         if(visited[node]==0):
               dt[node]=min(dt[node],dt[v]+weight)
               pq.append([dt[node],node])
    return dt

graph_elements=defaultdict(list)
graph_elements = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

#visited={"a":0,"b":0,"c":0,"d":0,"e":0}
#print(bfs(graph_elements,"a",visited))
visited={"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
#print(dfs(graph_elements,"a",visited,[]))
print(dk(graph_elements,"U",visited))