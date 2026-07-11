class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        a1 = [0]*26
        a2 = [0]*26

        for ch in s:
            a1[ord(ch)-ord('a')] += 1
        for ch in t:
            a2[ord(ch)-ord('a')]+=1
        
        if a1 == a2:
            return True
        else:
            return False


        # d1 = {}

        # for char in s:
        #     if char in d1:
        #         d1[char]+=1
        #     else:
        #         d1[char]=1

        # d2 = {}

        # for char in t:
        #     if char in d2:
        #         d2[char]+=1
        #     else:
        #         d2[char]=1

        # print(d1)
        # print(d2)

        # if d1==d2:
        #     return True
        # return False

        
        