luni_31 = [1, 3, 5, 7, 8, 10, 12]
luni_30 = [4, 6, 9, 11]

x = int(input('Numărul lunii este '))

if x > 12 or x < 1:
    print('Nu există așa lună')
else:
    if x in luni_31:
        print(31)
    elif x in luni_30:
        print(30)
    else :
        print('28 sau 29, depinde de an')