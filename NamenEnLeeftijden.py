def gegevens():
    i = 1
    while i == 1:
        naam = input('Wat is uw naam?: ')
        if naam == 'stop':
            break
        leeftijd = input('Wat is uw leeftijd?: ')
        if leeftijd == 'stop':
            break
        else: 
            print('Hallo ' + str(naam) + ' uw naam is ' + str(naam) + ' en uw leeftijd is ' + str(leeftijd))
gegevens()