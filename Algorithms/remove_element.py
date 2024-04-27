'''
Given a list of numbers and a target value T, remove all 
occurences of T from the list and return the new list


1. Conceptual understanding:
    I am reading an existing list, and filtering out the T value. Then, I am making a new list with the values that don't include T.

2. Conceptual Solution:
    Example 1: [1, 2, 3, 3, 4, 5, 3, 6], T=3 => [1, 2, 4, 5, 6]
    Example 2: [1, 2, 3, 2, 3, 2, 4, 2], T=2 => [1, 3, 3, 4]

3. Pseudocode:
    a. Define a function that takes numbers, and value
        b. Make a new empty list
        c. Iterate/loop through the list
            d. if the current number == value passed
            e. continue (skip)
        f. else
            g. pass the current number into new empty list
            h. return new list
'''

#Code Attempt 1:
def filteredList(numbers, value):

    result = []
    for number in numbers:
        if number == value:
            continue
        else:
            result.append(number)
    return result

filteredList([1, 2, 3, 3, 4, 5, 3, 6], 3)