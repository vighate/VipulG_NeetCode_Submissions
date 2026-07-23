class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        adj = {ch:i for i,ch in enumerate(s)}
        start = end = 0
        res = []
        for i, ch in enumerate(s):
            end = max(end, adj[ch])
            if i == end:
                res.append(end-start+1)
                start = i+1
        return res



        l = {ch:i for i, ch in enumerate(s)}
        start = 0
        end = 0
        ans = []
        for i, ch in enumerate(s):
            end = max(end, l[ch])
            if i==end:
                ans.append(end-start+1)
                start = i+1

        return ans