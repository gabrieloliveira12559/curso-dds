cinema = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

linha = int(input("digite a linha do assento (0 a 2): "))
coluna = int(input("digite a coluna do assento (0 a 2): "))
nome = input("digite seu nome: ")

cinema[linha][coluna] = nome
print("nova disposição na sala: ", cinema)