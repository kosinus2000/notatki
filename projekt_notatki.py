def dodaj_notatke():
    notatka = input("Dodaj swoja notatke: ")
    file = open("notatki.txt", 'a', encoding='utf-8')
    file.write(notatka + '\n')
    file.close()


def wyswietl_notatke():
    print()
    try:

        file = open("notatki.txt")
        notatki = file.readlines()
        if notatki:
            i = 1
            for n in notatki:
                print(f"Numer notatki: {i}:")
                print(f"{n}")
                i += 1
        else:
            print("Brak notatek!")
    except FileNotFoundError:
        print("Usunales windowsa")


def usun_notatki():
    try:
        numer_notatki = int(input(("Podaj numer notatki: "))) - 1

        file = open("notatki.txt", 'r', encoding='utf-8')

        notatki = file.readlines()

        if numer_notatki <= len(notatki):
            notatki.pop(numer_notatki)

            file = open("notatki.txt", 'w', encoding='utf-8')
            file.writelines(notatki)
            print("Notatka usunieta :)\n")
        else:
            print("Nieprawidlowy numer notatki")

    except ValueError:
        print("Prosze podac liczbe")
    except FileNotFoundError:
        print("Usunales windowsa")


def main():
    print("\nWitam w programie zarzadzajacym notatkami.")
    while True:
        try:

            print("1. Dodaj notatke.")
            print("2. Wyswietl notatki.")
            print("3. Usun notatki.")
            print("4. Zamknij program.")

            numer = int(input("Podaj liczbe: "))

            if numer == 1:
                dodaj_notatke()
            elif numer == 2:
                wyswietl_notatke()
            elif numer == 3:
                usun_notatki()
            elif numer == 4:
                print("Zamykanie programu")
                break
            else:
                print("Blad! Podaj numer z przedzialu 1 - 4!")

        except ValueError:
            print("Podaj liczbe!")


if __name__ == "__main__":
    main()
