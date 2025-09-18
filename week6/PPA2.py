'''Function heapSort(arr) sorts the array arr using max heap. 
Complete the function heapify(arr, n, i), that takes three arguments, arr is the max heap array, 
n is the number of elements in heap arr and i is the index of element that needs to be heapified 
and heapifies the array from index 0 to n-1 with respect to element at index i.'''

def heapify(arr, n, i):
    """
    Heapifies a subtree rooted at index i in a max-heap.
    Assumes that the children of i are already heapified.

    Args:
        arr: The max heap array.
        n: The number of elements in the heap array (current size of the heap).
        i: The index of the element that needs to be heapified.
    """
    largest = i  # Initialize largest as root
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # If left child exists and is greater than root
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # If right child exists and is greater than current largest
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    # We start from the last non-leaf node and go up to the root.
    # The last non-leaf node is at index (n//2 - 1).
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[i], arr[0] = arr[0], arr[i]
        # Call heapify on the reduced heap
        heapify(arr, i, 0) # 'i' is the new size of the heap for heapify
def heapSort(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

L = [int(item) for item in input().split(" ")]
heapSort(L)
print(*L)