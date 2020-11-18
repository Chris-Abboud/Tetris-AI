class shapeCharacter:
    rotationNumber = 1

    def moveRight(self):
        self.x1 = self.x1 + 1
        self.x2 = self.x2 + 1
        self.x3 = self.x3 + 1
        self.x4 = self.x4 + 1

        self.cordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]
        self.rotationCordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]

    def moveDown(self):
        self.y1 = self.y1 + 1
        self.y2+=1
        self.y3+=1
        self.y4+=1

        self.cordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]
        self.rotationCordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]

    def moveLeft(self):
        self.x1 = self.x1 - 1
        self.x2 = self.x2 - 1
        self.x3 = self.x3 - 1
        self.x4 = self.x4 - 1

        self.cordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]
        self.rotationCordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]

    def updateCords(self, update):
        [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)] = update
        self.cordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]

class Square(shapeCharacter):
    def __init__(self):
        self.number = 1
        self.y1, self.y2, self.y3, self.y4 = 0, 0, 1, 1
        self.x1, self.x2, self.x3, self.x4 = 4, 5, 4, 5

        self.cordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]
        self.rotationCordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]

    def rotate(self):
        self.rotationNumber = 1

class LongPiece(shapeCharacter):
    def __init__(self):
        self.number = 2
        self.y1, self.y2, self.y3, self.y4 = 0, 0, 0, 0
        self.x1, self.x2, self.x3, self.x4 = 3, 4, 5, 6

        self.cordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]
        self.rotationCordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]

    def rotate(self):
        self.rotationNumber+=1
        if self.rotationNumber % 2 != 0:
            self.rotationCordinates = [(self.y1+1,self.x1-1), (self.y2,self.x2), (self.y3-1,self.x3+1), (self.y4-2,self.x4+2)]

        if self.rotationNumber % 2 == 0:
            self.rotationCordinates = [(self.y1-1,self.x1+1), (self.y2,self.x2), (self.y3+1,self.x3-1), (self.y4+2,self.x4-2)]

class TeePiece(shapeCharacter):
    def __init__(self):
        self.number = 3
        self.y1, self.y2, self.y3, self.y4 = 0, 1, 1, 1
        self.x1, self.x2, self.x3, self.x4 = 4, 3, 4, 5

        self.cordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]
        self.rotationCordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]

    def rotate(self):
        self.rotationNumber+=1
        if self.rotationNumber % 4 == 0:
            self.rotationCordinates = [(self.y1-1,self.x1+1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4-2)]

        elif self.rotationNumber % 3 == 0:
            self.rotationCordinates = [(self.y1+1,self.x1-1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]

        elif self.rotationNumber % 2 == 0:
            self.rotationCordinates = [(self.y1,self.x1), (self.y2+1,self.x2+1), (self.y3,self.x3), (self.y4,self.x4)]
        else:
            self.rotationCordinates = [(self.y1,self.x1), (self.y2-1,self.x2-1), (self.y3,self.x3), (self.y4,self.x4+2)]
            self.rotationNumber = 1

class LeftEl(shapeCharacter):
    def __init__(self):
        self.number = 4
        self.y1, self.y2, self.y3, self.y4 = 0, 1, 1, 1
        self.x1, self.x2, self.x3, self.x4 = 3, 3, 4, 5

        self.cordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]
        self.rotationCordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]

    def rotate(self):
        self.rotationNumber+=1
        if self.rotationNumber % 4 == 0:
            self.rotationCordinates = [(self.y1,self.x1-2), (self.y2+1,self.x2-1), (self.y3,self.x3), (self.y4-1,self.x4+1)]
            

        elif self.rotationNumber % 3 == 0:
            self.rotationCordinates = [(self.y1+2,self.x1), (self.y2+1,self.x2+1), (self.y3,self.x3), (self.y4-1,self.x4-1)]

        elif self.rotationNumber % 2 == 0:
            self.rotationCordinates = [(self.y1,self.x1+2), (self.y2-1,self.x2+1), (self.y3,self.x3), (self.y4+1,self.x4-1)]

        else:
            self.rotationCordinates = [(self.y1-2,self.x1), (self.y2-1,self.x2-1), (self.y3,self.x3), (self.y4+1,self.x4+1)]
            self.rotationNumber = 1


class RightEl(shapeCharacter):
    def __init__(self):
        self.number = 5
        self.y1, self.y2, self.y3, self.y4 = 0, 1, 1, 1
        self.x1, self.x2, self.x3, self.x4 = 5, 3, 4, 5

        self.cordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]
        self.rotationCordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]
    
    def rotate(self):
        self.rotationNumber+=1
        if self.rotationNumber % 4 == 0:
            self.rotationCordinates = [(self.y1-2,self.x1), (self.y2+1,self.x2-1), (self.y3,self.x3), (self.y4-1,self.x4+1)]

        elif self.rotationNumber % 3 == 0:
            self.rotationCordinates = [(self.y1,self.x1-2), (self.y2+1,self.x2+1), (self.y3,self.x3), (self.y4-1,self.x4-1)]

        elif self.rotationNumber % 2 == 0:
            self.rotationCordinates = [(self.y1+2,self.x1), (self.y2-1,self.x2+1), (self.y3,self.x3), (self.y4+1,self.x4-1)]
        else:
            self.rotationCordinates = [(self.y1,self.x1+2), (self.y2-1,self.x2-1), (self.y3,self.x3), (self.y4+1,self.x4+1)]
            self.rotationNumber = 1



class ZigZagRight(shapeCharacter):
    def __init__(self):
        self.number = 6
        self.y1, self.y2, self.y3, self.y4 = 0, 0, 1, 1
        self.x1, self.x2, self.x3, self.x4 = 4, 5, 3, 4

        self.cordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]
        self.rotationCordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]

    def rotate(self):
        self.rotationNumber+=1
        if self.rotationNumber % 4 == 0:
            self.rotationCordinates = [(self.y1-1,self.x1-1), (self.y2-2,self.x2), (self.y3+1,self.x3-1), (self.y4,self.x4)]

        elif self.rotationNumber % 3 == 0:
            self.rotationCordinates = [(self.y1+1,self.x1-1), (self.y2,self.x2-2), (self.y3+1,self.x3+1), (self.y4,self.x4)]

        elif self.rotationNumber % 2 == 0:
            self.rotationCordinates = [(self.y1+1,self.x1+1), (self.y2+2,self.x2), (self.y3-1,self.x3+1), (self.y4,self.x4)]
        else:
            self.rotationCordinates = [(self.y1-1,self.x1+1), (self.y2,self.x2+2), (self.y3-1,self.x3-1), (self.y4,self.x4)]
            self.rotationNumber = 1


class ZigZagLeft(shapeCharacter):
    def __init__(self):
        self.number = 7
        self.y1, self.y2, self.y3, self.y4 = 0, 0, 1, 1
        self.x1, self.x2, self.x3, self.x4 = 3, 4, 4, 5

        self.cordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]
        self.rotationCordinates = [(self.y1,self.x1), (self.y2,self.x2), (self.y3,self.x3), (self.y4,self.x4)]
    
    
    def rotate(self):
        self.rotationNumber+=1
        if self.rotationNumber % 4 == 0:
            self.rotationCordinates = [(self.y1,self.x1-2), (self.y2-1,self.x2-1), (self.y3,self.x3), (self.y4-1,self.x4+1)]

        elif self.rotationNumber % 3 == 0:
            self.rotationCordinates = [(self.y1+2,self.x1), (self.y2+1,self.x2-1), (self.y3,self.x3), (self.y4-1,self.x4-1)]

        elif self.rotationNumber % 2 == 0:
            self.rotationCordinates = [(self.y1,self.x1+2), (self.y2+1,self.x2+1), (self.y3,self.x3), (self.y4+1,self.x4-1)]
        else:
            self.rotationCordinates = [(self.y1-2,self.x1), (self.y2-1,self.x2+1), (self.y3,self.x3), (self.y4+1,self.x4+1)]
            self.rotationNumber = 1
#%%