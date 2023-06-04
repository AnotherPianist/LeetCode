# class UnionFind:
#     def __init__(self, n):
#         self.disjoint_sets = list(range(n))

    
#     def union(self, i, j):
#         self.disjoint_sets[i] = j
    
    
#     def find(self, i):
#         if self.disjoint_sets[i] == i:
#             return i
#         else:
#             return self.find(self.disjoint_sets[i])


class QuickFind():
    def __init__(self, n):
        self.parents = list(range(n))
    

    def union(self, u, v):
        root_u, root_v = self.parents[u], self.parents[v]

        for i, node in enumerate(self.parents):
            if node == root_u:
                self.parents[i] = root_v

    
    def find(self, u):
        return self.parents[u]


    def connected(self, u, v):
        return self.parents[u] == self.parents[v]
    
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = QuickFind(n)
        
        number_connected_components = n
        
        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] == 1 and not uf.connected(i, j):
                    uf.union(i, j)
                    number_connected_components -= 1
        
        return number_connected_components