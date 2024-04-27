'''
Given an integer array nums and an integer val, remove all occurrences of val 
in nums in-place. The order of the elements may be changed. Then return the 
number of elements in nums which are not equal to val.

1. Conceptual understanding:
Given a list of nums, Iterate through the list looking for a specific value to 
delete. Keep the values in the same array, just delete the nums that equal
the value. Print out the length of the final array, as well as the array

2. Conceptual Solution:
    Example 1: nums = [3,2,2,3], val = 3 => 2, nums = [2,2,_,_]
    Example 2: nums = [0,1,2,2,3,0,4,2], val = 2 => 5, nums = [0,1,4,0,3,_,_,_]

3. Pseudocode:
    a. Define function that takes nums, var as parameter.
        b. Iterate through list
            c. if a number == value
                d. remove that number
            e. else
                f. continue 
        g. return num.len + ", nums =" + nums

'''

#Code Attempt 1:
def removeElement(nums, val):

    for num in nums:
        if num == val:
            nums.remove(num)
        else:
            continue
    return len(nums), "nums =", nums

print(removeElement([3,2,2,3], 3))
