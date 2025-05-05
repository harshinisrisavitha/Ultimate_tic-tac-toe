import math

Player = 'X'
Player_AI = 'O'

class SmallBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]		#creating a 3x3 board 		
        self.winner = None

    def is_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def empty_cells(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']		#returns empty cells 

    def check_winner(self, player):			#check if the player won
        # Check rows and columns
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
               all(self.board[j][i] == player for j in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2-i] == player for i in range(3)):
            return True
        return False

    def make_move(self, row, col, player):	#checks if any moves causes win	
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            if self.check_winner(player):
                self.winner = player
            return True
        return False

    def display(self):		#displays the board
        for row in self.board:
            print(' | '.join(row))
            print('-' * 5)

class UltimateBoard:
    def __init__(self):
        self.board = [[SmallBoard() for _ in range(3)] for _ in range(3)]		#initialize 9 small boards
        self.big_board = [[' ' for _ in range(3)] for _ in range(3)]
        self.winner = None

    def make_move(self, br, bc, sr, sc, player):
        small_board = self.board[br][bc] 			#selecting the small board (user input)
        if small_board.make_move(sr, sc, player):
            if small_board.winner:
                self.big_board[br][bc] = small_board.winner
                if self.check_winner(player):
                    self.winner = player
            return True
        return False

    def check_winner(self, player):		#checks for winner in the big board
        for i in range(3):
            if all(self.big_board[i][j] == player for j in range(3)) or \
               all(self.big_board[j][i] == player for j in range(3)):
                return True
        if all(self.big_board[i][i] == player for i in range(3)) or \
           all(self.big_board[i][2-i] == player for i in range(3)):
            return True
        return False

    def is_full(self):		#checks if all boards are full
        return all(small_board.is_full() or small_board.winner is not None 
                   for row in self.board for small_board in row)

    def valid_boards(self, last_sr, last_sc):		#returns the valid board for the next move
        if last_sr == -1 or last_sc == -1: 
            return [(r, c) for r in range(3) for c in range(3) 
                    if not self.board[r][c].winner and not self.board[r][c].is_full()] #checks if the board has (a winner or if it is full)->if not then then returns that board
        
        target_board = self.board[last_sr][last_sc]
        if target_board.winner or target_board.is_full():		#If the conditions are true ->returns all other boards which are neither full nor have a winner 
            return [(r, c) for r in range(3) for c in range(3) 
                    if not self.board[r][c].winner and not self.board[r][c].is_full()]
        return [(last_sr, last_sc)]

    def evaluate(self):		#Helper to minimax (score the winner  big_board->(AI=100) (Player=-100) small_board->(AI=10)(player=-10)
        if self.check_winner(Player_AI):
            return 100
        if self.check_winner(Player):
            return -100
        
        score = 0
        # Evaluate small board 
        for r in range(3):
            for c in range(3):
                if self.big_board[r][c] == Player_AI:
                    score += 10
                elif self.big_board[r][c] == Player:
                    score -= 10
        return score

    def minimax(self, depth, alpha, beta, is_maximizing):			#is_maximizing (True->AI trying to max the score)(False->Player trying to min the score)
        if depth == 0 or self.winner or self.is_full():		#base case->if winner or is_full
            return self.evaluate()

        valid_boards = self.valid_boards(-1, -1)  #return the valid boards
        if is_maximizing:
            max_eval = -math.inf
            
            for br, bc in valid_boards:
                small_board = self.board[br][bc]
                for (sr, sc) in small_board.empty_cells():
                  
                    small_board.board[sr][sc] = Player_AI	
                    prev_winner = small_board.winner		
                    if small_board.check_winner(Player_AI):	#checks if the winner is AI->updates the small and big boards 
                        small_board.winner = Player_AI
                        self.big_board[br][bc] = Player_AI
                    
                    eval = self.minimax(depth-1, alpha, beta, False)	#checking for the oponnents next move
                    
                    # Undo move
                    small_board.board[sr][sc] = ' '		#backtracking the move
                    small_board.winner = prev_winner
                    self.big_board[br][bc] = ' ' if prev_winner is None else prev_winner
                    
                    max_eval = max(max_eval, eval)	#update max_eval & alpha
                    alpha = max(alpha, eval)
                    if beta <= alpha:		#break as the opponent would have a better counter to this move
                        break
            return max_eval		#return the best move possible
        else:
            min_eval = math.inf
            for br, bc in valid_boards:
                small_board = self.board[br][bc]
                for (sr, sc) in small_board.empty_cells():
                    # Simulate move
                    small_board.board[sr][sc] = Player
                    prev_winner = small_board.winner
                    if small_board.check_winner(Player):
                        small_board.winner = Player
                        self.big_board[br][bc] = Player
                    
                    eval = self.minimax(depth-1, alpha, beta, True)
                    
                    # Undo move
                    small_board.board[sr][sc] = ' '
                    small_board.winner = prev_winner
                    self.big_board[br][bc] = ' ' if prev_winner is None else prev_winner
                    
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval

    def best_move(self, valid_boards):
        best_val = -math.inf
        best_move = None
        for br, bc in valid_boards:
            small_board = self.board[br][bc]
            for (sr, sc) in small_board.empty_cells():
                
                small_board.board[sr][sc] = Player_AI
                prev_winner = small_board.winner
                if small_board.check_winner(Player_AI):
                    small_board.winner = Player_AI
                    self.big_board[br][bc] = Player_AI
                
                eval = self.minimax(3, -math.inf, math.inf, False)  # Depth 3 for performance increase the depth for better AI performance
                
                # backtrack
                small_board.board[sr][sc] = ' '
                small_board.winner = prev_winner
                self.big_board[br][bc] = ' ' if prev_winner is None else prev_winner
                
                if eval > best_val:
                    best_val = eval
                    best_move = (br, bc, sr, sc)
        return best_move		#returns the move with highest score

    def display(self):
        print("\nUltimate Board:")
        for big_row in range(3):
            for row in range(3):
                line = []
                for big_col in range(3):
                    line.append('|'.join(self.board[big_row][big_col].board[row]))
                print(' || '.join(line))
            if big_row < 2:
                print('=' * 23)

def play_ultimate_game():
    game = UltimateBoard()
    current_player = Player
    last_sr, last_sc = -1, -1	#initialsize the first move(track the last move)

    while not game.winner and not game.is_full():		#run until someone wins or the bosrd is full
        print(f"\nCurrent player: {current_player}")
        game.display()
        valid_boards = game.valid_boards(last_sr, last_sc)		#show the valid boards_based on the last moves
        print(f"Playable small boards: {valid_boards}")

        if current_player == Player:
         
            while True:
                try:
                    br, bc = map(int, input("Enter small board (row col): ").split())
                    if (br, bc) not in valid_boards:
                        print("Invalid board.")
                        continue
                    sr, sc = map(int, input("Enter cell (row col): ").split())
                    if not (0 <= sr < 3 and 0 <= sc < 3) or game.board[br][bc].board[sr][sc] != ' ':
                        print("Invalid cell.")
                        continue
                    break
                except:
                    print("Invalid input. Example: '0 1' for row 0, column 1")
        else:
            # AI move
            print("AI is thinking...")
            br, bc, sr, sc = game.best_move(valid_boards)
            print(f"AI chooses board ({br}, {bc}) and cell ({sr}, {sc})")

        if game.make_move(br, bc, sr, sc, current_player):
            last_sr, last_sc = sr, sc
            current_player = Player_AI if current_player == Player else Player
        else:
            print("Invalid move!")

    game.display()
    if game.winner:
        print(f" Player {game.winner} wins!")
    else:
        print("It's a draw!")

if __name__ == '__main__':
    play_ultimate_game()
