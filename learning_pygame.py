import pygame
import sys

# Start pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rectangle Demo")

# Clock (controls FPS)
clock = pygame.time.Clock()

running = True

while running:

    # Handle events (like closing window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background (IMPORTANT so old frames don't stack)
    screen.fill((30, 30, 30))

    # YOUR RECTANGLE LINE
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))

    # Update screen (show everything we just drew)
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

# Quit cleanly
pygame.quit()
sys.exit()