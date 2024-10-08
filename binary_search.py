import random
import time

# Implement binary search algorithm

# Prove that binary search is faster than naive search

# Naive search: Scan the entire list and ask if it is equal to the target
# If "yes", return the index
# If "no", then return -1

def naive_search(l, target):
    # Example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1 

# Binary search uses divide and conquer
# We will leverage the fact that our list is sorted
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1
    # example l = [1, 3, 5, 10, 12] # Should return 3
    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return target
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)


if __name__=="__main__":
    # l = [1, 3, 5, 10, 15]
    # target = 10
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    # Build a sorted list of length 10,000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print(f"Naive search time: {(end - start)/length} seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print(f"Binary search time: {(end - start)/length} seconds")