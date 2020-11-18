#%%
import pygame

def makeVerticleLines(x):
    L = []
    for i in range(x):
        point1 = tuple([i * 40, 0])
        point2 = tuple([i * 40, 800])
        L.append(tuple([point1, point2]))
    return L

def makeHorizontalLines(x):
    L = []
    for i in range(x):
        point1 = tuple([0, i * 40])
        point2 = tuple([800, i * 40])
        L.append(tuple([point1, point2]))
    return L
    
class Grid: 
    def __init__(self):
        self.grid_lines = makeVerticleLines(11)
        self.horizontal_grid_lines = makeHorizontalLines(21)
        
    def draw(self, surface):
        for line in self.grid_lines:
            pygame.draw.line(surface, (23, 23, 23), line[0], line[1], 1)

        for horiz in self.horizontal_grid_lines:
            pygame.draw.line(surface, (23, 23, 23), horiz[0], horiz[1], 1)

