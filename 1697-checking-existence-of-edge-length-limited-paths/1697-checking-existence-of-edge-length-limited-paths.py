class UnionFind:
    def __init__(self, size):
        self.group = [0] * size
        self.rank = [0] * size
        
        for i in range(size):
            self.group[i] = i
            
    
    def find(self, node: int):
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]
    
    
    def join(self, node1, node2):
        group1 = self.find(node1)
        group2 = self.find(node2)
        
        if group1 == group2:
            return
        
        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1
            
    
    def are_connected(self, node1, node2):
        return self.find(node1) == self.find(node2)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        queries_count = len(queries)
        answer = [False] * queries_count
        
        queries_with_index = [[] for _ in range(queries_count)]
        
        for i in range(queries_count):
            queries_with_index[i] = queries[i]
            queries_with_index[i].append(i)
        
        edgeList.sort(key=lambda x: x[2])
        queries_with_index.sort(key=lambda x: x[2])
        
        edges_index = 0
        
        for p, q, limit, query_original_index in queries_with_index:
            while edges_index < len(edgeList) and edgeList[edges_index][2] < limit:
                node1 = edgeList[edges_index][0]
                node2 = edgeList[edges_index][1]
                uf.join(node1, node2)
                edges_index += 1
            
            answer[query_original_index] = uf.are_connected(p, q)
        
        return answer