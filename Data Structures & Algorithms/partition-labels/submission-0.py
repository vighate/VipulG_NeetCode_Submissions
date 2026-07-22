class Solution:
    def partitionLabels(self, s: str) -> List[int]:
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