#a list of fruits that when the user stops, it stops and gives the list in alphabetical order, after that if the client wants to remove one fruit of the list, there is an option for that.

input_string = input("Escolha as frutas da sua lista separando por vírgulas: ")
grupo_lista = input_string.split(",")
print("Juntando as frutas na lista..")
for name in grupo_lista:
    print(name)


