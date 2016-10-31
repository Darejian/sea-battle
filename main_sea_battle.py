print "Welcome to Sea Battle Game"

#MAIN VARIABLES
boardPlayer1 = []
boardPlayer2 = []

empty_cell = 0 #value which marks cell as empty
board_size = 10 #size of the board (size x size)
deckShips = [4,3,2,1] #decks which ships can consist of
numberOfShipsPerDeck = [1,2,3,4] # number of ships allowed for appropriate deck (matches with deck array)

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
def set_ships_manually(board,deck,numberOfShips):
    print("Place a ship")
    for j in range(len(deck)):
        for n in range(numberOfShips[j]):
            TopRow = int(input("Top row: "))
            LeftCol = int(input("Left column: "))
            sOrientation = raw_input("Orientation: h - horizontal, v - vertical: ")
            if sOrientation == 'h':
                for i in range(deck[j]): 
                    board[TopRow-1][LeftCol+i-1] = 1
            else:
                for i in range(deck[j]):
                    board[TopRow+i-1][LeftCol-1] = 1
            print_board(board)
    

#set ships automatically
#shoot

print("This is your board. Empty for now:")

create_board(boardPlayer1) 
print_board(boardPlayer1)
set_ships_manually(boardPlayer1,deckShips,numberOfShipsPerDeck)
clear_board(boardPlayer1)
