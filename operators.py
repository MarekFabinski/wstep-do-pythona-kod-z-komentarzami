"""
Gdy wypisujemy tekst do konsoli i składa się on z paru części połączonych ze sobą plusem
musimy pamiętać, że każda składowa musi być tekstem, aby konkatenacja się odbyła.
Dlatego w przykładzie poniżej dokonujemy konwersji zmiennej suma, która jest typem int,
na typ str (string).
"""

def main():
    x = 7
    y = 3

    suma = x + y
    print("Wynik dodawania: " + str(suma))

    roznica = x - y
    print("Wynik odejmowania: " + str(roznica))

    iloczyn = x * y
    print("Wynik mnożenia: " + str(iloczyn))

    iloraz = x / y
    print("Wynik dzielenia: " + str(iloraz))

    reszta = x % y
    print("Reszta z dzielenia: " + str(reszta))

    """
    W Pythonie występują operatory łączone +=, -=, *=, /=, %=
    Powiedzmy, że mamy zmienną: z = 5
    Chcemy zwiększyć jej wartość o 5, więc logicznym byłoby zapisanie z = z + 5
    Jednak rzadko stosuje się taki zapis, więc zapiszemy to w taki sposób: z += 5, 
    który robi to samo, czyli dodaje do zmiennej 'z' liczbę 5  
    """
    z = 5
    z += 5
    print(z)    # W konsoli wyświetli się nam wartość 10

    """
    Operatory porównań, tak jak na matematyce: >, >=, <, <=, != (ten zapis oznacza, że wartość po lewej nie równa się wartości po prawej)
    oraz == (podwójny znak == porównuje wartości po lewej i po prawej, podczas gdy pojedynczy znak = przypisuje wartość po prawej do zmiennej,
    która jest po lewej. Operatory porównań zwracają wartości True or False. Poniżej prezentacja działania.
    """

    print(str(x) + "<" + str(y) + " == " + str(x < y))
    print(str(x) + "<=" + str(y) + " == " + str(x <= y))
    print(str(x) + ">" + str(y) + " == " + str(x > y))
    print(str(x) + ">=" + str(y) + " == " + str(x >= y))
    print(str(x) + "==" + str(y) + " == " + str(x == y))
    print(str(x) + "!=" + str(y) + " == " + str(x != y))


if __name__ == "__main__":
    main()
