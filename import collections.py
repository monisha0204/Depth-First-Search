import collections
# DFS algorithm with loop, without recursion
def dfs(graph,root):
    visited=set()
    visited.add(root)
    stack=collections.deque([root])
    while stack:
        #print(stack)
        # Dequeue a vertex from queue
        vertex=stack.pop()
        print(vertex)
        # If not visited,mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)
if __name__ == '__main__':
    graph1={0:[1,2,3], 1:[0,2], 2:[0,1,4], 3:[0], 4:[2]}
    graph2={0:[1,4], 1:[0,2,3,4], 2:[1,3], 3:[1,2,4], 4:[0,1,3]}
    graph,root=graph1, 0
    print(F"Graph Adjancey List: \n {graph} \n")
    print(F"Following is Depth First Traversal From {root}:")
    dfs(graph,root)