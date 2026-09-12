credit = input("Number: ")

while not credit.isdigit:
    credit = input("Number: ")

sum = 0
for i in range(len(credit)-2,-1,-2):
    mult = int(credit[i])*2

    if mult > 9:
        mult = str(mult)
        sum = sum + int(mult[0]) + int(mult[1])
    elif mult < 10:
        sum = sum + mult

for i in range(len(credit)-1,-1,-2):
    sum = sum + int(credit[i])

if sum%10 == 0:
    if len(credit) == 15 and (int(credit[0]) == 3 and int(credit[1]) == 4) or (int(credit[0]) == 3 and int(credit[1]) == 7):
        print("AMEX")
    elif len(credit) == 16 and int(credit[0]) == 5 and (int(credit[1]) == 1 or int(credit[1]) == 2 or int(credit[1]) == 3 or int(credit[1]) == 4 or int(credit[1]) == 5):
        print("MASTERCARD")
    elif len(credit) == 13 or len(credit) == 16 and int(credit[0]) == 4:
        print("VISA")
else:
    print("INVALID")
