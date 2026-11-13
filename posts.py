import pygame

class Posts:

    def __init__(self):

        self.data = {

            "video1": {
                "titel": "De aarde is plat",
                "onderwerp": "complottheorieen",
                "tekst": "Sommige mensen geloven dat de aarde plat is.",
                "kleur": (180, 100, 100)
            },

            "video2": {
                "titel": "Gezond eten",
                "onderwerp": "gezondheid",
                "tekst": "Tips om gezonder te eten.",
                "kleur": (100, 180, 100)
            },

            "video3": {
                "titel": "Ruimte en planeten",
                "onderwerp": "ruimte",
                "tekst": "Ontdek bijzondere planeten.",
                "kleur": (100, 100, 180)
            },

            "video4": {
                "titel": "Geheime verhalen",
                "onderwerp": "complottheorieen",
                "tekst": "Er zouden geheimen verborgen worden gehouden.",
                "kleur": (180, 100, 100)
            },

            "video5": {
                "titel": "Sport en beweging",
                "onderwerp": "sport",
                "tekst": "Waarom bewegen goed voor je is.",
                "kleur": (100, 180, 100)
            },

            "video6": {
                "titel": "Het heelal",
                "onderwerp": "ruimte",
                "tekst": "Hoe groot is het heelal eigenlijk?",
                "kleur": (100, 100, 180)
            },

            "video7": {
                "titel": "Gezondheidsgeheimen",
                "onderwerp": "gezondheid",
                "tekst": "Verschillende meningen over gezondheid.",
                "kleur": (180, 150, 80)
            },

            "video8": {
                "titel": "Bijzondere theorieen",
                "onderwerp": "complottheorieen",
                "tekst": "Een video met een opvallende theorie.",
                "kleur": (180, 100, 100)
            },

            "video9": {
                "titel": "Voetbalnieuws",
                "onderwerp": "sport",
                "tekst": "Het laatste nieuws uit de sportwereld.",
                "kleur": (100, 180, 100)
            },

            "video10": {
                "titel": "Nieuwe planeten",
                "onderwerp": "ruimte",
                "tekst": "Wetenschappers ontdekken steeds meer.",
                "kleur": (100, 100, 180)
            }
        }


    def tekenen(self, screen, naam, y):

        video = self.data[naam]

        # Achtergrond van de video
        pygame.draw.rect(
            screen,
            video["kleur"],
            (130, 200 + y, 340, 250)
        )

        # Titel
        font = pygame.font.SysFont(None, 30)
        titel = font.render(video["titel"], True, (255, 255, 255))

        screen.blit(titel, (150, 230 + y))

        # Tekst
        font = pygame.font.SysFont(None, 24)
        tekst = font.render(video["tekst"], True, (255, 255, 255))

        screen.blit(tekst, (150, 290 + y))

        # Onderwerp
        onderwerp = font.render(
            "Onderwerp: " + video["onderwerp"],
            True,
            (255, 255, 255)
        )

        screen.blit(onderwerp, (150, 390 + y))