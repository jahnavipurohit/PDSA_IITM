'''Write a Python function kthLargest(arr, k) that accepts a list arr of integers of size n 
and an integer k, such that k < = n and returns the kth largest integer in arr. 
The solution should run in O(n) time.'''

import random

def _partition(arr, left, right):
    """
    This is a helper function that partitions the array around a pivot element.
    It's the core of the Quickselect algorithm, similar to the partition step in Quicksort.
    It returns the final index of the pivot.
    """
    # Choose a random pivot to avoid worst-case scenarios on sorted data.
    pivot_index = random.randint(left, right)
    pivot_value = arr[pivot_index]
    
    # Move the pivot to the end of the sub-array
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    
    store_index = left
    for i in range(left, right):
        # We're looking for the kth *largest*, so we want to partition
        # with larger numbers to the left.
        if arr[i] > pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
            
    # Move the pivot to its final sorted position
    arr[right], arr[store_index] = arr[store_index], arr[right]
    
    return store_index

def kthLargest(arr, k):
    """
    Finds the kth largest element in an unsorted list of integers.

    This function uses the Quickselect algorithm, which has an average-case
    time complexity of O(n), where n is the size of the list.

    Args:
        arr (list): A list of integers.
        k (int): An integer representing the rank of the element to find.
                 k must be between 1 and the size of the list.

    Returns:
        int: The kth largest element in the list.
    """
    if not arr or k < 1 or k > len(arr):
        raise ValueError("Invalid input: array must not be empty and k must be within bounds.")
    
    arr_copy = list(arr)  # Work on a copy to avoid modifying the original list
    left, right = 0, len(arr_copy) - 1
    
    # We are looking for the element at index k-1 from the end
    # of a sorted array (in descending order), which is equivalent to
    # the element at index k-1 from the beginning of a sorted array.
    target_index = k - 1
    
    while left <= right:
        pivot_index = _partition(arr_copy, left, right)
        
        if pivot_index == target_index:
            # We found the kth largest element at its correct position
            return arr_copy[pivot_index]
        elif pivot_index > target_index:
            # The element is in the left partition (numbers larger than the pivot)
            right = pivot_index - 1
        else:
            # The element is in the right partition (numbers smaller than the pivot)
            left = pivot_index + 1


arr=[int(item) for item in input().split(" ")]
k=int(input())
print(kthLargest(arr, k))