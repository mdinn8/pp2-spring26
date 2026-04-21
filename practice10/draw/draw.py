import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

screen.fill(WHITE)

color = BLACK
radius = 10
drawing = False
mode = "circle"   

fill = False

start_pos = None  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
            if event.key == pygame.K_g:
                color = GREEN
            if event.key == pygame.K_b:
                color = BLUE
            if event.key == pygame.K_k:
                color = BLACK

            if event.key == pygame.K_e:
                mode = "erase"
            if event.key == pygame.K_c:
                mode = "circle"
            if event.key == pygame.K_q:
                mode = "rect"
            if event.key == pygame.K_f:
                fill = True
            if event.key == pygame.K_KP_MINUS:
                radius -=1
            if event.key == pygame.K_KP_PLUS:
                radius +=1   

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pygame.mouse.get_pos()
            canvas_copy = screen.copy()

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            if mode == "rect":
                end_pos = pygame.mouse.get_pos()
                screen.blit(canvas_copy,(0,0))
                x1, y1 = start_pos
                x2, y2 = end_pos

                rect = pygame.Rect(min(x1,x2), min(y1,y2),
                                   abs(x2-x1), abs(y2-y1))
                pygame.draw.rect(screen, color, rect, 2)

                

        if event.type == pygame.MOUSEMOTION and drawing:
            x, y = pygame.mouse.get_pos()

            if mode == "circle":
                pygame.draw.circle(screen, color, (x, y), radius)

            elif mode == "erase":
                pygame.draw.circle(screen, WHITE, (x, y), radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()