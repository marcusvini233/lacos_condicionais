print("CONDIÇÃO PARA VOTAR 2022")
print("*" * 25)
idade = int(input("Insira a idade do eleitor: "))

if idade >= 18:
    print("Permitido e obrigatório votar em 2022.")
elif idade < 18:
    print("Não está permitido votar em 2022.")
elif idade >= 65:
    print("Não é obrigatório votar em 2022.")

