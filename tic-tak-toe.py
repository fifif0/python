from random import randrange

def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[0][0]+"   |   "+board[0][1]+"   |   "+board[0][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[1][0]+"   |   "+board[1][1]+"   |   "+board[1][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   "+board[2][0]+"   |   "+board[2][1]+"   |   "+board[2][2]+"   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    

def enter_move(board):
    while True:
        move=int(input("Pick number:"))

        if move<1 or move>9:
            print("Only number from 1 to 9")
            continue
        elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
            print("That square is already taken, choose other squrae ")
            continue

        for row in range(0,3):
            for column in range(0,3):
                if board[row][column] == str(move):
                    board[row][column] = 'O'
        break
  
def make_list_of_free_fields(board):
    
    global free_squares
    free_squares = [ ]

    for row in range(0,3):
        for column in range(0,3):
            if board[row][column] == "X" or board[row][column] == "O":
                pass
            else:
                free_squares.append(([row],[column]))

def victory_for(board, sign):

    if sign == "O":
        print("Human ->")
    else:
        print("Computer ->")       
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        return True
    #else:
    #  print("We do not have a winner yet")


def draw_move(board):
    while True:
        
        row = randrange(3)
        column = randrange(3)

        if ([row],[column]) not in free_squares:
            continue
        else:
            board[row][column] = 'X'
            return
        
board = [ ['1','2','3'], ['4','5','6'], ['7','8','9'] ]
numberOfMoves = 0
human = 'O'
computer = 'X'

display_board(board)
print()

while numberOfMoves<9:
    enter_move(board)
    numberOfMoves +=1
    display_board(board)

    if victory_for(board, human) == True:
        print("Human win")
        break
    else:
        make_list_of_free_fields(board)
        
        #display_board(board)

    print()
    draw_move(board)
    numberOfMoves +=1
    display_board(board)
    
    if victory_for(board, computer) == True:
        print("Computer win")
        break
    else:
        make_list_of_free_fields(board)
        print()
        #display_board(board)
else:
    print("End Game")

    
    
    
        
        

    


