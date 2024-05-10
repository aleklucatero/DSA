'''
Given an array of integers nums and integer target, return indices
of the two numbers such that they add up to the target. You may
assume that each input have exactly one solution, and you may not use
the same element twice.

1. Conceptual understanding:
    I am reading a list (nums), and seeing what combination of two indices can add up to the target that is given.

2. Conceptual Solution:
    Example 1: [2, 7, 11, 15], T=9 => [0, 1]
    Example 2: [3, 2, 4], T=6 => [1, 2]

3. Pseudocode:
    a. Define a function that takes nums(array), and target (target value for addition)
        b. Initialize pointer (a) at 0
        d. Initialize Targetlist for answer []
        e. while the len of nums is > a
            f. iterate through nums using
                g. if nums[a] + num == target: 
                    h. push [a] & num into Targetlist
                i. else
                    j. a += 1
        k. return new list 
'''

#Code Attempt #1
# def findCombination(nums, target):
#     combination = []
#     a = 0
#     while len(nums) > a:
#         for num in nums:
#             if nums[a] + num == target:
#                 combination.append((a, num))
#             else:
#                 a += 1
#     return combination

# print(findCombination([2, 7, 11, 15], 9)) #Expected is [0, 1]
# print(findCombination([3, 2, 4], 6)) #Expected is [1, 2]

'''
3. Pseudocode:
    a. Define a function that takes nums(array), and target (target value for addition)
        b. Initialize combination list
        c. for outer loop that iterates through first indici (i)
            d. for inner loop that iterates through second indice, starts at first indici + 1 (i + j)
                e. if nums[i] + nums[j] == target:
                    f. append([i, j])
        return combination
'''

#Code Attempt #2 - IT WORKS BUT NOT EFFICIENT
#Time complexity is O(n^2) - Since there are 2 indicis/combinations that are going through array. (Inner loop)
# def findCombination(nums, target):
#     combination = []
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 combination.append(i)
#                 combination.append(j)
#     return combination

# print(findCombination([2, 7, 11, 15], 9)) #Expected is [0, 1]
# print(findCombination([3, 2, 4], 6)) #Expected is [1, 2]

#Code Attempt #3 - MAKING IT EFFICIENT using hashmap
def findCombination(nums, target):
    hashMap = {}
    for i in range(len(nums)):
        if nums[i] in hashMap:
            return [hashMap[nums[i]], i]
        else:
            difference = target - nums[i]
            hashMap[difference] = i
    return []

print(findCombination([2, 7, 11, 15], 9))
print(findCombination([3, 2, 4], 6))




