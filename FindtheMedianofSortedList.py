class Solution:
   def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
     #Merge the given lists.
     nums1.extend(nums2)
  
  
     #Now sort the merged list.
     nums1.sort()
  
  
     #Find the middle element of the sorted list.
     mid = len(nums1)//2
  
  
     #If the length of the sorted list is even :
     if len(nums1)%2 == 0:
         return (nums1[mid-1]+nums1[mid])/2

     #If the length of the sorted list is odd :
     else:
         return nums1[mid]
