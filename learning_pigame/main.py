import pygame # the import of pygame and this is installed in pyharm and your pc

pygame.init() # this is always needed when coding with pygame // you can think of it as a pygame.init() where init = initialize
# setting icon// image needs to come from you file you dat. And then dont forget to call the variable
# Making Screen
screen = pygame.display.set_mode((800, 600)) # this variable is not really called but it is for the screen and display // as well as the coordinate are (x, y)
# setting title that goes in the right top corner after the logo
pygame.display.set_caption("Learning PYG")
# Setting Icon
icon_image = pygame.image.load("scientist.png")
pygame.display.set_icon(icon_image)

# game loop
running = True # variable to control the while loop
while running: # This while loop serves to maintain the pygame window running
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # //if condition so that when user presses the [x] the widow as well a sthe program stops running
            running = False


    i = 0
    loop = True
    while loop:
        screen.fill((169, 232, 123))
        pygame.display.update()  # Update is necessary for many events
        pygame.time.delay(200)
        i += 1

        screen.fill((255, 255, 255))
        pygame.display.update()
        pygame.time.delay(200)
        i += 1

        screen.fill((0, 0, 255))
        pygame.display.update()
        pygame.time.delay(200)

        i += 1

        if i == 12:
            loop = False
    screen.fill((169, 232, 123))

    pygame.display.update()  # Update is necessary for many event










