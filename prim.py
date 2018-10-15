import math
import heapq as hq

def prim(G):
    n = len(G)
    visited = [False]*n
    parents = [-1]*n
    dist = [999999]*n
    queue = []
    hq.heappush(queue, (0, 0))
    dist[0] = 0
    while len(queue) > 0:
        d, u = hq.heappop(queue)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in G[u]:
            if not visited[v] and w < dist[v]:
                dist[v] = w
                parents[v] = u
                hq.heappush(queue, (w, v))
            
    return parents, dist

G = ([(1, 2), (2, 3), (4, 6)],
    [(0, 2), (4, 2), (5, 3)],
    [(0, 3), (4, 1), (3, 5)],
    [(2, 5), (4, 5), (5, 6)],
    [(0, 6), (1, 2), (2, 1), (3, 5), (5, 4)],
    [(1, 3), (3, 6), (4, 4)])

p, d = prim(G)
print(p)
print(d)
                