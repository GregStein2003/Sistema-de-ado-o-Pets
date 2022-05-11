
from pet import Pet
from pessoa import Pessoa

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
