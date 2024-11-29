import random

def zahlenratespiel():
    print("Willkommen zum Zahlenratespiel!")
    print("Ich denke an eine Zahl zwischen 1 und 100. Kannst du sie erraten?")
    
    # Generiere eine zufällige Zahl zwischen 1 und 100
    geheime_zahl = random.randint(1, 100)
    versuche = 0
    erraten = False

    while not erraten:
        try:
            tipp = int(input("Gib eine Zahl ein: "))
            versuche += 1
            if tipp < geheime_zahl:
                print("Zu niedrig! Versuch es nochmal.")
            elif tipp > geheime_zahl:
                print("Zu hoch! Versuch es nochmal.")
            else:
                print(f"Herzlichen Glückwunsch! Du hast die Zahl {geheime_zahl} nach {versuche} Versuchen erraten!")
                erraten = True
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")

if __name__ == "__main__":
    zahlenratespiel()
