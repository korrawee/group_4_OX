class Board :
    def __init__(self,):
        self.array = [[' ',' ',' '], 
                    [' ', ' ', ' '], 
                    [' ', ' ', ' ']]
        self.playerTurn = 1
        self.player = ['O', 'X']
        self.row = 0
        self.column = 0

    def win_check(self,):
        state = 0
        for row in range(3):
            if self.array[row][0] == self.array[row][1] == self.array[row][2] != "_":
                state = 1
        # check column        
        for column in range(3):
            if self.array[0][column] == self.array[1][column] == self.array[2][column] != "_":
                state = 1
        # check cross    
        if self.array[0][0] == self.array[1][1] == self.array[2][2] != "_":
            state = 1
        elif self.array[0][2] == self.array[1][1] == self.array[2][0] != "_":
            #print(array[0][2], "player is WIN!!!")
            state  = 1
        if(state == 1):
            return True
        else:
            return False

    def getChar(self, row, column):
        return self.array[row][column]

    def setChar(self, char,  r, c):
        self.array[r][c] = char
class Printer:
    def __init__(self,):
	self.board = Board()
	self.textInput = TextInput()
    def show(self):
	for i in range(3):
	     for j in range(3):
		print("|",end=' ')
		tmp = self.board.getChar(i,j) #สร้างตัวแปรไว้เก็บค่าชั่วคราว
		print(tmp,end = " ")
	     print("|\n-------")
        self.textInput.getInput(self)
	self.show()
    def resetBoard(self):
	for a in range(3)d:
	   for b in range(3):
		self.board.getChar(a,b)
	self.show()

class TextInput:
    def __init__(self):

        
game = Printer()
game.show()
