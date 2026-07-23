from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand)%groupSize !=0:
            return False

        count = Counter(hand)

        for card in sorted(count):

            if count[card]>0:
                need = count[card]

                for nxt in range(card, card+groupSize):
                    if count[nxt] < need:
                        return False
                    count[nxt] -= need
        return True

















        if len(hand)%groupSize != 0:
            return False
        
        count = Counter(hand)

        for card in sorted(count):

            if count[card] > 0:
                need = count[card]

                for nxt in range(card, card+groupSize):
                    if count[nxt] < need:
                        return False
                    count[nxt]-=need
        return True