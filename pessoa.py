class Pessoa:
    def __init__(self, id=None, nome=None, sexo=None):
        self._id = id
        self._nome = nome
        self._sexo = sexo
        self._pet = []

    def teste(self, item, item2=None):
        self._item = item
        self._item2 = item2

    def get_teste(self):
        return self._item 

    def deserializar(self, linha):
        dados = linha.split(';')
        self._id = int(dados[0])
        self._nome = dados[1]
        self._sexo = dados[2]
        self._pet = localiza_pet(int(dados[3]))

    def set_pet(self, petId):
        self._pet.append(petId)

    def get_petId(self):
        return self._pet
    
    def get_nome(self):
        return self._nome

    def serializar(self):
        return f'\n{self._id};{self._nome};{self._sexo};{self._pet}'

    def exibe_dados(self):
        print(self._pet)
        print('* Pessoa *')
        print('Id:', self._id)
        print('Nome:', self._nome)
        print('Sexo:', self._sexo)
        print('* Pet *')
        # for petId in self._pet:
        #     self._pet = localiza_pet()
        #     print(petId)
        #     if petId:
        #         petId.exibe_dados()
        #     else:
        #         print('Desconhecido')
        #     print()