class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = []
        count = 0
        for i in nums :
            if i == 1 :
                count += 1
            else :
                l.append(count)
                count = 0
        l.append(count)
        return max(l)
        