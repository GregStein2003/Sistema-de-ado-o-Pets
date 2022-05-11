class Pessoa:
 def __init__(self, id=None, nome=None, sexo=None):
    self._id = id
    self._nome = nome
    self._sexo = sexo
 
 def deserializar(self, linha):
    dados = linha.split(';')
    self._id = int(dados[0])
    self._nome = dados[1]
    self._sexo = dados[2]
    self._pet = list[dados[3]]

 def serializar(self):
     return f'\n{self._id};{self._nome};{self._sexo}'

 def exibe_dados(self):
    print('* Pessoa *')
    print('Id:', self._id)
    print('Nome:', self._nome)
    print('Sexo:', self._sexo)
    print('* Pet *')
    if self._pet:
        self._pet.exibe_dados()
    else:
        print('Desconhecido')
    print()

class Pet:
 def __init__(self, id=None, nome=None, sexo=None, tipo=None):
    self._id = id
    self._nome = nome
    self._sexo = sexo
    self._tipo = tipo

 def deserializar(self, linha):
    dados = linha.split(';')
    self._id = int(dados[0])
    self._nome = dados[1]
    self._sexo = dados[2]
    self._tipo = dados[3]
 
 def serializar(self):
     return f'\n{self._id};{self._nome};{self._sexo};{self._tipo}'

 def get_id(self):
    return self._id
 
 def exibe_dados(self):
    print('Id:', self._id)
    print('Nome:', self._nome)
    print('Sexo:', self._sexo)
    print('Tipo:', self._tipo)

 def localiza_pet(id):
    for pet in pets:
        if pet.get_id() == id:
            return pet
        return None

if __name__ == '__main__':
 pets = []
 pessoas = []
 continuar = 's'
 id_pet = 0
 id_pessoas = 0

 print("\n----- MENU -----")
 print("1- CADASTRAR PET", '\n2- CADASTRAR PESSOA', '\n3- ADOTAR','\n4- LISTAR TUDO', '\n5- LISTAR POR TIPO DE PET',
 '\n6- SALVAR', '\n7- CARREGAR', '\n8- SAIR')
 inpt = input('\nOPÇÃO: ')

 if inpt == '1':
        while continuar in 'Ss':
            id_pet +=1
            inpt_nome = input('Digite o nome do pet: ')
            inpt_sexo = input('Digite o sexo: (M/F): ')
            inpt_tipo = input('Digite o tipo do pet: ')
            pets.append(Pet(id_pet, inpt_nome, inpt_sexo, inpt_tipo))
            arq = open('pets.txt', 'w')
            arq.write('id;nome;sexo;tipo')
            for pet in pets:
                arq.write(pet.serializar())
            continuar = input('Continuar? S/N: ')
            arq.close()
 if inpt == '2':
     while continuar in 'Ss':
            id_pessoas +=1
            inpt_nome = input('Digite o nome da pessoa: ')
            inpt_sexo = input('Digite o sexo: (M/F): ')
            pessoas.append(Pessoa(id_pessoas, inpt_nome, inpt_sexo, inpt_tipo))
            arq = open('pessoas.txt', 'w')
            arq.write('id;nome;sexo;tipo')
            for pessoa in pessoas:
                arq.write(pessoa.serializar())
            continuar = input('Continuar? S/N: ')
            arq.close()
if inpt == '3':
    inpt_adt_pessoa = input('Digite o nome da pessoa que irá adotar: ')
    inpt_adt_pet = input('Digite o nome do pet que deseja adotar: ')
