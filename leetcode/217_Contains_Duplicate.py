class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                return True
        return False


obj = Solution()
print(obj.containsDuplicate([1,2,3,1]))