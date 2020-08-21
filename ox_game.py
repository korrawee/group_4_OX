class Board :
    def __init__(self,):
        self.array = [[' ',' ',' '], 
                    [' ', ' ', ' '], 
                    [' ', ' ', ' ']]
        self.row = 0
        self.column = 0

    def win_check(self,):
        state = 0
        for row in range(3):
            if self.array[row][0] == self.array[row][1] == self.array[row][2] != " ":
                state = 1
        # check column        
        for column in range(3):
            if self.array[0][column] == self.array[1][column] == self.array[2][column] != " ":
                state = 1
        # check cross    
        if self.array[0][0] == self.array[1][1] == self.array[2][2] != " ":
            state = 1
        elif self.array[0][2] == self.array[1][1] == self.array[2][0] != " ":
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
                print("|",end='')
                tmp = self.board.getChar(i,j) #สร้างตัวแปรไว้เก็บค่าชั่วคราว
                print(tmp,end = "")
            print("|\n-------")
        self.textInput.getInput(self)
        self.show()
    def resetBoard(self):
        for a in range(3):
            for b in range(3):
                self.board.setChar(" ", a, b)

class TextInput() :
    def __init__(self,):
        self.row = 0
        self.column = 0
        self.player = 1
    def getInput(self,obj):
        self.row = int(input("row: "))
        self.column = int(input("column: "))   
        if self.error_check(obj,self.row,self.column) is True :
            if(self.player == 1):
                obj.board.setChar("o", self.row, self.column)
                self.player = 2
            elif(self.player == 2):
                obj.board.setChar("x", self.row, self.column)
                self.player = 1
    def error_check(self,obj ,row ,column):
        if(self.row > 2):
            return False
        elif(self.column > 2):
            return False
        tmp = obj.board.getChar(self.row, self.column)
        if(tmp == 'o'):
            return False
        elif(tmp == 'x'):
            return False
        else:
            return True


        
game = Printer()
game.show()
