"""
Créé par Dorian Bernaquez Girard, Groupe 402
Classifier le caractère comme NPC, Kobold, ou Héros.
"""
import random
import time
from dataclasses import dataclass
from enum import Enum

sacados = True


class Alignement(Enum):
    LawfulGood = 1
    NeutralGood = 2
    ChaoticGood = 3
    LawfulNeutral = 4
    Neutral = 5
    ChaoticNeutral = 6
    LawfulEvil = 7
    NeutralEvil = 8
    ChaoticEvil = 9
    null = 10


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
        self.alignement = 0
        self.des = []
        self.vivant = True
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

    def est_vivant(self):
        if self.hp <= 0:
            self.vivant = False
            print(f"Le caractère n'est plus vivant.")
        else:
            pass


non_joueur = NPC()
joueur = NPC()


class Kobold(NPC):
    def __init__(self):
        super().__init__()
        self.dmg = None
        self.d20 = None
        self.cible = None
        self.vivant = True

    def attaquer(self, cible):
        self.d20 = random.randint(1, 20)
        if self.d20 == 20:
            hp_loss = random.randint(1, 8)
            cible.subir_dommage(hp_loss)
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
                cible.subir_dommage(dommage)
            if self.d20 <= cible.armure:
                print(f"*Swoosh!* Vous manquez l'attaque! Il a encore {cible.hp} points de vie.")

    def subir_dommage(self, dmg):
        self.hp -= dmg


class Heros(NPC):
    def __init__(self):
        super().__init__()
        self.dmg = None
        self.cible = None
        self.d20 = None
        self.vivant = True

    def subir_dommage(self, dmg):
        self.hp -= dmg

    def attaquer(self, cible):
        self.d20 = random.randint(1, 20)

        if self.d20 == 20:
            hp_loss = random.randint(1, 8)
            cible.subir_dommage(hp_loss)
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
                cible.subir_dommage(dommage)
            if self.d20 <= cible.armure:
                print(f"*Swoosh!* Vous manquez l'attaque! Il a encore {cible.hp} points de vie.")


@dataclass
class Item:
    qte = int
    nom_item = str


class SacADos(Item):
    def __init__(self):
        super().__init__()
        self.liste_item = []
        nom_item = self.nom_item
        qte = self.qte
        print(f"test: {nom_item}, {qte}")

    def ajouter_item(self, nom, qte_item):
        nom_item = self.nom_item
        qte = qte_item
        nouveau_qte = qte + qte_item
        if self.liste_item.__contains__(nom_item):
            print(f"test: {self.liste_item}, {nouveau_qte}")
            pass
        else:
            self.liste_item.append(nom)
            print(f"test: {self.liste_item}, {nouveau_qte}")


kobold_joueur = Kobold()
heros_joueur = Heros()

heros_joueur.attaquer(kobold_joueur)
kobold_joueur.attaquer(heros_joueur)
heros_joueur.est_vivant()
kobold_joueur.est_vivant()

sac = SacADos()
sac.ajouter_item("Or", 15)
sac.ajouter_item("Or", 15)
