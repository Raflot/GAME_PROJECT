import numpy as np
import matplotlib.pyplot as plt
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
            if i+j<2*x/3:
                BOARD[i][j] = -1
            if i+j>2*(y+2*x/3):
                BOARD[i][j] = -1
            if j-i>2*(2*x/3):
                BOARD[i][j] = -1
            if i-j>2*(2*x/3):
                BOARD[i][j] = -1
    return BOARD

board = board_init(x,y)
for i in range(2*x):
    for j in range(2*y):
        if board[i][j]==1:
            plt.scatter(j, i, c='black', s=200,marker='h',edgecolors='white')
#plt.imshow(board, cmap='gray', interpolation='nearest', )
plt.show()

print(board)