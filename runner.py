import pygame
import numpy as np
import math

TRAN_X = 200
TRAN_Y = 200
def inverse_kinematics(x, y, l1, l2):
    print(x**2 + y**2 - l1**2 - l2**2)
    print(2*l1*l2)
    print((x**2 + y**2 - l1**2 - l2**2) / (2*l1*l2))
    theta2 = np.arccos((x**2 + y**2 - l1**2 - l2**2) / (2*l1*l2))
    theta1 = np.arctan2(y, x) - np.arctan2(l2*np.sin(theta2), l1 + l2*np.cos(theta2))
    return theta1, theta2

def draw_arm(theta1, theta2, l1, l2, screen, color=(255, 0, 0)):
    print(np.cos(theta1))
    print(np.cos(theta1 + theta2))
    if not math.isnan(theta1):
        x = int(l1*np.cos(theta1) + l2*np.cos(theta1 + theta2))
        y = int(l1*np.sin(theta1) + l2*np.sin(theta1 + theta2))

        pygame.draw.line(screen, color, (TRAN_X, TRAN_Y), (TRAN_X + l1*np.cos(theta1), TRAN_Y + l1*np.sin(theta1)), 5)
        pygame.draw.line(screen, color, (TRAN_X + l1*np.cos(theta1), TRAN_Y + l1*np.sin(theta1)), (TRAN_X + x, TRAN_Y + y), 5)

if __name__ == '__main__':
    x = 50
    y = 60
    l1 = 100
    l2 = 100
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()
    running = True
    while running:
        (x,y) = pygame.mouse.get_pos()
        (x,y) = (x-TRAN_X, y-TRAN_Y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        theta1, theta2 = inverse_kinematics(x, y, l1, l2)
        screen.fill((255, 255, 255))
        draw_arm(theta1, theta2, l1, l2, screen)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

