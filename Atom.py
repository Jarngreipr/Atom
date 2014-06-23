from random import randint

import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

# Number of rows and columns in grid
rows = 12
columns = 12

grid = []
for row in range (rows):
    # Add an empty array that will hold each cell
    # in this dow
    grid.append([])
    for column in range(columns):
        grid[row].append(0) # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
# grid[0][0] = 1

pygame.init()

# Box specifications
width = 20
height = 20
margin = 5

# Size of display window
wbox = width * columns + margin * columns
hbox = height * rows + margin * rows
size = (wbox, hbox)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("Atom")

# Loop until the user clicks the close button.
done = False

clock = pygame.time.Clock()

class Atom(object):
    
    def atom(self):
        x = randint(1,10)
        y = randint(1,10)
        return [x, y]   
    
class North(object):
    
    def north(self):
        for row in range(rows):
            if atom == [row, column]:
                print "Gleypt!"
            #elif atom == [row - 1, column - 1]:
             #   east()
            #elif atom == [row - 1, column + 1]:
            #    west()
            elif atom != [row, column]:
                row += 1
            else:
                color = RED

# Main program loop
while not done:
    #-- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            laser = (row, column)
            # set that location to one
            #grid[row][column] = 1
            print "Click location %s. Grid coordinates: %d,%d" % (pos, row, column)
            for column in range(1, 10):
                if row == 11:
                    laser.north()
                else:
                    print "no!" 

    screen.fill(BLACK)
    # Draw grid
    for row in range(rows):
        for column in range(columns):
            color = WHITE
            pygame.draw.rect(screen,
                             color,
                             [(margin + width) * column + margin,
                              (margin + height) * row + margin,
                              width,
                              height])        
    
                    
    #---- Game logic should go here

            
                    
    
    # --- Drawing code should go here
    
    
    # First, clear the screen to go white. Don't put other drawing commands
    # above this, or they will be erased with this command
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
    
