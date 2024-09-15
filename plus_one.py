class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #You can use the "for in" loop to loop through all the elements of an array.
        n = len(digits)
        #variable to store the list and provide the length
        for i in range(n - 1, -1, -1):
            #The large integer does not contain any leading 0's.
            if digits[i] < 9:
                #both are counted as integers
                digits[i] += 1
                #if less than 9 it will add a space to the list 
                return digits
            
            digits[i] = 0
            #this will make it start at 0

        return [1] + digits
        #we need to insert a at the beginning of the array.
        # also ok: return [1] + [0]*n
