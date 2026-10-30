
import pygame
import sys

pygame.init()

# VENSTER
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("De Fabeltjesfuik")

clock = pygame.time.Clock()

# KLEUREN
BACKGROUND = (30, 32, 45)
BLACK = (12, 12, 15)
WHITE = (240, 240, 245)
GREEN = (70, 220, 150)
GREY = (130, 135, 150)
RED = (240, 90, 110)
BLUE = (75, 130, 220)

# LETTERTYPES
font = pygame.font.SysFont("arial", 17)
small = pygame.font.SysFont("arial", 13)
bold = pygame.font.SysFont("arial", 21, bold=True)
title_font = pygame.font.SysFont("arial", 25, bold=True)

# TELEFOON EN SCHERM
PHONE = pygame.Rect(100, 35, 400, 720)
VIEW = pygame.Rect(125, 190, 350, 495)

# VIDEO'S
videos = [
    {
        "topic": "Platte aarde",
        "title": "Is de aarde eigenlijk plat?",
        "description": "Een video met argumenten van mensen die geloven dat de aarde plat is.",
        "color": (80, 105, 160)
    },
    {
        "topic": "Wetenschap",
        "title": "De aarde vanuit de ruimte",
        "description": "Bekijk foto's en metingen die laten zien hoe onze planeet eruitziet.",
        "color": (40, 100, 155)
    },
    {
        "topic": "Maanlanding",
        "title": "Was de maanlanding echt?",
        "description": "Ontdek welke vragen mensen stellen over de maanlanding.",
        "color": (100, 85, 135)
    },
    {
        "topic": "Platte aarde",
        "title": "Waarom geloven mensen dit?",
        "description": "Een video over de argumenten achter de platte-aardetheorie.",
        "color": (100, 85, 150)
    },
    {
        "topic": "Dieren",
        "title": "Bijzondere dieren op aarde",
        "description": "Ontdek bijzondere dieren en hun leefgebieden.",
        "color": (55, 125, 95)
    },
    {
        "topic": "Platte aarde",
        "title": "De ijsmuur-theorie",
        "description": "Sommige mensen beweren dat er een ijsmuur rond de aarde is. Klopt dat?",
        "color": (75, 110, 155)
    },
    {
        "topic": "Wetenschap",
        "title": "Hoe werkt zwaartekracht?",
        "description": "Ontdek hoe wetenschappers zwaartekracht onderzoeken.",
        "color": (45, 110, 145)
    },
]

# SPELGEGEVENS
scroll = 0
likes = {}
saved = set()
watched = set()
recommended = set()

like_counts = {}
message = "Welkom! Begin met scrollen."
message_timer = 4

# HULPFUNCTIE VOOR TEKST
def draw_text(text, x, y, color=WHITE, f=font):
    image = f.render(text, True, color)
    screen.blit(image, (x, y))


def draw_wrapped(text, x, y, max_width, color=WHITE):
    words = text.split()
    line = ""
    line_y = y

    for word in words:
        test = line + word + " "
        if font.size(test)[0] > max_width:
            draw_text(line, x, line_y, color)
            line = word + " "
            line_y += 24
        else:
            line = test

    if line:
        draw_text(line, x, line_y, color)


# NIEUWE AANBEVELINGEN
def update_algorithm(topic):
    global message, message_timer

    count = like_counts.get(topic, 0)

    if count == 3 and topic not in recommended:
        recommended.add(topic)

        message = "Het algoritme ontdekt jouw interesse!"
        message_timer = 4

        # Meer video's over hetzelfde onderwerp
        if topic == "Platte aarde":
            extra = [
                {
                    "topic": topic,
                    "title": "Nog meer over de platte aarde",
                    "description": "Een nieuwe video met beweringen van voorstanders. Controleer de bronnen!",
                    "color": (110, 75, 145)
                },
                {
                    "topic": topic,
                    "title": "Waarom zou de aarde plat zijn?",
                    "description": "Bekijk hoe dezelfde theorie steeds opnieuw wordt besproken.",
                    "color": (95, 70, 145)
                },
                {
                    "topic": topic,
                    "title": "De waarheid over onze planeet?",
                    "description": "Een video met beweringen die je kritisch kunt onderzoeken.",
                    "color": (115, 80, 150)
                }
            ]
        else:
            extra = [
                {
                    "topic": topic,
                    "title": "Meer over " + topic,
                    "description": "Het algoritme denkt dat je dit onderwerp interessant vindt.",
                    "color": (90, 90, 150)
                }
                for _ in range(3)
            ]

        videos.extend(extra)


# TELEFOON TEKENEN
def draw_phone():
    pygame.draw.rect(
        screen, (18, 19, 27),
        (105, 45, 390, 710), border_radius=48
    )

    pygame.draw.rect(
        screen, (110, 115, 130),
        (100, 35, 400, 720), border_radius=50
    )

    pygame.draw.rect(
        screen, BLACK,
        (106, 41, 388, 708), border_radius=45
    )

    pygame.draw.rect(
        screen, (24, 27, 38),
        (120, 65, 360, 680), border_radius=35
    )

    pygame.draw.rect(
        screen, (40, 42, 48),
        (235, 77, 100, 12), border_radius=6
    )

    pygame.draw.circle(screen, (45, 65, 95), (355, 83), 7)

    pygame.draw.rect(
        screen, WHITE,
        (235, 720, 130, 5), border_radius=3
    )

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


# VIDEO KAART TEKENEN
def draw_video(video, index, y):
    card = pygame.Rect(130, y, 340, 415)

    pygame.draw.rect(
        screen, (42, 46, 62),
        card, border_radius=16
    )

    # Video-afbeelding / achtergrond
    picture = pygame.Rect(140, y + 10, 320, 190)

    pygame.draw.rect(
        screen, video["color"],
        picture, border_radius=12
    )

    # Decoratieve cirkel
    pygame.draw.circle(
        screen, (180, 190, 220),
        (300, y + 100), 48
    )

    pygame.draw.circle(
        screen, video["color"],
        (300, y + 100), 40
    )

    draw_text(
        "VIDEO",
        275, y + 88,
        WHITE, bold
    )

    # Onderwerp
    draw_text(
        video["topic"].upper(),
        145, y + 215,
        GREEN, small
    )

    # Titel
    draw_wrapped(
        video["title"],
        145, y + 240,
        300, WHITE
    )

    # Beschrijving
    draw_wrapped(
        video["description"],
        145, y + 290,
        300, GREY
    )

    # Knoppen
    like_rect = pygame.Rect(145, y + 355, 95, 38)
    save_rect = pygame.Rect(250, y + 355, 95, 38)

    pygame.draw.rect(
        screen,
        RED if index in likes else (65, 70, 85),
        like_rect, border_radius=9
    )

    pygame.draw.rect(
        screen,
        BLUE if index in saved else (65, 70, 85),
        save_rect, border_radius=9
    )

    draw_text(
        "♥ Like",
        like_rect.x + 19,
        like_rect.y + 9
    )

    draw_text(
        "★ Bewaar",
        save_rect.x + 9,
        save_rect.y + 9
    )

    return like_rect, save_rect


# HOOFDLOOP
running = True
view_time = 0
last_video = None

while running:
    dt = clock.tick(60) / 1000

    screen.fill(BACKGROUND)
    draw_phone()

    # TITEL
    draw_text("ForYou", 140, 115, WHITE, title_font)
    draw_text("Ontdek video's", 140, 150, GREY, small)

    # SCROLLGEBIED
    screen.set_clip(VIEW)

    current_buttons = []

    for i, video in enumerate(videos):
        y = 200 + i * 430 - scroll

        if y < 690 and y + 415 > 190:
            like_rect, save_rect = draw_video(video, i, y)

            current_buttons.append(
                (i, like_rect, save_rect)
            )

    screen.set_clip(None)

    # WELKE VIDEO WORDT BEKEKEN?
    active_video = None

    for i, video in enumerate(videos):
        y = 200 + i * 430 - scroll

        if y <= 205 and y + 415 > 205:
            active_video = i
            break

    if active_video is not None:
        if active_video == last_video:
            view_time += dt
        else:
            last_video = active_video
            view_time = 0

        if view_time >= 5 and active_video not in watched:
            watched.add(active_video)

            topic = videos[active_video]["topic"]
            like_counts[topic] = like_counts.get(topic, 0) + 1

            view_time = 0

    # MELDING
    if message_timer > 0:
        message_timer -= dt

        pygame.draw.rect(
            screen, (55, 65, 85),
            (135, 675, 330, 35),
            border_radius=8
        )

        draw_text(
            message, 145, 685,
            GREEN, small
        )

    # ALGORITME-INFORMATIE
    if recommended:
        draw_text(
            "Je feed wordt persoonlijker...",
            140, 160, GREEN, small
        )

    # BEDIENING
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # SCROLLEN
        if event.type == pygame.MOUSEWHEEL:
            scroll -= event.y * 45
            scroll = max(
                0,
                min(scroll, max(0, len(videos) * 430 - 495))
            )

        # KNOPPEN
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                mx, my = event.pos

                for i, like_rect, save_rect in current_buttons:

                    if like_rect.collidepoint(mx, my):
                        if i not in likes:
                            likes.add(i)

                            topic = videos[i]["topic"]
                            like_counts[topic] = (
                                like_counts.get(topic, 0) + 1
                            )

                            update_algorithm(topic)

                    elif save_rect.collidepoint(mx, my):
                        if i in saved:
                            saved.remove(i)
                        else:
                            saved.add(i)

                        message = "Video opgeslagen!"
                        message_timer = 2

    pygame.display.flip()

pygame.quit()
sys.exit()
