class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)

        for i in range(len(ratings)):
            if i > 0 and ratings[i] > ratings[i-1]:
                candies[i] = 1+candies[i-1]
        print(candies)

        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)

        return sum(candies)