import random
import time
from colorama import Fore, init

init()

    # Variable pour Rejouer

replay = True

while replay == True:

        # Initalisations:

    value_of_de = random.randint(1,6)
    paris = input(Fore.MAGENTA + "Voulez vous parrier sur un chiffre du dé? (y/n): ")

        # Vérifications:

    if paris == "y":
        choice = int(input("Veuillez entrer le chiffre que vous pensez (1-6): "))
        print("...")
        time.sleep(1)
        if choice == value_of_de:
            print(Fore.LIGHTGREEN_EX + f"""Voici le résultat du dé: {value_of_de}
            Vous aviez parier sur {choice}.
            Vous avez donc raison ! Bravo""")
        else:
            print(Fore.LIGHTRED_EX + f"""Voici le résultat du dé: {value_of_de}
            Vous aviez parier sur {choice}.
            Vous n'avez donc pas raison ! Une prochaine fois...""")
    elif paris == "n":
        print("...")
        time.sleep(1)
        print(Fore.LIGHTGREEN_EX + f"Voici le résultat du dé: {value_of_de}")
    else:
        print(Fore.LIGHTRED_EX + "Erreur")

        # Rejouer:

    replay = input("""Rejouer ? (y/n) 
    [>] """)
    if replay == "y":
        replay = True
    elif replay == "n":
        replay = False
    else:
        print(Fore.LIGHTRED_EX + "Erreur.")
        replay == False
