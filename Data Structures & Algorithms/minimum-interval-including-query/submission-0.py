class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        res = []

    
        for i in range(len(queries)):
            
            min_len = float('inf')

            for start, end in intervals:
                if start <= queries[i] <= end:
                    min_len = min(min_len, end-start+1)
                
                
            if min_len == float('inf'):
                res.append(-1)
            else:
                res.append(min_len)

        return res

