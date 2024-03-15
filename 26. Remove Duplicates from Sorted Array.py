class Solution(object):
   def removeDuplicates(self, nums):
       """
       :type nums: List[int]
       :rtype: int
       """


       unique_nums = set()


       # Create a list to store non-duplicate numbers
       non_duplicate_nums = []


       # Iterate over the input list 'nums'
       for num in nums:
           if num not in unique_nums:
               unique_nums.add(num)  # Add the number to the set
               non_duplicate_nums.append(num)  # Append the number to the non-duplicate list


       # Modify the original 'nums' list with the non-duplicate elements
       nums[:] = non_duplicate_nums


       # Return the length of the modified list 'nums'
       return len(nums)


# Example usage:
solution = Solution()
nums = [3, 4, 5, 5, 3, 7, 8, 9, 9]
print(solution.removeDuplicates(nums))
print(nums)  # Output: [3, 4, 5, 7, 8, 9]