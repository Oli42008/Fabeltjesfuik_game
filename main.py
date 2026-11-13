import pygame
import sys
import random

import posts
import algoritme
import telefoon
import acties
import eindscherm


class Game:

    def __init__(self):

        pygame.init()

        self.WIDTH = 600
        self.HEIGHT = 800

        self.screen = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT)
        )

        pygame.display.set_caption("De Fabeltjesfuik")

        self.clock = pygame.time.Clock()

        # Andere classes aanmaken
        self.telefoon = telefoon.Telefoon()
        self.posts = posts.Posts()
        self.algoritme = algoritme.Algoritme()
        self.acties = acties.Acties()
        self.eindscherm = eindscherm.Eindscherm()

        # Begin bij het startscherm
        self.scherm = "start"

        self.video_lijst = []
        self.index = 0

        self.start_tijd = 0

        self.laatste_video = None

        self.score = 0


    # Start een nieuw spel
    def nieuw_spel(self):

        self.algoritme = algoritme.Algoritme()

        # Kies eerst 3 willekeurige video's
        alle_videos = list(self.posts.data.keys())

        self.video_lijst = random.sample(alle_videos, 3)

        self.index = 0

        self.start_tijd = pygame.time.get_ticks()

        self.scherm = "spel"


    # Achtergrond tekenen
    def achtergrond_tekenen(self):

        self.screen.fill((235, 230, 220))

        # Extra achtergrondkleur
        pygame.draw.rect(
            self.screen,
            (215, 210, 200),
            (0, 0, 600, 800)
        )


    # Startscherm tekenen
    def startscherm_tekenen(self):

        self.achtergrond_tekenen()

        titel_font = pygame.font.SysFont(None, 60)
        tekst_font = pygame.font.SysFont(None, 28)

        titel = titel_font.render(
            "De Fabeltjesfuik",
            True,
            (30, 30, 30)
        )

        self.screen.blit(titel, (120, 200))

        uitleg = [
            "Welkom bij De Fabeltjesfuik!",
            "Je gaat video's bekijken op een sociaal",
            "mediaplatform.",
            "",
            "Het algoritme kijkt naar jouw gedrag.",
            "Wat je liket, opslaat en lang bekijkt,",
            "kan invloed hebben op de video's die je",
            "daarna te zien krijgt.",
            "",
            "Na 10 video's krijg je jouw fuikscore."
        ]

        y = 300

        for regel in uitleg:

            tekst = tekst_font.render(
                regel,
                True,
                (30, 30, 30)
            )

            self.screen.blit(tekst, (100, y))

            y += 30

        # Startknop
        pygame.draw.rect(
            self.screen,
            (70, 140, 180),
            (200, 500, 200, 60),
            border_radius=12
        )

        knop_font = pygame.font.SysFont(None, 35)

        knop_tekst = knop_font.render(
            "START",
            True,
            (255, 255, 255)
        )

        self.screen.blit(knop_tekst, (265, 518))


    # Knoppen tekenen
    def knoppen_tekenen(self):

        font = pygame.font.SysFont(None, 25)

        # Like
        pygame.draw.rect(
            self.screen,
            (210, 80, 100),
            (140, 500, 90, 45),
            border_radius=8
        )

        tekst = font.render("Like", True, (255, 255, 255))
        self.screen.blit(tekst, (160, 513))

        # Opslaan
        pygame.draw.rect(
            self.screen,
            (80, 130, 180),
            (240, 500, 90, 45),
            border_radius=8
        )

        tekst = font.render("Opslaan", True, (255, 255, 255))
        self.screen.blit(tekst, (245, 513))

        # Volgende
        pygame.draw.rect(
            self.screen,
            (70, 150, 100),
            (340, 500, 100, 45),
            border_radius=8
        )

        tekst = font.render("Volgende", True, (255, 255, 255))
        self.screen.blit(tekst, (345, 513))


    # Spelscherm tekenen
    def spelscherm_tekenen(self):

        self.achtergrond_tekenen()

        naam = self.video_lijst[self.index]

        # Video tekenen
        self.posts.tekenen(
            self.screen,
            naam,
            0
        )

        # Teller
        font = pygame.font.SysFont(None, 30)

        teller = font.render(
            "Video " + str(self.index + 1) + " van 10",
            True,
            (30, 30, 30)
        )

        self.screen.blit(teller, (220, 150))

        # Knoppen tekenen
        self.knoppen_tekenen()

        # Telefoon als laatste tekenen
        self.telefoon.tekenen(self.screen)


    # Naar de volgende video
    def volgende_video(self):

        naam = self.video_lijst[self.index]

        # Bereken hoe lang de speler heeft gekeken
        einde_tijd = pygame.time.get_ticks()

        seconden = (einde_tijd - self.start_tijd) / 1000

        self.algoritme.tijd_opslaan(naam, seconden)

        # Video als bekeken opslaan
        self.algoritme.post_bekeken(naam)

        # Als er 10 video's bekeken zijn
        if len(self.algoritme.bekeken) >= 10:

            self.score = self.algoritme.diepte_berekenen(self.posts)

            self.scherm = "einde"

        else:

            # Eerst de 3 willekeurige video's afmaken
            if self.index < 2:

                self.index += 1

            else:

                # Daarna video's kiezen met het algoritme
                nieuwe_video = self.algoritme.kies_volgende(self.posts)

                if nieuwe_video is not None:

                    self.video_lijst.append(nieuwe_video)
                    self.index += 1

            # Start de kijktijd van de nieuwe video
            self.start_tijd = pygame.time.get_ticks()


    # Klikken verwerken
    def klik_verwerken(self, actie):

        if self.scherm == "start":

            if actie == "start":
                self.nieuw_spel()

        elif self.scherm == "spel":

            naam = self.video_lijst[self.index]

            onderwerp = self.posts.data[naam]["onderwerp"]

            if actie == "like":

                self.algoritme.like(naam)

            elif actie == "opslaan":

                self.algoritme.opslaan(naam)

            elif actie == "volgende":

                self.volgende_video()

        elif self.scherm == "einde":

            if actie == "opnieuw":
                self.nieuw_spel()


    # Het spel starten
    def starten(self):

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

            actie = self.acties.verwerken(event)

            if actie is not None:
                self.klik_verwerken(actie)

            # Welk scherm moet getekend worden?
            if self.scherm == "start":

                self.startscherm_tekenen()

            elif self.scherm == "spel":

                self.spelscherm_tekenen()

            elif self.scherm == "einde":

                self.eindscherm.tekenen(
                    self.screen,
                    self.score,
                    self.algoritme,
                    self.posts
                )

            pygame.display.flip()

            self.clock.tick(60)


# Game starten
game = Game()
game.starten()