import pygame

class Eindscherm:

    def tekenen(self, screen, score, algoritme, posts):

        screen.fill((235, 230, 220))

        titel_font = pygame.font.SysFont(None, 45)
        tekst_font = pygame.font.SysFont(None, 27)

        titel = titel_font.render(
            "Jouw resultaat",
            True,
            (30, 30, 30)
        )

        screen.blit(titel, (200, 100))

        # Score tonen
        score_tekst = tekst_font.render(
            "Je fuikscore is: " + str(score) + "%",
            True,
            (30, 30, 30)
        )

        screen.blit(score_tekst, (200, 180))

        # Uitleg over de score
        if score >= 70:

            uitleg = "Je bent sterk in een filterbubbel terechtgekomen."

        elif score >= 40:

            uitleg = "Je bent gedeeltelijk in een filterbubbel terechtgekomen."

        else:

            uitleg = "Je feed bleef redelijk gevarieerd."

        tekst = tekst_font.render(uitleg, True, (30, 30, 30))
        screen.blit(tekst, (70, 240))

        # Zoek het meest bekeken onderwerp
        onderwerpen = {}

        for naam in algoritme.bekeken:

            onderwerp = posts.data[naam]["onderwerp"]

            if onderwerp not in onderwerpen:
                onderwerpen[onderwerp] = 0

            onderwerpen[onderwerp] += 1

        beste_onderwerp = "geen"

        for onderwerp in onderwerpen:

            if beste_onderwerp == "geen":
                beste_onderwerp = onderwerp

            elif onderwerpen[onderwerp] > onderwerpen[beste_onderwerp]:
                beste_onderwerp = onderwerp

        # Extra uitleg
        uitleg2 = "Je keek het meest naar: " + beste_onderwerp
        tekst2 = tekst_font.render(uitleg2, True, (30, 30, 30))
        screen.blit(tekst2, (70, 310))

        # Likes en opgeslagen video's
        tekst3 = tekst_font.render(
            "Aantal likes: " + str(len(algoritme.likes)),
            True,
            (30, 30, 30)
        )

        screen.blit(tekst3, (70, 370))

        tekst4 = tekst_font.render(
            "Aantal opgeslagen: " + str(len(algoritme.opgeslagen)),
            True,
            (30, 30, 30)
        )

        screen.blit(tekst4, (70, 410))

        # Uitleg over hoe de fuik is ontstaan
        if len(onderwerpen) == 1:

            uitleg3 = "Je hebt maar een soort onderwerp gezien."

        elif len(onderwerpen) == 2:

            uitleg3 = "Je hebt vooral een paar onderwerpen gezien."

        else:

            uitleg3 = "Je hebt verschillende onderwerpen gezien."

        tekst5 = tekst_font.render(uitleg3, True, (30, 30, 30))
        screen.blit(tekst5, (70, 470))

        # Opnieuw knop
        pygame.draw.rect(
            screen,
            (70, 140, 180),
            (200, 600, 200, 60),
            border_radius=12
        )

        knop_tekst = tekst_font.render(
            "Opnieuw spelen",
            True,
            (255, 255, 255)
        )

        screen.blit(knop_tekst, (220, 620))