class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        fives = 0
        tens = 0
        flag = False

        for bill in bills:
            if bill==5:
                fives+=1
            elif bill==10:
                if fives == 0:
                    return False
                fives-=1
                tens+=1
            else:
                if tens>0 and fives>0:
                    tens-=1
                    fives-=1
                elif fives>=3:
                    fives-=3
                else:
                    return False
        return True














        
        five = 0
        ten = 0

        for bill in bills:

            if bill == 5:
                five += 1
            
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True

        