anime = "pokemon"
lista = ["demon slayer", "one piece", "hollow knnight", "huntexhunter"]
notas = [9.5, 10.0, 10.8, 8.0]

print(lista) # mostrar todos da lista
print(lista[0]) # pegando o primeiro valor da lista
lista.append("death note") # adicionando valores na minha lista
print(lista) # mostrando a lista com o valor adicionado
#--------------------------------------------------------------------------
print("mostrando nota")
print(f'A nota do {lista[0]} : {notas[0]}')
notas.append(9.5)
print(f' a nota de {lista[4]} : {notas[4]}')
lista.append(anime)