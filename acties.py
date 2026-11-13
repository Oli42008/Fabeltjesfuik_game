import pygame

class Acties:

    def verwerken(self, event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                return "volgende"

            elif event.key == pygame.K_RIGHT:
                return "volgende"

        elif event.type == pygame.MOUSEWHEEL:

            if event.y < 0:
                return "volgende"

        elif event.type == pygame.MOUSEBUTTONDOWN:

            x = event.pos[0]
            y = event.pos[1]

            # Startknop
            if 200 <= x <= 400 and 500 <= y <= 560:
                return "start"

            # Opnieuw knop
            elif 200 <= x <= 400 and 600 <= y <= 660:
                return "opnieuw"

            # Like knop
            elif 140 <= x <= 230 and 500 <= y <= 545:
                return "like"

            # Opslaan knop
            elif 240 <= x <= 330 and 500 <= y <= 545:
                return "opslaan"

            # Volgende knop
            elif 340 <= x <= 440 and 500 <= y <= 545:
                return "volgende"

        return None