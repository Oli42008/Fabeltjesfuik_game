
import pygame
import sys

pygame.init()

# Venster
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Onze Game")

# Kleuren
BACKGROUND = (30, 32, 45)
BLACK = (12, 12, 15)
DARK_GREY = (40, 42, 48)
WHITE = (240, 240, 245)
GREEN = (70, 220, 150)

clock = pygame.time.Clock()

def draw_phone():
    # Schaduw
    pygame.draw.rect(
        screen, (18, 19, 27),
        (105, 45, 390, 710), border_radius=48
    )

    # Buitenrand van de telefoon
    pygame.draw.rect(
        screen, (110, 115, 130),
        (100, 35, 400, 720), border_radius=50
    )

    # Zwarte behuizing
    pygame.draw.rect(
        screen, BLACK,
        (106, 41, 388, 708), border_radius=45
    )

    # Scherm
    pygame.draw.rect(
        screen, (24, 27, 38),
        (120, 65, 360, 680), border_radius=35
    )

    # Bovenste speaker
    pygame.draw.rect(
        screen, DARK_GREY,
        (235, 77, 100, 12), border_radius=6
    )

    # Camera
    pygame.draw.circle(
        screen, (45, 65, 95), (355, 83), 7
    )
    pygame.draw.circle(
        screen, (20, 30, 45), (355, 83), 4
    )

    # Voorbeeld van een game-interface
    font = pygame.font.SysFont("arial", 28, bold=True)
    title = font.render("MIJN GAME", True, WHITE)
    screen.blit(title, title.get_rect(center=(300, 160)))

    # Speelveld
    pygame.draw.rect(
        screen, (37, 43, 58),
        (145, 205, 310, 390), border_radius=15
    )

    # Voorbeeldobject in het spel
    pygame.draw.rect(
        screen, GREEN,
        (275, 380, 50, 50), border_radius=8
    )

    # Onderste navigatiebalk
    pygame.draw.rect(
        screen, WHITE,
        (235, 720, 130, 5), border_radius=3
    )

    # Knoppen aan de zijkant
    pygame.draw.rect(
        screen, (100, 105, 120),
        (94, 175, 6, 75), border_radius=3
    )
    pygame.draw.rect(
        screen, (100, 105, 120),
        (94, 270, 6, 45), border_radius=3
    )
    pygame.draw.rect(
        screen, (100, 105, 120),
        (500, 190, 6, 100), border_radius=3
    )


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)

    draw_phone()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
