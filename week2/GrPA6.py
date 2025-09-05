'''You have given a list of distinct integers ranging from 1 to n in increasing order. There is one number missing in list L. Find the missing number in the list L.

Note: The worst case running time of your program should be: O(log n)

Implement the function missing_number(L) that takes list L and returns the missing number.

Sample Input 1
[1, 2, 4, 5, 6]
Output 1
3

Sample Input 2
[1, 2, 3, 4, 6]
Output 2
5'''

def missing_number(L):
    # Edge cases
    size = len(L)
    if L[0] != 1:
        return 1
    if L[size - 1] != (size + 1):
        return size + 1
    left = 0
    right = size - 1
    mid = 0
    while right > left + 1:
        mid = (left + right) // 2
        if (L[left] - left) != (L[mid] - mid):
            right = mid
        elif (L[right] - right) != (L[mid] - mid):
            left = mid
    return L[left] + 1