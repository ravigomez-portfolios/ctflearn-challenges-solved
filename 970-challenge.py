print('######  INICIO DO PROCESSO ###############')

firstpart = "543210"
secoundpart = "******"
thirdpart = "1234"

def isValid(cardNumber):
    i = 1
    s = 0
    for c in card:
        r = int(c) * (1 if (i % 2 == 0) else 2)
        if r > 9:
            r = r - 9
        s +=r
        i +=1

    if s % 10 == 0:
        return True
    else:
        return False

for i in range(0, 999999):
    card = firstpart + str(i).zfill(6) + thirdpart

    if int(card) % 123457 == 0 & isValid(cardNumber=card):
        print(card)

print('######  FIM DO PROCESSO ###############')