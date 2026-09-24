class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for i in nums:
            str1 = str(i)
            if len(str1) % 2 == 0:
                count += 1
        return count

obj = Solution()
print(obj.findNumbers([12,345,2,6,7896]))