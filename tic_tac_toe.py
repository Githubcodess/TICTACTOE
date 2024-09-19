def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)
        
def initialize_board():
    return[[' ' for _ in range(3)] for _ in range(3)]

def check_winner(board,player):
    for row in board:
        if row == [player,player,player]:
            return True
        
    for col in range(3):
        if[board[row][col] for row in range(3)]== [player, player,player]:
           return True
       
    if[board[i][i] for i in range (3)] == [player,player,player]:
        return True
    
    if [board[i][2-i] for i in range(3)] == [player,player,player]:
        return True
    
    return False  

def check_draw(board):
    return all (cell != ' ' for row in board for cell in row) 

def minimax(board , depth , is_maximizing):
    if check_winner(board , '0'):
        return 10-depth
    if check_winner(board ,'X'):
        return depth - 10
    if check_draw(board):
        return 0 
    
    if is_maximizing:
        best_score = float(-'inf')
        for row in range (3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = '0'
                    score = minimax (board, depth + 1, False) 
                    board[row][col] = ' '
                    best_score + max(score ,best_score)
            return best_score
        else:
            best_score = float ('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                      board[row][col] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
        return best_score 
     
def best_move(board):
    best_score  = float('-inf')
    move = None
    
    for row in range (3):
        for col in range (3):
            if board[row][col] == ' ':
                board[row][col] ='0'
                score = minimax(board , 0, False)
                board[row][col] = ' '
                if score > best_score:
                    best_score= score
                    move = (row, col)
    return move
                  
def tictactoe():
    board = initialize_board()
    print('welcome to Tic Tac Toe!')
    print_board(board)
    
    while True:
        human_move = tuple(map(int, input("Enter your move (row and column): ").split()))
        if board[human_move[0]][human_move[1]] == ' ':
            board[human_move[0]][human_move[1]] = 'X'
        else:
            print("Invalid move. Try again.")
            continue

        print_board(board)

        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        # AI's turn (O)
        print("AI's turn:")
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break

        if check_draw(board):
            print("It's a draw!")
            break

# Run the game 
tictactoe()

def minimax_alpha_beta(board, depth, is_maximizing, alpha, beta):
    # Terminal states (win/loss/draw)
    if check_winner(board, 'O'):
        return 10 - depth
    if check_winner(board, 'X'):
        return depth - 10
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax_alpha_beta(board, depth + 1, False, alpha, beta)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax_alpha_beta(board, depth + 1, True, alpha, beta)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score    
                                              