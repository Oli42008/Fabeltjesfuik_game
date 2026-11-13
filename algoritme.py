import random

class Algoritme:

    def __init__(self):

        self.bekeken = []
        self.likes = []
        self.opgeslagen = []
        self.kijktijd = {}

        self.aanbevolen = None


    # Houdt bij welke video bekeken is
    def post_bekeken(self, naam):

        if naam not in self.bekeken:
            self.bekeken.append(naam)


    # Houdt likes bij
    def like(self, naam):

        if naam in self.likes:
            self.likes.remove(naam)
        else:
            self.likes.append(naam)


    # Houdt opgeslagen video's bij
    def opslaan(self, naam):

        if naam in self.opgeslagen:
            self.opgeslagen.remove(naam)
        else:
            self.opgeslagen.append(naam)


    # Slaat de kijktijd op
    def tijd_opslaan(self, naam, seconden):

        self.kijktijd[naam] = seconden


    # Kijkt welk onderwerp de meeste interesse krijgt
    def interessant_onderwerp(self, posts):

        scores = {}

        # Begin met 0 punten voor ieder onderwerp
        for naam in posts.data:

            onderwerp = posts.data[naam]["onderwerp"]

            if onderwerp not in scores:
                scores[onderwerp] = 0

        # Lang kijken geeft punten
        for naam in self.kijktijd:

            onderwerp = posts.data[naam]["onderwerp"]

            if self.kijktijd[naam] >= 5:
                scores[onderwerp] += 2

        # Een like geeft punten
        for naam in self.likes:

            onderwerp = posts.data[naam]["onderwerp"]
            scores[onderwerp] += 3

        # Opslaan geeft extra punten
        for naam in self.opgeslagen:

            onderwerp = posts.data[naam]["onderwerp"]
            scores[onderwerp] += 4

        # Zoek het onderwerp met de meeste punten
        beste_onderwerp = None
        hoogste_score = -1

        for onderwerp in scores:

            if scores[onderwerp] > hoogste_score:
                hoogste_score = scores[onderwerp]
                beste_onderwerp = onderwerp

        return beste_onderwerp


    # Kiest de volgende video
    def kies_volgende(self, posts):

        onderwerp = self.interessant_onderwerp(posts)

        mogelijkheden = []

        for naam in posts.data:

            if naam not in self.bekeken:

                video_onderwerp = posts.data[naam]["onderwerp"]

                if video_onderwerp == onderwerp:
                    mogelijkheden.append(naam)

        # Als er video's over het onderwerp zijn
        if len(mogelijkheden) > 0:
            self.aanbevolen = random.choice(mogelijkheden)

        # Anders kiest het algoritme een willekeurige video
        else:

            mogelijkheden = []

            for naam in posts.data:

                if naam not in self.bekeken:
                    mogelijkheden.append(naam)

            if len(mogelijkheden) > 0:
                self.aanbevolen = random.choice(mogelijkheden)

        return self.aanbevolen


    # Bereken de fuikscore
    def diepte_berekenen(self, posts):

        onderwerpen = {}

        for naam in self.bekeken:

            onderwerp = posts.data[naam]["onderwerp"]

            if onderwerp not in onderwerpen:
                onderwerpen[onderwerp] = 0

            onderwerpen[onderwerp] += 1

        hoogste_aantal = 0

        for onderwerp in onderwerpen:

            if onderwerpen[onderwerp] > hoogste_aantal:
                hoogste_aantal = onderwerpen[onderwerp]

        # Het meest bekeken onderwerp bepaalt de basis van de score
        score = hoogste_aantal * 10

        # Likes en opgeslagen video's verhogen de score een beetje
        score += len(self.likes) * 2
        score += len(self.opgeslagen) * 2

        if score > 100:
            score = 100

        return score