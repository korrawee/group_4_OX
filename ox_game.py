class Board :
    def __init__(self,):
        self.array = [[' ',' ',' '], 
                    [' ', ' ', ' '], 
                    [' ', ' ', ' ']]
        self.game_stillplay = True
        self.winner = None
        self.player = "X"
        self.turn = 0


    def startgame(self):
        textinput = TextInput() #declare obj var.
        printer = Printer()
        while self.game_stillplay: #game loop
            printer.show(self)
            if(self.win_check()):
                if self.player == 'O':
                    self.player = 'X'
                    print("THE WINNER IS PLAYER " + self.player + " !!")
                    self.player = 'O'
                else:
                    self.player = 'O'
                    print("THE WINNER IS PLAYER " + self.player + " !!")
                    self.player = 'X'
                self.clearBoard()
                print("\nNEW GAME BEGIN!!!!\n")
                printer.show(self)
            if (self.tie_check()):
                print("Game TIE..")
                self.clearBoard()
                printer.show(self)
            print(" Player " + self.player + ' TURN',end='')
            textinput.getInput(self)

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
            state  = 1
        if(state == 1):
            return True
        else:
            return False

    def tie_check(self):
        for k in self.array:
            if '-' in k:
                return True
            else:
                return False

    def error_check(self,position):
        if(position > 9):
            return False
        tmp = self.getChar(position)
        if(tmp == 'O'):
            return False
        elif(tmp == 'X'):
            return False
        else:
            return True

    def getChar(self, position):
        list1 = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        return self.array[list1[position-1][0]][list1[position-1][1]]

    def setChar(self, char,  r, c):
        list1 = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        if self.error_check(obj,position) is True :
            if (self.player == 'O'):
                self.array[lis1[position-1][0]][list1[position-1][1]] = char
                self.player = 'X'
            elif(self.player == 'X'):
                self.array[lis1[position-1][0]][list1[position-1][1]] = char
                self.player = 'O'
    def claerBoard(self):
        self.array = [[' ',' ',' '],
                [' ',' ',' '],
                [' ',' ',' ']]
#===========================================================================================
class Printer:
    def show(self,obj):
        print("|",end="")
        for position in range(1,10):
            tmp = obj.getChar(position)
            print(tmp,end="")
            print("|",end="")
            if(position%3 == 0 and position != 1):
                print("\n-------")
#===========================================================================================
class TextInput() :
    def getInput(self,obj):
        position = int(input("\nwhich box you desire: "))
        obj.setChar(position)
        
game = Board()
game.startgame()

