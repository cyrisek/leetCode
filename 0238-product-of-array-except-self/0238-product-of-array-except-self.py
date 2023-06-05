class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         # array nums 
        # return aanswer[i]
        n = len(nums)
        answer = [1] * n

        # Calculate the left values
        left_product = 1
        for i in range(n):
            answer[i] *= left_product
            left_product *= nums[i]

        # Calculate the right values
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer