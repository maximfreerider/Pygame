import pygame

pygame.init()
win = pygame.display.set_model((500),(500))

pygame.display.set_caption("My game")

x = 50
y = 50
width = 40
height = 60
speed = 15

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(win, (0,0,255), (x, y, width, height))
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]
        x -= speed
    if keys[pygame.K_RIGHT]
        x += speed
    if keys[pygame.K_UP]
        Y -= speed
    if keys[pygame.K_DOWN]
        Y += speed    

pygame.quit()
