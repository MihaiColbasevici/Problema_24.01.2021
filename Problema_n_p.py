# Pentru a introduce elementele din terminal puteti sterge '#' din liniile 2, 3
#with open("input.txt", 'w') as f:
#   f.write(input("Dati lista de nume (separate prin ', '): "))

with open("input.txt", 'r') as k:
    var = k.read()
lista = var.split(', ')
lista = sorted(lista)
with open('output.txt', 'w') as j:
    for i in lista:
        j.write(i + '\n')