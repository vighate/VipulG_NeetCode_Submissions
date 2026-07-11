class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = []

        for i in range(len(temperatures)):
            val1 = temperatures[i]
            print(val1)
            for j in range(i+1, len(temperatures)):

                if val1 < temperatures[j]:
                    res.append(j-i)
                    break
            else:
                res.append(0)
        return res

                