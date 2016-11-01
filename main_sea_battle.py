print "Welcome to Sea Battle Game"

#MAIN VARIABLES
boardPlayer1 = [[],[]]
#temporary initiation for debug purposes
boardPlayer1 = [[1,0,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0,0],
                [1,0,0,1,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]]

boardPlayer2 = []

empty_cell = 0 #value which marks cell as empty
board_size = 10 #size of the board (size x size)
deckShips = [4,3,2,1] #decks which ships can consist of
numberOfShipsPerDeck = [1,2,3,4] # number of ships allowed for appropriate deck (matches with deck array)
willShoot = "y" #does player want to shoot (y -yes, otherwise no)

#FUNCTIONS

#create board
def create_board(board):
    for row in range(board_size): 
        board.append([]) 
        for column in range(board_size): 
            board[row].append(empty_cell) 

#initiate board (for debug purposes) - DOES NOT WORK, REASON NOT FOUND YET
def initiate_board(board):
    board = [[1,0,0,0,0,0,0,0,0,0],
             [1,0,0,0,0,0,0,0,0,0],
             [1,0,0,0,0,0,0,0,0,0],
             [1,0,0,1,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0],
             [0,0,0,1,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]]

#check board TBD

#print board
def print_board(board):
    x = ["",0,1,2,3,4,5,6,7,8,9,10]
    print(x)
    i=0
    for row in board:
        print( i, row)
        i+=1
        

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
def shoot(board):
    hitFlag = 0 #flag marking if the player missed (0) or hit (1) enemy's ship
    Ship = []
    iDeck = 0
    aliveDecks = 0
    row = 0
    col = 0
    
    print("Shoot!")
    targetRow = int(input("Target row: "))
    targetCol = int(input("Target column: ")) #if the cell is empty
    if board[targetRow][targetCol] == 0: 
        board[targetRow][targetCol] = "."
        print("Missed")
    else:
        #BUG: case when cell == x is not processed
        #case when cell == 1:
        if board[targetRow][targetCol] == 1:   
            board[targetRow][targetCol] = "x"
            #if the cel is not empty
            #build vertical array of potential ship decks
            i = 0
            for row in range(targetRow-3,targetRow+4): # from -(MaxDeckSize-1) rows till +(MaxDeckSize-1) rows. BUG: MaxDeckSize not parametrized. 
                print(targetRow,row, targetCol)
                if board[row][targetCol] == 1 or board[row][targetCol] == "x":
                    Ship.append([]) #add array cell to store a pair of coordinates
                    Ship[i].append(row)
                    Ship[i].append(targetCol)
                    print(row,targetCol,Ship)
                    i+=1
            #check all items in the vertical array
            iDeck = len(Ship)
            #BUG: we don't check if the decks are sequential
            if iDeck > 1: #if number of _sequential_ decks vertically > 1, then the ship is oriented vetically
                i = 0
                for i in range(iDeck):
                    if board[Ship[i][0]][Ship[i][1]] == 1:
                        aliveDecks+=1
            if aliveDecks > 0:
                print("Hit! Shoot again!")
            else:
                print("KILLED! Shoot again!")
            
            
            #find sub-array of decks
            #if sub-array of decks length is ==1, then
                #build horisontal array of potential ship decks
                    #if horisonal sub-array length ==1, then KILLED (only target cell )
                    #else
            #else (if vertical sub-array of decks length >1)

         
#BODY
'''
print("This is your board. Empty for now:")
create_board(boardPlayer1)
print_board(boardPlayer1)
'''
print("Board initiated:")
#initiate_board(boardPlayer1)
print_board(boardPlayer1)
#set_ships_manually(boardPlayer1,deckShips,numberOfShipsPerDeck)

#shoot cycle
while willShoot == "y":
    shoot(boardPlayer1)
    print_board(boardPlayer1)
    willShoot = raw_input("Shoot again? y/n: ")
    
clear_board(boardPlayer1)
