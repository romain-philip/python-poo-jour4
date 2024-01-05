import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = [Carte(valeur, couleur) for valeur in range(1, 14) for couleur in ['Coeur', 'Carreau', 'Trefle', 'Pique']]

    def tirer_carte(self):
        return self.paquet.pop(random.randint(0, len(self.paquet) - 1))

    def valeur_carte(self, carte):
        if carte.valeur > 10:
            return 10
        elif carte.valeur == 1:
            return 11 if input("Voulez-vous que l'as vaille 1 ou 11 ? ") == "11" else 1
        else:
            return carte.valeur

    def jouer(self):
        joueur = [self.tirer_carte() for _ in range(2)]
        croupier = [self.tirer_carte() for _ in range(2)]

        while sum(self.valeur_carte(carte) for carte in joueur) < 21 and input("Voulez-vous tirer une carte ? (Oui/Non) ").lower() == "oui":
            joueur.append(self.tirer_carte())

        while sum(self.valeur_carte(carte) for carte in croupier) < 17:
            croupier.append(self.tirer_carte())

        score_joueur = sum(self.valeur_carte(carte) for carte in joueur)
        score_croupier = sum(self.valeur_carte(carte) for carte in croupier)

        print(f"Votre score : {score_joueur}, Score du croupier : {score_croupier}")

        if score_joueur > 21:
            print("Vous avez perdu")
        elif score_croupier > 21 or score_joueur > score_croupier:
            print("Vous avez gagné")
        else:
            print("Le croupier a gagné")


jeu = Jeu()
jeu.jouer()
