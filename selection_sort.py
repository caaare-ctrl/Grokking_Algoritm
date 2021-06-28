# ----------------  Selection Sort  ---------------------------
#
# Sort the list from most to least
# Go throught the list --------->
# 1 2 3 -------> 3
# 1 2 -------> 3 2
# 1 --------> 3 2 1 SORTED!
#
# Big O Notation
# touch every element once O(n) Simple Search * n times
# O(n^2)
#
# ** On average you need to check a list 1/2 * n, but constant is ignored in Big O notation

def selection_sort(unsort_list):
    sorted_list = []

    for i in range(len(unsort_list)):
        smallest_num = unsort_list[0]
        smallest_index = 0
        for j in range(1,len(unsort_list)):
            if unsort_list[j] < smallest_num:
                smallest_num = unsort_list[j]
                smallest_index = j
        sorted_list.append(unsort_list.pop(smallest_index))
    return sorted_list

print(selection_sort([4,3,2]))




