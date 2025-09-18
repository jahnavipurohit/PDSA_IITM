'''Given a 2-D matrix m where each cell m[i][j] contains some number of coins, find a path to collect maximum coins from cell (x1, y1) to cell (x2, y2) in matrix м where x2 >= x1 and y2 >= y1. You can only travel one step right or one step down in each move.
Write a function MaxCoinsPath(M,x1,y1,x1,y1) that accepts a matrix, index (x1,y1) of the source cell and index (x2,y2) of the destination cell in matrix M. The function should return the maximum number of coins collected across all paths from source to destination.
Sample Input
[[2,1,3,2,5], [3,5,2,4,6], [7,6,1,3,2], [2,9,4,7,8], [1,4,5,11,3]] # Matrix M
(0,0) #Source (x1,y1)
(4,4) #Destination (x2,y2)
Output
52
Explanation
2 + 3 + 7 + 6 + 9 + 4 + 7 + 11 + 3 = 52 which is maximum in all paths from (1,1) to (4,4).'''

def MaxCoinPath(M,x1,y1,x2,y2):
    MCP=[]
    # Create matrix same size of M and initialized with 0
    for i in range(len(M)):
        L = []
        for j in range(len(M[0])):
            L.append(0)
        MCP.append(L)
    # Initialize x1 row and y1 coloumn    
    MCP[x1][y1] = M[x1][y1]
    for i in range(y1+1,len(M[0])):
        MCP[x1][i]= MCP[x1][i-1] + M[x1][i]
    for i in range(x1+1,len(M)):
        MCP[i][y1]= MCP[i-1][y1] + M[i][y1]
	# calculate value for each cell
    for i in range(x1+1,len(M)):
        for j in range(y1+1,len(M[0])):
            MCP[i][j] = max(MCP[i-1][j],MCP[i][j-1]) + M[i][j]
    # return max coin value at x2,y2
    return MCP[x2][y2]
M = eval(input())
(x1,y1)=eval(input())
(x2,y2) = eval(input())
print(MaxCoinPath(M,x1,y1,x2,y2))