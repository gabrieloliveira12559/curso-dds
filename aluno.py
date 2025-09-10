class aluno:
    nome =""
    idade = 0
    def mostrarsituacao(self):
        if self.idade >=18:
            print(self.nome, "maior de idade")
        else:
            print(self.nome, "menor de idade")

a1 = aluno()
a1.nome = "rodrigo raimundo"
a1.idade = 16

a1.mostrarsituacao()

a2 = aluno()
a2.nome = "yamil"
a2.idade = 160

a2.mostrarsituacao()

a3 = aluno()
a3.nome = "jonathan"
a3.idade = 16

a3.mostrarsituacao()

a4 = aluno()
a4.nome = "morais"
a4.idade = 16

a4.mostrarsituacao()

a5 = aluno()
a5.nome = "diego"
a5.idade = 18

a5.mostrarsituacao()

a6 = aluno()
a6.nome = "andrew"
a6.idade = 16

a6.mostrarsituacao()

a7 = aluno()
a7.nome = "aliaga"
a7.idade = 17

a7.mostrarsituacao()

a8 = aluno()
a8.nome = "vanessa"
a8.idade = 17

a8.mostrarsituacao()

a9 = aluno()
a9.nome = "luan"
a9.idade = 16

a9.mostrarsituacao()

a10 = aluno()
a10.nome = "leandro"
a10.idade = 17

a10.mostrarsituacao()
