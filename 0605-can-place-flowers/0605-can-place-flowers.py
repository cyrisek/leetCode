class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #flowerbed list of int
        # 0 means empty
        # 1 mean full?
        #n return true if 0 and if 1 return false
        # if 0 only adjecent with 0 or nothing can be planted
        count = 0
        for i, plot in enumerate(flowerbed):
            if plot == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1
            if count >= n:
                return True
        return False
