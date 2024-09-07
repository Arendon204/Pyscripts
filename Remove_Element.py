class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Consider the number of elements in nums which are not equal to val be k
        k = 0

        # Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
        for x in nums:
            if x != val:
                # Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
                nums[k] = x
                k += 1
        return k
