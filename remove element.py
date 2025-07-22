# Method 1
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        for j in range(0,len(nums)):
            if nums[j] == val:
                j+=1
            else:
                nums[i] = nums[j]
                i+=1
        return i
# method 2
class Solution1(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count =0
        l = []
        for num in nums:
            if num != val:
                l.append(num)
        nums[:] = l
        return len(l)