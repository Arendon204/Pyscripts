#Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
#add 11 and 1, 1 + 1 = 0, you get a carry on of 1, add 1 + 1 =  0, carry the one and youll get 100
# Output: "100"


class Solution:
    def addBinary(self, a: str, b: str) -> str: 
        #return the result in string form and a variable for the carry
        res = ""

        carry = 0

        #adding number together like 123456, its starting at the end, so we re reversing our input strings to compute the digits in order
        a, b = a[::-1], b[::-1]

        #a and b are not the same size so we re going to keep interating through
        #the one with the longer string is the one we will be interating through
        #its possible with the loop the string could be out of bounce

        for i in range(max(len(a), len(b))):
            #i is going for the longer string by reaching the end of string a/ b
            #get the a in bounds, if out of bounds default to 0
            #how can we convert these to digits?
            #use ord to get the ascii value, convert to integer, then subtract that from the ascii value of zero
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            #do the exact same thing - b at the position in bounds, if not in bounds defualt to the value of zero
            #you want the actual integer not the character interating through the string of b of i a of i are both characters
            #how can we convert these to the digits? Get the ascii value in python in the function 'ord' we can get the ascii value, but we dont want the ascii value
            #we want to convert the integer so we can take the ascii value and subtract from the ascii value of zero 
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0
            #we re going to sum them together into a total 
            total = digitA + digitB + carry
            #what character are we adding to our result string?
            #we re modding 'total' by 2 
            char = str(total % 2)
            #what if our total was 2?
            #whats the digit we would want to add in that case we d want to add? 
            #A zero and then change our carry to a one
            #what if this was a 3? the carry would also be one thats why we re modding by 2 because it works
            #modding by 2 end it right

            #we re converting our integer to a string 
            #we can adding the beginning of the results to after, dont forget to add the carry!
            res = char + res
            #we re going to take the total and divid by 2 and not mod it by 2 because if the total is equal to 2 then we have to carry a one then the total = 3
            #and also have to carry one.
            #if its equal to one then we do not have a carry which is why we re dividing by two 
            #once its done executing its guarantee to go through every digit in both strings
            carry = total // 2 
            #its possible at the end of this loop our carry could be equal to zero, but it could also be equal to one
        
        #we want to add one more if statement 
        #if the carry is non-zero then what are we going to do then we re going to take our result and add a one to the beginning of the result 
        #theres no more logic to handle only to return the resul string
        if carry:
            res = "1" + res
        return res