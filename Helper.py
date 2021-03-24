#%%
import copy
import pygame

def removAll(Grid):
    for i in range(len(Grid)):
        if canRemove(Grid[i]):
                Grid = DeleteRow(Grid, i)
                Grid = fillWithNum(Grid, oldCords, 0)


def canRemove(Row):
    count = 0
    for i in range(len(Row)):
        if Row[i] != 0:
            count+=1
    if count == 10:
        return True
    return False


def fillWithNum(L, points, Num):
    LCOPY = copy.copy(L)
    for cord in points:
        L[cord[0]][cord[1]] = Num
    return LCOPY


def DeleteRow(grid2, row):

    grid = copy.copy(grid2)
    for i in range(len(grid[0])):
        grid[row][i] = 0

    for j in range(row-1, 0, -1):
        for k in range(len(grid[0])):
            grid[j+1][k] = grid[j][k]

    return grid

def NotInList(L, number):
    for i in range(len(L)):
        if L[i] == number:
            return False
    return True

def FindBottomCords(L):
    J = copy.copy(L)
    J = sorted(J, key = lambda x: x[1])
    J.sort(key = lambda x: x[0])
    usedBase = []
    Lister = []
    final = []

    for i in range(len(J)): # Looks at all points and finds lowest by sorting and returning -1
        Base = J[i][1]
        if NotInList(usedBase, Base):
            usedBase.append(Base)
            for pair in J:
                if pair[1] == Base:
                    Lister.append(pair)
            final.append(Lister[-1])
            Lister = []
    return final

def canMoveDown(L, Cords):
    for cord in Cords:
        if cord[0] >= 19:
            return False
        if L[cord[0] + 1][cord[1]] != 0:
            return False
    return True



def FindRightCords(L):
    J = copy.copy(L)
    J = sorted(J, key = lambda x: x[0])
    J.sort(key = lambda x: x[1])
    usedBase = []
    Lister = []
    final = []

    for i in range(len(J)): # Looks at all points and finds lowest by sorting and returning -1
        Base = J[i][0]
        if NotInList(usedBase, Base):
            usedBase.append(Base)
            for pair in J:
                if pair[0] == Base:
                    Lister.append(pair)
            final.append(Lister[-1])
            Lister = []
    return final

def canMoveRight(L, Cords):
    for cord in Cords:
        if cord[1] > 8:
            return False
        if L[cord[0]][cord[1]+1] != 0:
            return False
    return True

def FindLeftCords(L):
    J = copy.copy(L)
    J = sorted(J, key = lambda x: x[0])
    J.sort(key = lambda x: x[1])
    usedBase = []
    Lister = []
    final = []

    for i in range(len(J)): # Looks at all points and finds lowest by sorting and returning -1
        Base = J[i][0]
        if NotInList(usedBase, Base):
            usedBase.append(Base)
            for pair in J:
                if pair[0] == Base:
                    Lister.append(pair)
            final.append(Lister[0])
            Lister = []
    return final

def canMoveLeft(L, Cords):
    for cord in Cords:
        if cord[1] < 1:
            return False
        if L[cord[0]][cord[1]-1] != 0:
            return False
    return True

def canRotate(RotatedCords, Grid):
    grid = copy.copy(Grid)

    for cord in RotatedCords:
        if cord[0] > 19 or cord[0] < 0:

            return False

        if cord[1] < 0 or cord[1] > 9:
            return False

    for cord in RotatedCords:
        if grid[cord[0]][cord[1]] != 0:
            return False
            
    return True

def drawGrid(Grid, screen):
    for i in range(len(Grid)):
            for j in range(len(Grid[0])):
                if Grid[i][j] == 1:
                    pygame.draw.rect(screen, (67, 200, 233), [j * 40, i * 40, 40, 40])
                if Grid[i][j] == 2:
                    pygame.draw.rect(screen, (227, 42, 220), [j * 40, i * 40, 40, 40]) 
                if Grid[i][j] == 3:
                    pygame.draw.rect(screen, (42, 227, 51), [j * 40, i * 40, 40, 40])   
                if Grid[i][j] == 4:
                    pygame.draw.rect(screen, (227, 120, 42), [j * 40, i *40, 40, 40])
                if Grid[i][j] == 5:
                    pygame.draw.rect(screen, (227, 42, 55), [j * 40, i * 40, 40, 40])
                if Grid[i][j] == 6:
                    pygame.draw.rect(screen, (255, 31, 252), [j * 40, i * 40, 40, 40])
                if Grid[i][j] == 7:
                    pygame.draw.rect(screen, (255, 247, 31), [j * 40, i * 40, 40, 40])

def show_score(x,y, screen, Score, font):
    scoreFinal = font.render("SCORE: " + str(Score), True, (255,255,255))
    screen.blit(scoreFinal, (x, y))

def show_level(x,y, screen, level, font):
    Level = font.render("LEVEL: " + str(level), True, (255,255,255))
    screen.blit(Level, (x, y))

def show_GameOver(x,y, screen, font):
    GameOver = font.render("GAME OVER!!!", True, (255,255,255))
    screen.blit(GameOver, (x, y))
# %%
