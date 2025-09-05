'''Binary search
Write a Python function binarySearchIndexAndComparisons(L, k) that accepts a list L 
sorted in ascending order and an integer k and returns a tuple (True/False, numComparisons). 
The first part of this tuple will be True if integer k is present in list L, False otherwise. 
The second part of the tuple is an integer which gives the number of elements in L 
that are actually compared to k while searching k in the list L using binary search.
For consistency use (left+right)//2 to calculate the middle index.
Example:
For given Land k, your function should return as mentioned in the table below.
L = [2, 6, 8, 11, 17, 23, 33, 44, 46, 50, 65] list is same for all examples below.
k - Return
11 - (True, 3)
23 - (True, 1)
100 - (False, 4)'''

def binarySearchIndexAndComparisons(L, k):
    left = 0
    right = len(L) - 1
    numComparisons = 0

    while left <= right:
        numComparisons += 1  # Each iteration involves one comparison (L[middle] == k)
        middle = (left + right) // 2

        if L[middle] == k:
            return (True, numComparisons)
        elif L[middle] < k:
            left = middle + 1
        else:  # L[middle] > k
            right = middle - 1

    return (False, numComparisons)