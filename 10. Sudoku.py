grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]
def possible(r, c, num):
    global grid
    for i in range(0, 9):
        if grid[r][i] == num:
            return False
        
    for i in range(0, 9):
        if grid[i][c] == num:
            return False

    x0 = (c // 3) * 3
    y0 = (r // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0+i][x0+j] == num:
                return False
    return True

def solve():
    global grid
    for r in range(0, 9):
        for c in range(0, 9):
            if grid[r][c] == 0:
                for num in range(1, 10):
                    if possible(r, c, num):
                        grid[r][c] = num
                        if solve(): 
                            return True
                        grid[r][c] = 0
                return False  
    for i in range(len(grid)):
        print(grid[i][:])
    return True

solve()
