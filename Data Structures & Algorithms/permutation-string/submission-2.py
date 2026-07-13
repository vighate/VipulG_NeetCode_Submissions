from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        n = len(s1)
        m = len(s2)

        s1_counter = Counter(s1)

        window_counter = Counter(s2[:n])

        if window_counter == s1_counter:
            return True
        
        for i in range(n,m):

            window_counter[s2[i]] += 1
            window_counter[s2[i-n]] -= 1

            if window_counter[s2[i-n]] == 0:
                del window_counter[s2[i-n]]

            if window_counter == s1_counter:
                return True


        return False

        # if len(s1) > len(s2):
        #     return False

        # s1_counter = Counter(s1)
        # print(s1_counter)

        # n = len(s1)
        # m = len(s2)

        # window_counter = Counter(s2[:n])
        # print(window_counter)

        # if window_counter == s1_counter:
        #     return True

        # for i in range(n,m):
        #     window_counter[s2[i]] += 1
        #     window_counter[s2[i-n]] -= 1

        #     if window_counter[s2[i-n]] == 0:
        #         del window_counter[s2[i-n]]

        #     if window_counter == s1_counter:
        #         return True

        # return False