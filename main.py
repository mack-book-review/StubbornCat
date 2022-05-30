import pygame
from pygame.locals import *
from mouse import Mouse
from cat import Cat

pygame.init()
pygame.font.init()


size = (width,height) = (500,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Georgia",20)

is_running = True
game_over = False
t0 = 0
t1 = 0


WHITE = (255,255,255)
BLUE = (0,0,255)

def main():
    global is_running,game_over,clock,t0,t1
    mouse = Mouse()
    cat = Cat()
    restart_text = font.render("Play Again?",True,BLUE)
    restart_text_rect = restart_text.get_rect()
    restart_text_rect.center = (width/2,height-50)


    total_time = 0

    while is_running:
        clock.tick(60)
        t1 = pygame.time.get_ticks() // 1000
        total_time += t1 - t0

        time_text = font.render("Time Survived: {}".format(total_time), True, BLUE)
        time_text_rect = time_text.get_rect()
        time_text_rect.center = (100, height - 50)
        for event in pygame.event.get():
            if event.type == QUIT:
                is_running = False
            if event.type == MOUSEBUTTONDOWN:
                if game_over:
                    x,y = pygame.mouse.get_pos()
                    if restart_text_rect.collidepoint(x,y):
                        cat.reset_position()
                        mouse.reset()
                        t0 = t1
                        total_time = 0
                        game_over = False

        if not game_over:

            if mouse.rect.colliderect(cat.rect):
                mouse.die()
                time = 0
                game_over = True

            mouse.update()
            cat.update()


        screen.fill(WHITE)
        mouse.draw(screen)
        cat.draw(screen)

        if game_over:
            game_over_text = font.render("Game Over", True, BLUE)
            game_over_text_rect = game_over_text.get_rect()
            game_over_text_rect.center = (width / 2, 20)
            screen.blit(game_over_text, game_over_text_rect)
            screen.blit(restart_text,restart_text_rect)
        else:
            screen.blit(time_text,time_text_rect)

        pygame.display.flip()
        t0 = t1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
