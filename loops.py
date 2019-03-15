"""
Z pętli korzystamy, gdy chcemy aby program wykonywał jakiś fragment kodu kilka razy,
ale nie będziemy tego kodu powielać określoną ilość razy, ponieważ jest to nie optymalne.
Dlatego stosujemy pętle, które jak sama nazwa wskazuje, zapętlają fragment kodu i wykonują
go określoną ilość razy (dla pętli for) lub do czasu gdy spełni się jakiś warunek logiczny (dla pętli while).
"""


def main():
    for i in range(0, 10):
        print(i)
    """
    # Kod poniżej wykorzystuje pętlę for, aby liczyć średnią ocen, wystarczy go odkomentować
    print("Podaj liczbę ocen, które będą wchodzić w skład średniej")
    liczba_ocen = int(input())
    suma = 0
    for i in range(1, liczba_ocen + 1):
        print("Podaj ocenę " + str(i))
        ocena = float(input())
        suma += ocena
    print("Suma ocen to " + str(suma))
    print("średnia ocen to " + str(suma / liczba_ocen))
    """
    i = 0
    while i < 10:
        print(i)
        i += 1

    """
    # Kod poniżej wykorzustuje pętlę while, aby liczyć średnią ocen, wystarczy go odkomentować
    print("Podaj liczbę ocen, które będą wchodzić w skład średniej")
    liczba_ocen = int(input())
    suma = 0
    i = 1
    while i <= liczba_ocen:
        print("Podaj ocenę " + str(i))
        ocena = float(input())
        suma += ocena
        i += 1
    print("Suma ocen to " + str(suma))
    print("średnia ocen to " + str(suma / liczba_ocen))
    """

if __name__ == "__main__":
    main()