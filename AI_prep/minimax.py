import numpy as np 
import math
players=['x','o']


board=[[' 'for _ in range(3)]for _ in range(3)]


def check_winner(player):
    for i in range(3):
        if all(board[i][j]==player for j in range(3)):return True
        if all(board[j][i]==player for j in range(3)):return True
    if all(board[i][i]==player for i in range(3)):return True
    if all(board[i][2-i]==player for i in range(3)):return True
    return False
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()


def check_board():
    for player in players:
        if check_winner(player):
            return player
    if all(board[i][j]!=' 'for i in range(3) for j in range(3)):
        return 'draw'
    return None

def mini_max(depth,is_maximizing,alpha,beta):
    winner=check_board()

    if winner=='o':
        return 10-depth
    if winner=='x':
        return depth-10
    elif winner=='draw':
        return 0
    
    if is_maximizing:
        best_score=-math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j]==' ':
                    board[i][j]='o'
                    score=mini_max(depth+1,False,alpha,beta)
                    board[i][j]=' '
                    best_score=max(best_score,score)
                    alpha=max(alpha,best_score)
                    if beta<=alpha:
                        return best_score
        return best_score
                    
    else:
        best_score=math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j]==' ':
                    board[i][j]='x'
                    score=mini_max(depth+1,True,alpha,beta)
                    board[i][j]=' '
                    best_score=min(best_score,score)
                    beta=min(beta,best_score)
                    if beta<=alpha:
                        return best_score

        return best_score
    

def best_move():
    best_score=-math.inf
    move=(-1,-1)

    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                board[i][j]='o'
                score=mini_max(0,False,-math.inf,math.inf)
                board[i][j]=' '
                if score>best_score:
                    best_score=score
                    move=(i,j)
    return move



def play_game():
    print_board(board)
    turn=0

    while True:
        if turn%2==0:
            print("Your turn (X)")
            while True:
                r,c=map(int,input("enter row,col").split())
                if board[r][c]==' ':
                    board[r][c]='x'
                    break
                else:
                    print("occupied")
                
        else:
            print("AI's turn")
            r,c=best_move()
            board[r][c]='o'

        print_board(board)
        winner=check_board()

        if winner:
            if winner=="draw":
                print("its a draw")
            else:
                print(f"{winner} wins")
            break
        turn+=1


play_game()




