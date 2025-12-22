import numpy as np
x=30
y=30

def board_init(x,y):
    print("Board initialized")
    BOARD = np.zeros((2*x, 2*y))
    for i in range(2*x):
        for j in range(2*y):
            if i%2==0 and j%2==0:
                BOARD[i][j] = 1
            if i%2==1 and j%2==1:
                BOARD[i][j] = 1
            if i>(3*np.sqrt(3)/2)*x*y or j>(3*np.sqrt(3)/2)*x*y:
                BOARD[i][j] = -1
    return BOARD

board = board_init(x,y)

print(board)