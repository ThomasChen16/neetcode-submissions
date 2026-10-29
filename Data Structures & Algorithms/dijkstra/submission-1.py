import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # n = number of vertices 
        # edges = [starting vector(u), destination vector(v), weight(w)]
        # src = where to start the algorithm from

        # Create adjacency list to represent the graph
        adj = {}

        # Populate adjacency list with [] for number of vertices
        for i in range(n):
            adj[i] = []
        
        # Add edges to adjacency list
        for u, v, w in edges:
            adj[u].append((v, w))

        # Initialize every vertex's distance to infinity
        dist = {}

        for i in range(n):
            dist[i] = float('inf')
        dist[src] = 0

        minHeap = [(0, src)] # (distance, vertex)
        
        # Loop until minHeap is empty
        while minHeap:
            # Pop out the smallest current distance from src to vector u
            current_dist, u = heapq.heappop(minHeap)

            # Loop through the neighbors of starting vector
            for v, w in adj[u]:
                # new_dist is current_dist holding smallest dict + weight connecting u to neighbor v
                new_dist = current_dist + w
                
                # if new_dist is smaller than current dist in neighbor v update
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(minHeap, (new_dist, v))
        
        # Loop to see if any dist still inf meaning it was unreachable from src
        for i in range(n):
            if dist[i] == float("inf"):
                dist[i] = -1
        
        return dist

