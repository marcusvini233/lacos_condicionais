elements = int(input("Quantas frutas deseja adicionar à lista? "))
list1 = []

for i in range(elements):
    frutas = str(input("Qual fruta deseja adicionar à lista? "))
    list1.append(frutas)

print("As frutas da sua lista são: ", list1)

remove = input("Gostaria de remover algum elemento da lista? ")
element_remove = input("Qual fruta gostaria de remover?")