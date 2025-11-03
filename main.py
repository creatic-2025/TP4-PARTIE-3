"""
Créé par Dorian Bernaquez Girard, Groupe 402
Classifier le caractère comme NPC, Kobold, ou Héros.
"""
import random
import time


class NPC:
    def __init__(self):
        self.force = None
        self.agilite = None
        self.constitution = None
        self.intelligence = None
        self.sagesse = None
        self.charisme = None
        self.armure = None
        self.nom = None
        self.race = None
        self.espece = None
        self.hp = None
        self.profession = None
        self.des = []
        self.roulement_des()

    def roulement_des(self):
        def dice():
            des = []
            des_trois_plus_hautes = 0
            for i in range(4):
                des.append(random.randint(1, 6))
                des.sort()
                des_trois_plus_hautes = des[1:]
            return sum(des_trois_plus_hautes)

        self.force = dice()
        self.agilite = dice()
        self.constitution = dice()
        self.intelligence = dice()
        self.sagesse = dice()
        self.charisme = dice()
        self.armure = random.randint(1, 12)
        races = ["Kobold", "Heros"]
        self.race = random.choice(races)
        noms = ["Dian", "Nese", "Falledrick", "Mae", "Valhein", "Dol", "Earl", "Cedria", "Azulei", "Yun", "Cybel",
                "Ina", "Foolly", "Skili", "Juddol", "Janver"]
        self.nom = random.choice(noms)
        especes = ["Monstre", "Humain"]
        self.espece = random.choice(especes)
        self.hp = random.randint(1, 20)
        professions = ["Guerrier", "Voleur", "Menuisier", "Cuisinier"]
        self.profession = random.choice(professions)

    def afficher_caracteristiques(self):
        print(f"Espèce: {self.espece}\nRace: {self.race}\nNom: {self.nom}\nPoints de vie: {self.hp}\n"
              f"Force: {self.force}"
              f""
              f"\nAgilité: {self.agilite}\nConstitution: {self.constitution}\nIntelligence: {self.intelligence}"
              f"\nSagesse: {self.sagesse}\nCharisme: {self.charisme}\nArmure: {self.armure}")


non_joueur = NPC()
joueur = NPC()


class Kobold(NPC):
    def __init__(self):
        super().__init__()
        self.dmg = None
        self.d20 = None
        self.cible = None

    def attaquer(self, cible):
        self.d20 = random.randint(1, 20)
        if self.d20 == 20:
            hp_loss = random.randint(1, 8)
            cible.subir_dommage()
            time.sleep(1)
            print(f"*Slash!* Un attaque critique! Vouz endommagez le cible de {hp_loss}. Il a maintenant {cible.hp}"
                  f"")
        elif self.d20 == 1:
            time.sleep(1)
            print(f"*Swoosh!* Vous manquez l'attaque! Il a encore {cible.hp} points de vie.")
        else:
            if self.d20 >= cible.armure:
                dommage = random.randint(1, 6)
                print(f"*Slash!* Vous réuississez à causé {dommage} dégats. L'adversaire a {cible.hp}"
                      f" points de vie.")
                cible.subir_dommage()
            if self.d20 <= cible.armure:
                print(f"*Swoosh!* Vous manquez l'attaque! Il a encore {cible.hp} points de vie.")

    def subir_dommage(self, dmg):
        self.hp -= dmg
        joueur_kobold = joueur
        joueur_kobold.hp -= self.dmg


class Heros(NPC):
    def __init__(self):
        super().__init__()
        self.dmg = None
        self.cible = None
        self.d20 = None

    def attaquer(self, cible):
        self.d20 = random.randint(1, 20)

        if self.d20 == 20:
            hp_loss = random.randint(1, 8)
            cible.subir_dommage()
            time.sleep(1)
            print(f"*Slash!* Un attaque critique! Vouz endommagez le cible de {hp_loss}. Il a maintenant {cible.hp}"
                  f"")
        elif self.d20 == 1:
            time.sleep(1)
            print(f"*Swoosh!* Vous manquez l'attaque! Il a encore {cible.hp} points de vie.")
        else:
            if self.d20 >= cible.armure:
                dommage = random.randint(1, 6)
                print(f"*Slash!* Vous réuississez à causé {dommage} dégats. L'adversaire a {cible.hp}"
                      f" points de vie.")
                cible.subir_dommage()
            if self.d20 <= cible.armure:
                print(f"*Swoosh!* Vous manquez l'attaque! Il a encore {cible.hp} points de vie.")

    def subir_dommage(self):
        self.dmg = random.randint(1, 6)
        joueur_heros = joueur
        joueur_heros.hp -= self.dmg


kobold_joueur = Kobold()
heros_joueur = Heros()

heros_joueur.attaquer(kobold_joueur)
kobold_joueur.attaquer(heros_joueur)
