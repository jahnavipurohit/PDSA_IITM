'''Longest Decreasing Sequence
Longest Decreasing Sequence (LDS) is in which the value gets strictly decreasing over the sequence. 
For example, in [5, 4, 7, 1], [5, 4, 1] is a longest decreasing sequence.
Write a function LDS (L) to return a list of longest decreasing sequence. If more than one LDS 
is present in the list L then return any one of LDS.
Sample Input
L = [0, 2, 7, 3, 7, 3, 8, 2, 1, 0]
Sample Output
[7, 3, 2, 1, 0]'''

def LDS(L):
    n = len(L)
    LDSCount = [1]*n # LDS with respect to the index
    prev = [None]*n # previous value with respect to the index
    for i in range(n):
        preMax = L[0]
        for j in range(i):
            if L[j] > L[i] and LDSCount[j] > preMax:
                preMax, prev[i] = LDSCount[j], j
        LDSCount[i] = 1 + preMax # updating LDSCount
    mx = max(LDSCount) # count of LDS
    mxi = LDSCount.index(mx) # index of LDS

    # backtracking to get the sequence
    seq = []
    while mxi != None:
        seq.append(L[mxi])
        mxi = prev[mxi]
    return seq[::-1]