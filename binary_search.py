# ------Binary Search------
# **** Required : Input is a sorted list.
#
# If an element you look for in the list, binary search returns the position where it is located.
# Otherwise, it will return null.
#
# Steps
# 1. Start with 50 out of 100
# 2. If num > 50 => get the second half of the array. Else get the first half of array.
# If num == guessed num, return the guessed num position.
# 3. Continue the process until getting all the position.
#
# Good: Take very few steps in Binary Search, for example it takes 240000 steps for Simple Search if you are looking for the last word.
# But using Binary Search, it takes only 18 steps in total.
#
# Big O Notation:
# Binary Search : O(log2n)
# Simple Search : O(n)

def binary_search(sorted_list,num):
    # start the search
    low = 0
    high = len(sorted_list) - 1
    # while havent narrow to one element
    while low <= high:
        # find mid point like low = 0 , high = 7 => 7+0 > 3
        mid = (high + low) // 2
        guessed = sorted_list[mid]
        if guessed == num:
            return mid
        elif guessed > num:
            # move to the lower array half
            high = mid - 1
        elif guessed < num:
            # move to the higher array half
            low = mid + 1
    return None

assert (binary_search([1,2,3,4,5,6,7,9],3)) == 2, "Should Be At Position 2"
assert (binary_search([1,2,3,7,9],5)) == None, "Should Be None"
assert (binary_search([1,2,3,4,5,6,7,9],9)) == 7, "Should Be At Position 7"
