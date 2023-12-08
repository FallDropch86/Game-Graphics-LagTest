import pygame
import random
import time

pygame.init()

screen_WIDTH, screen_HEIGHT = 800, 600

startfps = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
clock = pygame.time.Clock()

# We will increase the ball speed due to the fact it lowers with decreasing fps...
ballspeed = 2

totalballs = 1

Window = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))
pygame.display.set_caption("Balls that multiply after bouncing of the screen. - FPS stress tester")

pygFont = pygame.font.SysFont(None, 35)

def text_display(text, color, posx, posy):
    fpstext = pygFont.render(text, False, color) # The boolean value is if there should be antialias. Set to false because of performance reasons
    Window.blit(fpstext, [posx, posy])

def circledraw(posx, posy, radius, color):
    pygame.draw.circle(Window, color, (posx, posy), radius)

class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

balls = [Ball(random.randint(0, 800), random.randint(0, 600), 20, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 0.1, 0.1)] # First ball

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for ball in balls:
        ball.x += ball.speed_x
        ball.y += ball.speed_y

        if ball.x - ball.radius < 0 or ball.x + ball.radius > screen_WIDTH:
            ball.speed_x = -ball.speed_x

        if ball.y - ball.radius < 0 or ball.y + ball.radius > screen_HEIGHT:
            ball.speed_y = -ball.speed_y

    Window.fill((0, 0, 0))

    for ball in balls:
        circledraw(ball.x, ball.y, ball.radius, ball.color)

    text_display("Resolution: 800x600", "Yellow", 550, 10)

    fps = clock.get_fps()
    fps_text = f"FPS: {fps:.3f}"
    fpstext_color = "Yellow"
    xpos, ypos = 10, 10 

    text_display(fps_text, fpstext_color, xpos, ypos)

    pygame.display.update()

    clock.tick(startfps)

    for ball in balls[:]:
        if (
            ball.x - ball.radius < 0 or ball.x + ball.radius > screen_WIDTH or
            ball.y - ball.radius < 0 or ball.y + ball.radius > screen_HEIGHT
        ):
            newball = Ball(random.randint(0, 800), random.randint(0, 600), 20, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 999999999, 999999999)
            balls.append(newball)
            totalballs += 1
            print(f"Total no. of balls: {totalballs}")

            break

pygame.quit()
quit()
