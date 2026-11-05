
import pygame
import sys

pygame.init()

# SCHERM
WIDTH = 600
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("De Fabeltjesfuik")

clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 18)
title_font = pygame.font.SysFont("arial", 25, bold=True)


# CLASS TELEFOON
class Telefoon:

    def tekenen(self):

        pygame.draw.rect(screen, (100, 105, 120),
                         (100, 35, 400, 720), border_radius=40)

        pygame.draw.rect(screen, (20, 22, 30),
                         (110, 45, 380, 700), border_radius=35)

        pygame.draw.rect(screen, (40, 42, 48),
                         (235, 65, 130, 10), border_radius=5)


# CLASS POST
class Post:

    def __init__(self, info):
        self.info = info
        self.likes = False
        self.bewaard = False

    def tekenen(self, y):

        pygame.draw.rect(screen, (55, 60, 80),
                         (130, y, 340, 160), border_radius=15)

        # Onderwerp
        onderwerp = font.render(
            self.info["onderwerp"], True, (70, 220, 150)
        )
        screen.blit(onderwerp, (145, y + 15))

        # Titel
        titel = font.render(
            self.info["titel"], True, (255, 255, 255)
        )
        screen.blit(titel, (145, y + 50))

        # Beschrijving
        beschrijving = font.render(
            self.info["beschrijving"], True, (180, 180, 190)
        )
        screen.blit(beschrijving, (145, y + 80))

        # Like
        if self.likes:
            like_tekst = "Liked"
        else:
            like_tekst = "Like"

        like = font.render(like_tekst, True, (240, 90, 110))
        screen.blit(like, (145, y + 120))

        # Bewaren
        if self.bewaard:
            bewaar_tekst = "Bewaard"
        else:
            bewaar_tekst = "Bewaar"

        bewaar = font.render(bewaar_tekst, True, (75, 130, 220))
        screen.blit(bewaar, (300, y + 120))


# CLASS GAME
class Game:

    def __init__(self):

        self.telefoon = Telefoon()
        self.scroll = 0
        self.posts = []

        # Alle video's
        videos = [
            {
                "onderwerp": "Platte aarde",
                "titel": "Is de aarde plat?",
                "beschrijving": "Bekijk deze theorie."
            },
            {
                "onderwerp": "Wetenschap",
                "titel": "De aarde vanuit de ruimte",
                "beschrijving": "Bekijk onze planeet."
            },
            {
                "onderwerp": "Maanlanding",
                "titel": "Was de maanlanding echt?",
                "beschrijving": "Ontdek meer over de maan."
            },
            {
                "onderwerp": "Dieren",
                "titel": "Bijzondere dieren",
                "beschrijving": "Ontdek bijzondere dieren."
            }
        ]

        # Van iedere video een post maken
        for video in videos:
            self.posts.append(Post(video))


    def tekenen(self):

        screen.fill((30, 32, 45))

        self.telefoon.tekenen()

        # Titel
        titel = title_font.render(
            "De Fabeltjesfuik", True, (255, 255, 255)
        )
        screen.blit(titel, (175, 100))

        # Posts tekenen
        for i in range(len(self.posts)):

            y = 180 + i * 180 - self.scroll

            self.posts[i].tekenen(y)


    def klikken(self, positie):

        x, y = positie

        for i in range(len(self.posts)):

            post_y = 180 + i * 180 - self.scroll

            # Like knop
            if 140 < x < 250 and post_y + 110 < y < post_y + 155:

                self.posts[i].likes = not self.posts[i].likes

            # Bewaar knop
            if 290 < x < 400 and post_y + 110 < y < post_y + 155:

                self.posts[i].bewaard = not self.posts[i].bewaard


    def starten(self):

        running = True

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                # Scrollen
                if event.type == pygame.MOUSEWHEEL:
                    self.scroll -= event.y * 30
                    self.scroll = max(0, min(self.scroll, 250))

                # Klikken
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.klikken(event.pos)

            self.tekenen()

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        sys.exit()


# SPEL STARTEN
game = Game()
game.starten()
