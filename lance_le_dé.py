import random
import time

    # Variable pour Rejouer

replay = True

    # Initalisations:

value_of_de = random.randint(1,6)

    # Vérifications:

while replay == True:
    paris = input("Voulez vous parrier sur un chiffre du dé? (y/n): ")
    if paris == "y":
        choice = int(input("Veuillez entrer le chiffre que vous pensez (1-6): "))
        print("...")
        time.sleep(1)
        if choice == value_of_de:
            print(f"""Voici le résultat du dé: {value_of_de}
            Vous aviez parier sur {choice}.
            Vous avez donc raison ! Bravo""")
        else:
            print(f"""Voici le résultat du dé: {value_of_de}
            Vous aviez parier sur {choice}.
            Vous n'avez donc pas raison ! Une prochaine fois...""")
    elif paris == "n":
        print("...")
        time.sleep(1)
        print(f"Voici le résultat du dé: {value_of_de}")
    else:
        print("Erreur")

        # Rejouer:

    replay = input("""Rejouer ? (y/n) 
    [>] """)
    if replay == "y":
        replay = True
    elif replay == "n":
        replay = False
    else:
        print("Erreur.")
        replay == False