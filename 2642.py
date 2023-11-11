class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.list = {i: [] for i in range(n)}
        for edge in edges:
            self.list[edge[0]].append((edge[1], edge[2]))

    def addEdge(self, edge: List[int]) -> None:
        self.list[edge[0]].append((edge[1],edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0,node1)]
        dist = {i: float('inf') for i in range (len(self.list))}
        dist[node1] = 0

        while heap:
            (d,node) = heapq.heappop(heap)
            if node == node2:
                return d
            if d>dist[node]:
                continue
            for neighbor, cost in self.list[node]:
                new = d + cost
                if new < dist[neighbor]:
                    dist[neighbor] = new
                    heapq.heappush(heap, (new,neighbor))
        return -1
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
