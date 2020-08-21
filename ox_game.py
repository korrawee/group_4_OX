class Board :
    def __init__(self):
        self.array = [null * 3] * 3
        self.playerTurn = 1
        self.player = ['O', 'X']
        self.row = 0
        self.column = 0
    def win_check(self,):
        state = 0
        for row in range(3):
        if array[row][0] == array[row][1] == array[row][2] != "_":
            print(array[row][0], "player is WIN!!!")
            state = 1
    # check column        
    for column in range(3):
        if array[0][column] == array[1][column] == array[2][column] != "_":
            print(array[0][column], "player is WIN!!!")
            state = 1
    # check cross    
    if array[0][0] == array[1][1] == array[2][2] != "_":
        print(aaray[0][0], "player is WIN!!!")
        state = 1
    elif array[0][2] == array[1][1] == array[2][0] != "_":
        print(array[0][2], "player is WIN!!!")
        state  = 1
    return state

    def getChar(self, row, column):
        return self.array[row][column]
    def getPosition(self,):
        return self.array[row][column]
    def setChar(self,):
        pass
class Printer :
    
class TextInput :


b1 = Board()
