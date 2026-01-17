board = [" " for _ in range(9)]
def print_board():
    print(board[0] ,  "|" , board[1] ,  "|" , board[2])
    print("____ ____ ___")
    print(board[3] ,  "|" , board[4] ,  "|" , board[5])
    print("____ ____ ___")
    print(board[6] ,  "|" , board[7] ,  "|" , board[8])
    
    
    
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]           
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False    

current_player = "X"
game_running = True
print_board()
while game_running:
    move = int(input(f"Player {current_player}, enter your move (0-8): ")) 
    if board[move] == " ":
        board[move] = current_player
        print_board()
        if check_winner(current_player):
            print(f"Player {current_player} wins!")
            game_running = False
        elif " " not in board:
            print("It's a tie!")
            game_running = False
        else:
            current_player = "O" if current_player == "X" else "X"
    else:
        print("position has been taken ,try again")
        