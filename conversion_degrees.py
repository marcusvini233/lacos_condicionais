#Fahrenheit (F)
#Celsius (C)
#Kelvin (K)

def convertF_to_C(num):
        f = 1.8*(c)+32.0
        f = round(f,1)
        print("Temperatura convertida em Fahrenheit:", f,"°F")

def convertC_to_F(num):
        c = (f-32)/1.8
        c = round(c,1)
        print("Temperatura convertida em Celsius:",c,"°C") 




print("CONVERSOR DE TEMPERATURAS")
print("*" * 20)
print("Escolha a conversão desejada:")
print("*" * 20)
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")
print("")

opcao = int(input("Opções (1-2): "))

if (opcao == 1):
    c = float(input("Temperatura em Celsius: "))
    convertF_to_C(c)
elif (opcao == 2):
    f = float(input("Temperatura em Fahrenheit: "))
    convertC_to_F(f)
else:
    print("Escolha entre as opções 1 ou 2.")
