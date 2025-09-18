'''Write a Python function KminGreaterThan(arr, k, num), that accepts an unsorted list arr,
two numbers k and num, returns True if the k th smallest element in the list arr is greater than 
or equal to num, otherwise returns False. Try to write a solution that runs in O(n log k) time.'''

import heapq

def KminGreaterThan(arr, k, num):
    """
    Checks if the k-th smallest element in an unsorted list arr is greater than or
    equal to num.

    Args:
        arr: The unsorted list of numbers.
        k: The k-th smallest element to find.
        num: The number to compare against.

    Returns:
        True if the k-th smallest element is greater than or equal to num,
        otherwise False.
    """
    if k <= 0:
        # k must be a positive integer
        return False
    
    # Use a min-heap to simulate a max-heap by storing negative values.
    # The heap will store the k smallest elements encountered so far.
    # The smallest element in this min-heap (most negative) will correspond
    # to the largest of the k smallest positive elements.
    max_heap_of_k_smallest = [] 

    for x in arr:
        if len(max_heap_of_k_smallest) < k:
            heapq.heappush(max_heap_of_k_smallest, -x) # Store negative to simulate max-heap
        else:
            # If current element x is smaller than the largest among the k smallest
            # (which is -heapq.nsmallest(1, max_heap_of_k_smallest)[0] or simply -max_heap_of_k_smallest[0] )
            # We want to keep the k smallest elements. If the current x is smaller than
            # the current k-th smallest (which is the root of our simulated max-heap),
            # we pop the largest and push the new smaller element.
            if -x > max_heap_of_k_smallest[0]: # If -x is greater, it means x is smaller (since we're comparing negatives)
                heapq.heapreplace(max_heap_of_k_smallest, -x)
    
    if len(max_heap_of_k_smallest) < k:
        # This case handles scenarios where the array has fewer than k elements.
        # The problem statement implies k <= len(arr).
        # If k is larger than the array length, the k-th smallest doesn't exist in the usual sense.
        # Returning False or raising an error would be options. For this problem,
        # let's assume valid k.
        return False # Or handle as per specific problem requirements

    # The k-th smallest element is the top of our simulated max-heap (after negating it back)
    k_th_smallest = -max_heap_of_k_smallest[0]
    
    return k_th_smallest >= num