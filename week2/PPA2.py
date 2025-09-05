'''Consider a list L containing n integers, where each integer i is in the range [0, r) 
that is 0 <= ir, r < 1000 and n>>r (n is much greater than r). 
Write a Python function sortInRange (L, r) to sort the list L in ascending order. 
Try to write a solution that runs in O(n + r) asymptotic complexity.
Sample Input:
L: 2, 0, 1, 1, 2, 3, 0, 2, 1, 0, 2, 3, 1, 2
r: 4
Sample Output:
0,0,0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3'''

def sortInRange(L, r):
    # Create a counting array initialized to zeros.
    # The size of the counting array should be 'r' because integers are in [0, r).
    counts = [0] * r

    # Populate the counting array: count occurrences of each integer in L.
    # This loop runs 'n' times, where 'n' is the length of L.
    for x in L:
        counts[x] += 1

    # Reconstruct the sorted list L based on the counts.
    # This part iterates through the 'counts' array (r times) and then places
    # elements back into L (n times in total across all inner loops).
    index = 0
    for i in range(r):
        while counts[i] > 0:
            L[index] = i
            index += 1
            counts[i] -= 1
            
            
            