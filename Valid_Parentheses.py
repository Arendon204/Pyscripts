#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.



class Solution:
    def isValid(self, s: str) -> bool:
        #A stack is used to keep track of opening brackets.
        dict = {'(': ')', '[': ']', '{': '}'}
        stack = []

        # If it's an opening bracket, it is pushed onto the stack.
        # If it's a closing bracket, the function checks if the stack is empty or if the top of the stack
        for char in s:
            if char in dict.keys():
                stack.append(char)
            elif char in dict.values():
                if not stack or dict[stack.pop()] != char:
                    return False
                    #If it's a closing bracket, the function checks if the stack is empty or if the top of the stack doesn't match the corresponding opening bracket. If either condition is true, the function returns False.
        return not stack
        
        #After processing all characters, if the stack is empty, all brackets were matched correctly, and the function returns True. Otherwise, it returns False.
