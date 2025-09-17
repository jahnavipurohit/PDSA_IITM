'''Maze solver
Alice wants to find the key in a maze and get out of it. 
The maze representation is given below, where x represents walls, space represents 
the allowed tiles Alice can walk on and * represents the tile that has the key.
There is only one tile opening in the left-most vertical wall, where Alice is initially standing.
Similarly there is only one tile opening in the right-most vertical wall, from which Alice has to exit.
Alice can travel horizontally or vertically, but cannot travel diagonally. 
Moving to adjacent tile vertically or horizontally is counted as a step.
There are three possible outcomes, either you can exit the maze after getting the key, 
or the key is not reachable or the finish tile is not reachable.
Print the minimum number of steps Alice requires to reach the finish tile traveling through 
tile having the key.
If the key tile is not reachable then print -1.
If the key tile is reachable but finish tile is not reachable then print -2.
Note: Input and printing are required'''


from collections import deque
import sys

def read_input():
    maze = []
    for line in sys.stdin:
        line = line.rstrip('\n')
        if line:  # ignore empty lines
            maze.append(list(line))
    n = len(maze)
    m = len(maze[0]) if n > 0 else 0
    return maze, n, m

def find_positions(maze, n, m):
    start = end = key = None

    for i in range(n):
        if not start and maze[i][0] == ' ':
            start = (i, 0)
        if not end and maze[i][m - 1] == ' ':
            end = (i, m - 1)

    for i in range(n):
        for j in range(m):
            if maze[i][j] == '*':
                key = (i, j)

    return start, key, end


def bfs(maze, n, m, start, target):
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    queue.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == target:
            return dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and (maze[nx][ny] == ' ' or maze[nx][ny] == '*'):
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
    return -1

def solve_maze():
    maze, n, m = read_input()
    start, key, end = find_positions(maze, n, m)

    if not start or not key or not end:
        print(-1)
        return

    dist1 = bfs(maze, n, m, start, key)
    if dist1 == -1:
        print(-1)
        return

    # Change key tile to space so second BFS can pass through it
    maze[key[0]][key[1]] = ' '

    dist2 = bfs(maze, n, m, key, end)
    if dist2 == -1:
        print(-2)
        return

    print(dist1 + dist2)

solve_maze()
