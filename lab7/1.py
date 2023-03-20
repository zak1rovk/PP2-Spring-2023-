import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mickey Mouse Clock")

clock_image = pygame.image.load("mickeyclock.jpeg")

clock_center = (200, 200)

minute_hand_length = 80
second_hand_length = 100

minute_hand_color = (255, 255, 255)
second_hand_color = (255, 0, 0)

def draw_hand(angle, length, color):
    rotated_hand = pygame.transform.rotate(clock_image, angle)
    hand_rect = rotated_hand.get_rect()
    hand_rect.center = clock_center
    hand_end = (clock_center[0] + length * pygame.math.Vector2(angle).x, clock_center[1] - length * pygame.math.Vector2(angle).y)
    pygame.draw.line(screen, color, clock_center, hand_end, 5)
    screen.blit(rotated_hand, hand_rect)

minute_hand_image = pygame.image.load("mickeyclock_minute_hand.png")
second_hand_image = pygame.image.load("mickeyclock_second_hand.png")

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = datetime.datetime.now().time()

    minute_angle = (current_time.minute / 60) * 360
    second_angle = (current_time.second / 60) * 360

    screen.blit(clock_image, (0, 0))

    draw_hand(minute_angle, minute_hand_length, minute_hand_color)
    draw_hand(second_angle, second_hand_length, second_hand_color)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()