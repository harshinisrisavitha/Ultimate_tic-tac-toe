# Ultimate Tic Tac Toe with Alpha-Beta Pruning AI
This project implements Ultimate Tic Tac Toe, an advanced variant of the classic game, powered by an AI using the Minimax algorithm with Alpha-Beta pruning to make optimal decisions.

## Game Rules
- The board is a 3×3 grid of 3×3 tic-tac-toe boards.
- A move in one small board determines the next board your opponent must play in.
- Win a small board by getting 3 in a row.
- Win the game by winning three small boards in a row on the big board.

## Heuristic Evaluation

- +100 if the AI wins the big board.
- −100 if the human wins the big board.
- +10 for each small board the AI wins.
- −10 for each small board the human wins.

## Code Structure

## SmallBoard Class

- Handles a 3x3 tic-tac-toe board:
- check_winner(): Determines winner of the board.
- make_move(): Executes a move and checks for a win.
- empty_cells(): Returns list of available moves.
- display(): Prints the board.

## UltimateBoard Class

- Handles the 3x3 grid of SmallBoard:
- make_move(br, bc, sr, sc, player): Makes a move.
- check_winner(): Checks the big board for a winner.
- evaluate(): Heuristic evaluation for AI scoring.
- minimax(depth, alpha, beta, is_maximizing): AI decision-making algorithm.
- best_move(valid_boards): Finds the best possible move.
- valid_boards(last_sr, last_sc): Determines which small boards are playable.
- display(): Shows the full board beautifully.

## How to run the game
```sh
python3 project.py
