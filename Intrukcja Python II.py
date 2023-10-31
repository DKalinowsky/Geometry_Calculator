import math
print('Witaj w programie do obliczania objetosci, masy i pola powieszchni wybranych figur.')
print('Dostepne figury to: 1. Kula, 2. Czworoscian foremny, 3. Elipsoda, 4. Ostroslup prosty o podstawie prostokatnej, 5. Stozek, 6. Walec')
figura = int(input('Wybierz numer wybranej figury: '))
if figura == 1:
    print('Wybrana figura to kula.')
    print('Dostepne wlasciwosci do obliczenia to 1. Objetosc, 2. Masa, 3. Pole powierzchni')
    wartosc = int(input('Wybierz numer wartosci ktora chcesz policzyc: '))
    if wartosc == 1:
        print('Wybrano objetosc kuli')
        r1 = float(input('Podaj wartosc promienia kuli: '))
        if r1 <= 0:
            print('Wartosc promienia kuli musi byc dodatnia')
            quit()


        def objkuli(r1):
            wynik = (4 / 3 * r1 ** 3) * math.pi
            return wynik


        print(str('Objetosc kuli o promieniu ') + str(r1) + str(' wynosi: '), end='')
        print(str(objkuli(r1)), str(' jednostek szesciennych'))

    if wartosc == 2:
        print('Wybrano mase kuli')
        d1 = float(input('Podaj gestosc kuli: '))
        v1 = float(input('Podaj objetosc kuli: '))
        if d1 <= 0:
            print('Gestosc kuli musi byc dodatnia')
            quit()
        if v1 <= 0:
            print('Objetosc kuli musi byc dodatnia')
            quit()


        def masakuli(d1, v1):
            wynik = d1 * v1
            return wynik


        print(str('Masa kuli o gestosci ') + str(d1) + str(' i objetosci ') + str(v1) + str(' wynosi: '), end='')
        print(str(masakuli(d1, v1)), str('jednostek masowych'))

    if wartosc == 3:
        print('Wybrano pole powierzchni kuli')
        r1 = float(input('Podaj wartosc promienia kuli: '))
        if r1 <= 0:
            print('Gestosc kuli musi byc dodatnia')
            quit()


        def polekuli(r1):
            wynik = (4 * r1 ** 2) * math.pi
            return wynik


        print(str('Pole kuli o promieniu ') + str(r1) + str(' wynosi: '), end='')
        print(str(polekuli(r1)), str('jednostek kwadratowych'))

if figura == 2:
    print('Wybrana figura to czworoscian foremny.')
    print('Dostepne wlasciwosci do obliczenia to 1. Objetosc, 2. Masa, 3. Pole powierzchni')
    wartosc2 = int(input('Wybierz numer wartosci ktora chcesz policzyc: '))
    if wartosc2 == 1:
        print('Wybrano objetosc czworoscianu foremnego')
        a1 = float(input('Podaj wartosc boku czworoscianu foremnego: '))
        if a1 <= 0:
            print('Dlugosc musis byc dodatnia')
            quit()


        def objczwfor(a1):
            wynik = (a1 ** 3 * math.sqrt(2)) / 12
            return wynik


        print(str('Objetosc czworoscianu foremnego o boku ') + str(a1) + str(' wynosi: '), end='')
        print(str(objczwfor(a1)), str('jednostek szesciennych'))

    if wartosc2 == 2:
        print('Wybrano mase czworoscianu foremnego')
        d2 = float(input('Podaj gestosc czworoscianu foremnego: '))
        v2 = float(input('Podaj objetosc czworoscianu foremnego: '))
        if d2 <= 0:
            print('Gestosc czworoscianu foremnego musi byc dodatnia')
            quit()
        if v2 <= 0:
            print('Objetosc czworocianu foremengo musi byc dodatnia')
            quit()


        def masaczwfor(d2, v2):
            wyniki = d2 * v2
            return wyniki


        print(str('Masa czworoscianu foremnego o gestosci ') + str(d2) + str(' i objetosci ') + str(v2) + str(
            ' wynosi: '),
              end='')
        print(str(masaczwfor(d2, v2)), str('jednostek masowych'))

    if wartosc2 == 3:
        print('Wybrano pole powierzchni czworoscianu foremnego')
        a1 = float(input('Podaj wartosc boku czworoscianu foremnego: '))
        if a1 <= 0:
            print('Dlugosc musis byc dodatnia')
            quit()


        def poleczwfor(a1):
            wynik = a1 ** 2 * math.sqrt(3)
            return wynik


        print(str('Pole czworscianu foremnego o boku ') + str(a1) + str(' wynosi: '), end='')
        print(str(poleczwfor(a1)), str('jednostek kwadratowych'))

if figura == 3:
    print('Wybrana figura to elipsoda.')
    print('Dostepne wlasciwosci do obliczenia to 1. Objetosc, 2. Masa, 3. Pole powierzchni')
    wartosc3 = float(input('Wybierz numer wartosci ktora chcesz policzyc: '))
    if wartosc3 == 1:
        print('Wybrano objetosc elipsody')
        a3 = int(input('Podaj wartosc poziomej polosi: '))
        b3 = int(input('Podaj wartosc pionowej polosi: '))
        if a3 <= 0:
            print('Wartosc polosi musi byc dodatnia')
            quit()
        if b3 <= 0:
            print('Wartosc polosi musi byc dodatnia')
            quit()


        def objelip(a3, b3):
            wynik = (4 / 3) * math.pi * a3 * (b3 ** 2)
            return wynik


        print(str('Objetosc elipsody o poziomej polosi'), str(a3), str('i pionowej polosi'), str(b3), str('wynosi: '),
              end='')
        print(str(objelip(a3, b3)), str(' jednostek szesciennych'))

    if wartosc3 == 2:
        print('Wybrano mase elipsody')
        d3 = float(input('Podaj gestosc elipsody: '))
        v3 = float(input('Podaj objetosc elipsody'))
        if d3 <= 0:
            print('Gestosc elipsody musi byc dodatnia')
            quit()
        if v3 <= 0:
            print('Objetosc elipsody musi byc dodatnia')
            quit()


        def masaelip(d3, v3):
            wynik = d3 * v3
            return wynik


        print(str('Masa elipsody o gestosci'), str(d3), str('i objetosci'), str(v3), str('wynosi: '), end='')
        print(str(masaelip(d3, v3)), str('jednostek masowych'))

    if wartosc3 == 3:
        print('Wybrano pole powierzchni elipsody')
        a3 = float(input('Podaj wartosc poziomej polosi: '))
        b3 = float(input('Podaj wartosc pionowej polosi: '))
        if a3 <= 0:
            print('Wartosc polosi musi byc dodatnia')
            quit()
        if b3 <= 0:
            print('Wartosc polosi musi byc dodatnia')
            quit()
        if a3 <= b3:
            print('Blad, musi byc spelnione zalozenie a > b')
            quit()
        epsilon = math.sqrt(1 - (b3 ** 2 / a3 ** 2))


        def poleelip(a3, b3):
            wynik = 2 * b3 * math.pi * (b3 + (a3 / epsilon) * math.asin(epsilon))
            return wynik


        print(str('Pole elipsody o poziomej polosi'), str(a3), str('i pionowej polosi'), str(b3), str('wynosi: '),
              end='')
        print(str(poleelip(a3, b3)), str('jednostek kwadratowych'))

if figura == 4:
    print('Wybrana figura to ostroslup prosty o podstawie prostokatnej')
    print('Dostepne wlasciwosci do obliczenia to 1. Objetosc, 2. Masa, 3. Pole powierzchni')
    wartosc4 = int(input('Wybierz numer wartosci ktora chcesz policzyc: '))
    if wartosc4 == 1:
        print('Wybrano objetosc ostroslupa prostego o podstawie prostokatnej')
        a4 = float(input('Podaj wartosc krawedzi podstawy ostroslupa: '))
        h4 = float(input('Podaj wartosc wysokosci ostroslupa: '))
        if a4 <= 0:
            print('Wartosc krawedzi podstawy ostroslupa musi byc dodatnia')
            quit()
        if h4 <= 0:
            print('Wartosc wysokosci ostroslupa musi byc dodatnia')
            quit()


        def objostr(a4, h4):
            wynik = 1 / 3 * a4 ** 2 * h4
            return wynik


        print(str('Objetosc ostroslupa prostego o dlugosci krawedzi podstawy'), str(a4), str('i wysokosci'), str(h4),
              str('wynosi: '), end='')
        print(str(objostr(a4, h4)), str('jednostek szesciennych'))

    if wartosc4 == 2:
        print('Wybrano mase ostroslupa prostego o podstawie prostokatnej')
        d4 = float(input('Podaj gestosc ostroslupa: '))
        v4 = float(input('Podaj objetosc ostroslupa: '))
        if d4 <= 0:
            print('Gestosc ostroslupa musi byc dodatnia')
            quit()
        if v4 <= 0:
            print('Objetosc ostroslupa musi byc dodatnia')
            quit()


        def masaostr(d4, v4):
            wynik = d4 * v4
            return wynik


        print(str('Masa ostroslupa prostego o gestosci'), str(d4), str('i objetosci'), str(v4), str('wynosi: '), end='')
        print(str(masaostr(d4, v4)), str('jednostek masowych'))

    if wartosc4 == 3:
        print('Wybrano pole powierzchni ostroslupa prostego o podstawie prostokatnej')
        a4 = float(input('Podaj wartosc krawedzi podstawy ostroslupa: '))
        h14 = float(input('Podaj wartosc wysokosci sciany bocznej ostroslupa: '))
        if a4 <= 0:
            print('Wartosc krawedzi podstawy ostroslupa musi byc dodatnia')
            quit()
        if h14 <= 0:
            print('Wartosc wysokosci sciany bocznej ostroslupa musi byc dodatnia')
            quit()


        def poleostr(a4, h14):
            wynik = a4 ** 2 + 2 * a4 * h14
            return wynik


        print(str('Pole ostroslupa o krawedzi podstawy'), str(a4), str('i wysokosci sciany bocznej'), str(h14),
              str('wynosi: '), end='')
        print(str(poleostr(a4, h14)), str('jednostek kwadratowych'))

if figura == 5:
    print('Wybrana figura to stozek')
    print('Dostepne wlasciwosci do obliczenia to 1. Objetosc, 2. Masa, 3. Pole powierzchni')
    wartosc5 = int(input('Wybierz numer wartosci ktora chcesz policzyc: '))

    if wartosc5 == 1:
        print('Wybrano objetosc stozka')
        r5 = float(input('Podaj wartosc promienia podstawy stozka: '))
        h5 = float(input('Podaj wartosc wysokosci stozka: '))
        if r5 <= 0:
            print('Wartosc promienia podstawy stozka musi byc dodatnia')
            quit()
        if h5 <= 0:
            print('Wartosc wysokosci stozka musi byc dodatnia')
            quit()



        def objstoz(r5, h5):
            wynik = (math.pi * r5 ** 2 * h5) / 3
            return wynik


        print(str('Objetosc stozka o promieniu'), str(r5), str('i wysokosci'), str(h5), str('wynosi: '), end='')
        print(str(objstoz(r5, h5)), str('jednostek szesciennych'))

    if wartosc5 == 2:
        print('Wybrano mase stozka')
        d5 = float(input('Podaj gestosc stozka: '))
        v5 = float(input('Podaj objetosc stozka: '))
        if d5 <= 0:
            print('Gestosc stozka musi byc dodatnia')
            quit()
        if v5 <= 0:
            print('Objetosc stozka musi byc dodatnia')
            quit()


        def masastoz(d5, v5):
            wynik = d5 * v5
            return wynik


        print(str('Masa stozka o gestosci'), str(d5), str('i objetosci'), str(v5), str('wynosi: '), end='')
        print(str(masastoz(d5, v5)), str('jednostek masowych'))

    if wartosc5 == 3:
        print('Wybrano pole powierzchni stozka')
        r5 = float(input('Podaj wartosc promienia podstawy stozka: '))
        l5 = float(input('Podaj wartosc tworzacej stozka: '))
        if r5 <= 0:
            print('Wartosc promienia podstawy stozka musi byc dodatnia')
            quit()
        if l5 <= 0:
            print('Wartosc tworzacej stozka musi byc dodatnia')
            quit()


        def polestoz(r5, l5):
            wynik = math.pi * r5 * (r5 + l5)
            return wynik


        print(str('Pole powierzchni stozka o promieniu podstawy'), str(r5), str('i o tworzacej stozka'), str(l5), str('wynosi: '), end='')
        print(str(polestoz(r5, l5)), str('jednostek kwadratowych'))

if figura == 6:
    print('Wybrales walec')
    print('Dostepne wlasciwosci do obliczenia to 1. Objetosc, 2. Masa, 3. Pole powierzchni')
    wartosc6 = int(input('Wybierz numer wartosci ktora chcesz policzyc: '))
    if wartosc6 == 1:
        print('Wybrales objetosc walca')
        r6 = float(input('Podaj wartosc promienia podstawy walca: '))
        h6 = float(input('Podaj wartosc wysokosci walca: '))
        if r6 <= 0:
            print('Wartosc promienia podstawy walca musi byc dodatnia')
            quit()
        if h6 <= 0:
            print('Wartosc wysokosci walca musi byc dodatnia')
            quit()


        def objwal(r6, h6):
            wynik = math.pi * r6 ** 2 * h6
            return wynik


        print(str('Objetosc walca o promienu podstawy'), str(r6), str('i wysokosci'), str(h6), str('wynosi: '), end='')
        print(str(objwal(r6, h6)), str('jednostek szesciennych'))

    if wartosc6 == 2:
        print('Wybrano mase walca')
        d6 = float(input('Podaj gestosc walca: '))
        v6 = float(input('Podaj objetosc walca: '))
        if d6 <= 0:
            print('Gestosc walca musi byc dodatnia')
            quit()
        if v6 <= 0:
            print('Objetosc walca musi byc dodatnia')
            quit()


        def masawal(d6, v6):
            wynik = d6 * v6
            return wynik


        print(str('Masa walca o gestosci'), str(d6), str('i objetosci'), str(v6), str('wynosi: '), end='')
        print(str(masawal(d6, v6)), str('jednostek masowych'))

    if wartosc6 == 3:
        print('Wybrano pole powierzchni walca')
        r6 = float(input('Podaj wartosc promienia podstawy walca: '))
        h6 = float(input('Podaj wartosc wysokosci walca: '))
        if r6 <= 0:
            print('Wartosc promienia podstawy walca musi byc dodatnia')
            quit()
        if h6 <= 0:
            print('Wartosc wysokosci walca musi byc dodatnia')
            quit()


        def polewal(r6, h6):
            wynik = 2 * (math.pi * r6 ** 2) + 2 * (math.pi * r6 * h6)
            return wynik


        print(str('Pole powierzchni walca o promieniu podstawy'), str(r6), str('i wysokosci'), str(h6), str('wynosi: '), end='')
        print(str(polewal(r6, h6)), str('jednostek kwadratowych'))
