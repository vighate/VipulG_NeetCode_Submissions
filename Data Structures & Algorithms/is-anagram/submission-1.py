class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d1 = {}

        for char in s:
            if char in d1:
                d1[char]+=1
            else:
                d1[char]=1

        d2 = {}

        for char in t:
            if char in d2:
                d2[char]+=1
            else:
                d2[char]=1

        print(d1)
        print(d2)

        if d1==d2:
            return True
        return False

        
        