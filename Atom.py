import random, pygame, sys



FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
ROWS = 8
COLUMNS = 8
BOXSIZE = 40 # size of white boxes
MARGIN = 2
BOARDWIDTH = BOXSIZE * COLUMNS + MARGIN * COLUMNS
BOARDHEIGHT = BOXSIZE * ROWS + MARGIN * ROWS
assert (BOARDWIDTH * BOARDHEIGHT < WINDOWWIDTH * WINDOWHEIGHT), 'Board cannot be larger than display window'
assert (BOARDWIDTH < WINDOWWIDTH), 'Board width cannot be greater than window width'
assert (BOARDHEIGHT < WINDOWHEIGHT), 'Board height cannot be greater than window height'
ATOMS = 1

# colors: R G B
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =   (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLUEGREEN= (20, 180, 255)
BGCOLOR = BLUEGREEN



def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    
    pygame.display.set_caption('Atom')
    
    mainBoard = getRandomizedBoard()
    
    while True: # main game loop
        DISPLAYSURF.fill(BGCOLOR) # drawing the window
        drawBoard()
        
        for event in pygame.event.get(): # event handling loop
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True                
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def getRandomizedBoard():
    # create a matrix full of zeroes
    grid = [[0 for columns in range(COLUMNS)] for rows in range(ROWS)]
            
    # insert atoms randomly
    for atoms in range(ATOMS):
        rows = ROWS - 1
        columns = COLUMNS -1
        y = random.randint(-1, rows)
        x = random.randint(-1, columns)
        grid[y][x] = 1 

def getLaserBoard():
    # Create a board one bigger than the one containing atoms
    LASERCOLUMNS = COLUMNS + 2
    LASERROWS = ROWS + 2
    lgrid = [[0 for columns in range(LASERCOLUMNS)] for rows in range(LASERROWS)]
    for i in range(1, LASERROWS - 1):
        lgrid[i][0] = 'W%d' % (i)
    for i in range(1, LASERROWS - 1):
        lgrid[i][LASERCOLUMNS] = 'E%d' % (i)
    for i in range(1, LASERCOLUMNS -1):
        lgrid[LASERROWS][i] = 'S%d' % (i)
    for i in range(1, LASERCOLUMNS - 1):
        lgrid[0][i] = 'N%d' % (i)
        
def drawBoard():
    startposx = (WINDOWWIDTH - BOARDWIDTH) / 2
    startposy = (WINDOWHEIGHT - BOARDHEIGHT) / 2
    for row in range(ROWS):
        for column in range(COLUMNS):
            color = WHITE
            pygame.draw.rect(DISPLAYSURF,
                             color,
                             [startposx +(MARGIN + BOXSIZE) * column + MARGIN,
                              startposy + (MARGIN + BOXSIZE) * row + MARGIN,
                              BOXSIZE,
                              BOXSIZE])

#def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    #left = boxx * (BOXSIZE +
                               

if __name__ == '__main__':                           
    main()
