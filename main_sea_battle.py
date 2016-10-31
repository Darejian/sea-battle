print "Welcome to Sea Battle Game"

#MAIN VARIABLES
boardPlayer1 = []
boardPlayer2 = []

empty_cell = 0 #value which marks cell as empty
board_size = 10 #size of the board (size x size)

#FUNCTIONS

#create board
def create_board(board):
    for row in range(board_size): 
        board.append([]) 
        for column in range(board_size): 
            board[row].append(empty_cell) 

#print board
def print_board(board):
    for row in board:
        print(row)

#clear board from ships
def clear_board(board):
    for row in range(board_size):
        for column in range(board_size):
            board[row][column] = 0

#set ships manually
def set_ships_manually(board):
    print("Place a ship")
    deck = [4,3,2,1]
    for j in range(len(deck)):
        TopRow = int(input("Top row: "))
        LeftCol = int(input("Left column: "))
        sOrientation = raw_input("Orientation: h - horizontal, v - vertical: ")
        if sOrientation == 'h':
            for i in range(deck[j]): 
                board[TopRow-1][LeftCol+i-1] = 1
        else:
            for i in range(deck[j]):
                board[TopRow+i-1][LeftCol-1] = 1
        for row in board:
            print(row)
    

#set ships automatically

print("This is your board. Empty for now:")

create_board(boardPlayer1) 
print_board(boardPlayer1)
set_ships_manually(boardPlayer1)



#print("Now place your ships. Format: x y d")

#PLACE 4x SHIP





print_board(boardPlayer1)
clear_board(boardPlayer1)


'''
print("Place 4x ship")
print("Place 3x ship")
print("Place another 3x ship")
print("Place 2x ship")
print("Place another 2x ship")
print("Place another 2x ship")
print("Place 1x ship")
print("Place another 1x ship")
print("Place another 1x ship")
print("Place another 1x ship")
'''
