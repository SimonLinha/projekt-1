ukoly = []  # seznam pro úkoly

def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        if not nazev:
            print("Název úkolu nesmí být prázdný. Zkuste to znovu.")
            continue

        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("Popis úkolu nesmí být prázdný. Zkuste to znovu.")
            continue

        ukol = {"nazev": nazev, "popis": popis}
        ukoly.append(ukol)
        print("Úkol byl úspěšně přidán.")
        break


while True:
    print("\nSprávce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")

    try:
        moznost = int(input("Vyberte možnost (1-4): "))
    except ValueError:
        print("Zadejte platné číslo.")
        continue

    if moznost == 1:
        pridat_ukol()

    elif moznost == 2:
        if not ukoly:
            print("Žádné úkoly nejsou zadány.")
        else:
            print("Seznam úkolů:")
            for i, ukol in enumerate(ukoly, start=1):
                print(f"{i}. {ukol['nazev']} – {ukol['popis']}")

    elif moznost == 3:
        if not ukoly:
            print("Seznam úkolů je prázdný.")
            continue
        print("Seznam úkolů:")
        for i, ukol in enumerate(ukoly, start=1):
            print(f"{i}. {ukol['nazev']} – {ukol['popis']}")
        try:
            cislo = int(input("Zadejte číslo úkolu k odstranění: "))
            if 1 <= cislo <= len(ukoly):
                odstraneny = ukoly.pop(cislo - 1)
                print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
            else:
                print("Neplatné číslo úkolu.")
        except ValueError:
            print("Zadejte platné číslo.")

    elif moznost == 4:
        print("Ukončuji program...")
        break

    else:
        print("Neplatná volba. Zkuste to znovu.")