class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}

        for s in strs:

            count = [0]*26

            res = []
            for char in s:
                #print(s)
                count[ord(char) - ord('a')] += 1
                #print(count)
                res.append(count)

            key = tuple(count)
            print(key)

            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]

        return list(d.values())