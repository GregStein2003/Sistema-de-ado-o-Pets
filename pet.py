class Pet:
    def __init__(self, id=None, nome=None, sexo=None, tipo=None):
        self._id = id
        self._nome = nome
        self._sexo = sexo
        self._tipo = tipo

    def deserializar(self, linha):
        dados = linha.split(';')
        self._id = int(dados[0])
        self._nome = str(dados[1])
        self._sexo = dados[2]
        self._tipo = dados[3]
    
    def serializar(self):
        return f'\n{self._id};{self._nome};{self._sexo};{self._tipo}'

    def get_nome(self):
        return self._nome

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