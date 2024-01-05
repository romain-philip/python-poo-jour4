class Rectangle:
    def __init__(self, longueur=1, largeur=1):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur



rectangle = Rectangle(3, 4)


print(f"Longueur: {rectangle.get_longueur()}")
print(f"Largeur: {rectangle.get_largeur()}")
print(f"Périmètre: {rectangle.perimetre()}")
print(f"Surface: {rectangle.surface()}")
