from tkinter import END
from turtle import end_fill


print("Escolha um número para ver a tabuada de 1 a 10.")
print("-" * 20)

tabuada = int(input("Qual tabuada deseja ver? "))
incr = 0

print("*" * 20)
print("Tabuada do {}".format(tabuada))
print("*" * 20)

while incr <= 10:
    print("{} x {} = {}".format(tabuada, incr, incr * tabuada))
    incr += 1
