rangeNumber = 100
aux = 0
while(rangeNumber != 0):
    print(rangeNumber, end=",")
    rangeNumber -= 1

    if aux == 10:
        print()
        aux = 0
    aux += 1
print()
