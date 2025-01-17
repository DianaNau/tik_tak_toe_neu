def zeichne_spielfeld(spielfeld):
    for reihe in spielfeld:
        print(" | ".join(reihe))
        print("-" * 9)

def ist_spielfeld_voll(spielfeld):
    for reihe in spielfeld:
        if " " in reihe:
            return False
    return True

def ueberpruefe_gewinner(spielfeld):
    for reihe in spielfeld:
        if reihe[0] == reihe[1] == reihe[2] != " ":
            return reihe[0]
    
    for spalte in range(3):
        if spielfeld[0][spalte] == spielfeld[1][spalte] == spielfeld[2][spalte] != " ":
            return spielfeld[0][spalte]

    if spielfeld[0][0] == spielfeld[1][1] == spielfeld[2][2] != " ":
        return spielfeld[0][0]
    if spielfeld[0][2] == spielfeld[1][1] == spielfeld[2][0] != " ":
        return spielfeld[0][2]

    return None

def starte_spiel():
    spielfeld = [[" " for _ in range(3)] for _ in range(3)]
    aktueller_spieler = "X"

    while True:
        zeichne_spielfeld(spielfeld)
        print(f"--- Spieler {aktueller_spieler} ist an der Reihe ---")

        while True:
            try:
                zeile = int(input("Wähle die Zeile (1-3): ")) - 1
                spalte = int(input("Wähle die Spalte (1-3): ")) - 1

                if zeile < 0 or zeile > 2 or spalte < 0 or spalte > 2:
                    print("Ungültige Eingabe. Bitte wähle eine Zahl zwischen 1 und 3.")
                    continue

                if spielfeld[zeile][spalte] != " ":
                    print("Das Feld ist bereits belegt. Versuche es erneut.")
                    continue

                spielfeld[zeile][spalte] = aktueller_spieler
                
                gewinner = ueberpruefe_gewinner(spielfeld)
                if gewinner:
                    zeichne_spielfeld(spielfeld)
                    print(f"Spieler {gewinner} hat gewonnen!")
                    return
                
                if ist_spielfeld_voll(spielfeld):
                    print("Das Spielfeld ist voll! Das Spiel endet unentschieden.")
                    return
                
                aktueller_spieler = "O" if aktueller_spieler == "X" else "X"
                break  

            except ValueError:
                print("Ungültige Eingabe. Bitte gib eine Zahl zwischen 1 und 3 ein.")

starte_spiel()
