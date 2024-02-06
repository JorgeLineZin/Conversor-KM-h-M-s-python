Km = "kM"
Mm = "M"

numeroConv = input("Bem vindo ao conversor \n Escolha entre KM/h ou M/s: ")

if (numeroConv) == Km:
    print("Você escolheu KM/h")

numer = float(input("digite o numero que quer converter: "))

if (numer) >= 1:
    print(numer / 3.6)

elif (numeroConv) == Mm:
    print("Você escolheu M/s")

numer = float(input("digite o numero que quer converter: "))

if (numer) >= 1:
    print(numer * 3.6)
