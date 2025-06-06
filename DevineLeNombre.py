import random

def devine_le_nombre():
    print("Bienvenue dans le jeu 'Devine le nombre' !")
    print("Je vais choisir un nombre entre 1 et 100.")
    print("Essayez de le deviner en le moins d'essais possible.\n")
    
    nombre_a_deviner = random.randint(1, 100)
    nombre_essais = 0

    while True:
        try:
            tentative = int(input("Votre tentative : "))
            nombre_essais += 1

            if tentative < nombre_a_deviner:
                print("Trop petit ! Essayez encore.")
            elif tentative > nombre_a_deviner:
                print("Trop grand ! Essayez encore.")
            else:
                print(f"Bravo ! Vous avez deviné le nombre en {nombre_essais} essai(s) !")
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    print("Merci d'avoir joué !")

if __name__ == "__main__":
    devine_le_nombre()
