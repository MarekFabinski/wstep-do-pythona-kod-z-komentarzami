def main():
    logiczna = True
    print(type(logiczna))       # w konsoli wyświetli się <class 'bool'> co oznacza, że zmienna jest zmienną logiczną bool

    calkowita = -7
    print(type(calkowita))      # <class 'int'> oznacza, że zmienna jest liczbą całkowitą int (skrót od integer)

    zmiennopozycyjna = -7.4
    print(type(zmiennopozycyjna))   # <class 'float'> zmienna jest liczbą zmiennopozycyjną float

    zespolona = -7.4 + 8.4j
    print(type(zespolona))      # <class 'complex'> zmienna jest liczbą zespoloną complex (pamiętać, że w Pythonie część urojona to j, a nie i)

    napis = "Ala ma kota"       # równie dobrze napisem może być "6+7j"
    print(type(napis))          # <class 'str'> zmienna jest napisem str (skrót od string)

    print(float(5))             # konwersja int na float

    print(int(5.0))             # konwersja float na int

    print(int(5.7))             # konwersja float na int. Na tym przykładzie widać, że nie zachodzi zaokrąglenie liczby, a tylko obcięcie wartości po przecinku.

    print(float("5.7"))         # konwersja str na float

    text = str(-5.3)            # konwersja int na str i przypisanie tej wartości (tekstu) do zmiennej
    print(text)
    print(type(text))           # sprawdzenie, że -5.3 jest faktycznie tekstem


if __name__ == "__main__":
    main()
