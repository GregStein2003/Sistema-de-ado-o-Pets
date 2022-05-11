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