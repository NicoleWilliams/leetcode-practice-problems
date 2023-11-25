# Problem 2169
# https://leetcode.com/problems/count-operations-to-obtain-zero/description/
# You are given two non-negative integers num1 and num2.

# In one operation, if num1 >= num2, you must subtract num2 from num1, 
# otherwise subtract num1 from num2.

# For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining 
# num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5, after one operation, 
# num1 = 4 and num2 = 1.
# Return the number of operations required to make either num1 = 0 or num2 = 0.

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # create variable for count of operations
        # create a while loop
        # check if num1 >= num2, if yes num1 = num1 - num2 and add one to operation count. If no, num2 = num2 - num1 and add one to operation count. 
        # break while look if either num is equal to 0 and return operations count
        ops_count = 0
        while num1 != 0 and num2 !=0:
            if num1 >= num2:
                num1 = num1 - num2
                ops_count += 1
            else:
                num2 = num2 - num1
                ops_count += 1
            
        return int(ops_count)