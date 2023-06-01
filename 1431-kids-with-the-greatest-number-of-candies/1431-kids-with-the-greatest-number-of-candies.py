class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        # n kins with candies
        # candies integer array
        # extra candies integer
        # boolean response
        response = []
        for i in candies:
            new_amout = i + extraCandies
            if max(candies) <= new_amout:
                 response.append(True)
            else:
                 response.append(False)
        
        return response
