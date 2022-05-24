class Pessoa:
    def __init__(self, id=None, nome=None, sexo=None):
        self._id = id
        self._nome = nome
        self._sexo = sexo
        self._pet = []

    def deserializar(self, linha):
        dados = linha.split(';')
        self._id = int(dados[0])
        self._nome = dados[1]
        self._sexo = dados[2]

    def set_pet(self, pet):
        self._pet.append(pet)

    def get_petId(self):
        return self._pet
    
    def get_nome(self):
        return self._nome

    def serializar(self):
        pets = ','.join( [ str(p.get_id()) for p in self._pet ] )
        return f'\n{self._id};{self._nome};{self._sexo};{pets}'

    def exibe_dados(self):
        print('* Pessoa *')
        print('Id:', self._id)
        print('Nome:', self._nome)
        print('Sexo:', self._sexo)
        print('* Pets *')
        if len(self._pet) == 0:
            print('Não tem pet')
        else:
            for pet in self._pet:
                pet.exibe_dados()
        print()