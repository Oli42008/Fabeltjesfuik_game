import pygame

class Telefoon:

    def tekenen(self, screen):

        # Rand van de telefoon
        pygame.draw.rect(
            screen,
            (20, 20, 20),
            (100, 100, 400, 600),
            8,
            border_radius=35
        )

        # Bovenste luidspreker
        pygame.draw.rect(
            screen,
            (20, 20, 20),
            (260, 110, 80, 8),
            border_radius=5
        )

        # Onderste knop
        pygame.draw.circle(
            screen,
            (20, 20, 20),
            (300, 680),
            10,
            3
        )