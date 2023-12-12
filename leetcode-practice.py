# Problem 1
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# https://leetcode.com/problems/two-sum/description/ 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]




# Problem 1160
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/?envType=daily-question&envId=2023-12-02 

# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once).
# Return the sum of lengths of all good strings in words.

# Example 1:
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # create var to store good words
        # loop through each word in array 
        # for each word in array, loop thru each character in the word and check if that char is in chars. 
            # if char in chars, pop it off
            # if char not in chars, move to next word in array
        # get length of each word in good words list 
        # add together lengths
        # return sum
        good_words = []
        
        for word in words: 
            char_list = list(chars) #[a t a c h]
            new_word = ""
            for char in word: # c
                if char in char_list: 
                    i = char_list.index(char)
                    char_list.pop(i) 
                    new_word += char
                if word == new_word:
                    good_words.append(new_word)
        
        print(good_words)
        sum_of_lengths = 0
        for word in good_words:
            sum_of_lengths += len(word)

        return sum_of_lengths





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