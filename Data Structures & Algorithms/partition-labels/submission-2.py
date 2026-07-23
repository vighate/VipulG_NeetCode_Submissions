from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        adj = {ch: i for i, ch in enumerate(s)}
        start = 0
        end = 0
        res = []
        for i, ch in enumerate(s):
            end = max(end, adj[ch])
            if i==end:
                res.append(end-start+1)
                start = i+1
        return res