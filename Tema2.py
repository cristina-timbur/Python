luni_31 = [1, 3, 5, 7, 8, 10, 12]
luni_30 = [4, 6, 9, 11]
y = int(input('Anul este '))
x = int(input('Numărul lunii este '))

if x > 12 or x < 1 or y < 0:
    print('Nu există așa ceva')
else:
    if x in luni_31:
        print(31)
    elif x in luni_30:
        print(30)
    else : 
        if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
            print(29)
        else : 
            print(28)