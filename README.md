# Depth-First-Search
 DFS code
 DFS algorithm
 Starting from the source, select a neighbour and explore that path fully before coming back to select another neighbour.
 Use a Stack to keep track of paths/nodes to be explored. Explore last added node first.
 Add start node to the stack and a 'visited' list and repeat below:
 - Get current node by popping from top of stack and print as DFS path node.
 - Push all neighbours of current node to the stack, if not already visited(to avoid revisiting) and
 - also add those nodes to the visited list
 repeat until all the elements in stack are popped
