class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [-1 for i in range(len(edges)+1)]
        edge = []

        def find(a):
            if parent[a] < 0:
                return a
            return find(parent[a])

        def union(a,b):
            parenta, parentb = find(a), find(b)
            if parenta == parentb:
                edge.append(a) 
                edge.append(b)
                return
            if parent[parenta] <= parent[parentb]:
                #parent a is bigger, add b to a
                parent[parenta] += parent[parentb]
                parent[parentb] = parenta
            else:
                parent[parentb] += parent[parenta]
                parent[parenta] = parentb
        
        for start,end in edges:
            union(start,end)
        
        return edge
