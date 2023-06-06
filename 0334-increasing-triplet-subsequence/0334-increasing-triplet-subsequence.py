class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # if i < j < k 
        min_value = float('inf')
        mid_value = float('inf')

        for num in nums:
            if num <= min_value:
                min_value = num
            elif num <= mid_value:
                mid_value = num
            else:
                return True

        return False