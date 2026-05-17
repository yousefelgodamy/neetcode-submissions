class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        queue = deque()
        visited = set()

        node_map = defaultdict(list) # node to list of neighbors
        for edge in edges:
            node_map[edge[0]].append(edge[1])
            node_map[edge[1]].append(edge[0])

        nodes = list(node_map.keys())
        queue.append(nodes[0])
        visited.add(nodes[0])
        
        while len(queue) > 0:
            curr_node = queue.popleft()
            neighbors = node_map[curr_node]
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    node_map[neighbor].remove(curr_node)
                else:
                    return False
        if len(visited) != n:
            return False

        return True