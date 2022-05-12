import os.path

from pet import Pet
from pessoa import Pessoa

if __name__ == '__main__':
    pets = list()
    persons = list()
    
    petId = 0
    personId = 0

    while True:

        print("\n----- MENU -----")
        print("1- CADASTRAR PET", '\n2- CADASTRAR PESSOA', '\n3- ADOTAR','\n4- LISTAR TUDO // DEBUG', '\n5- LISTAR POR TIPO DE PET',
        '\n6- SALVAR', '\n7- CARREGAR', '\n8- SAIR')

        option = input('\nOPÇÃO: ')
        if option == '1':
            petId +=1
            petName = input('Digite o nome do pet: ')
            petSexo = input('Digite o sexo: (M/F): ')
            petType = input('Digite o tipo do pet: ')
            pets.append(Pet(petId, petName, petSexo, petType))

        elif option == '2':
            personId += 1
            personName = input('Digite o nome da pessoa: ')
            personSexo = input('Digite o sexo: (M/F): ')
            persons.append(Pessoa(personId, personName, personSexo))

        elif option == '3':
            if os.path.isfile('pessoas.txt') and os.path.isfile('pets.txt'): # Verifica se os arquivos de Pets e Pessoas contem informações
                refreshFilePerson = False
                refreshFilePet = False

                adoptPet = input('Digite o nome do pet que deseja adotar: ')
                adoptPerson = input('Digite o nome da pessoa que irá adotar: ')

                # Lendo informações do arquivo Pets.
                for pet in pets:
                    if pet.get_nome() == adoptPet:
                        idPetAdd = pet.get_id()
                        refreshFilePet = True

                # Lendo informações do arquivo Pessoas.
                for person in persons:
                    if person.get_nome() == adoptPerson:
                        person.set_pet(idPetAdd) # (*) <- Pet Id
                        refreshFilePerson = True
                  
                if refreshFilePet == False:
                    print("\nNão foi possível localizar o pet")

                if refreshFilePerson == False:
                    print("\nNão foi possível localizar a Pessoa")
            else:
                print("É necessário que exista alguma pessoa e/ou pet cadastrado!")

        elif option == '4':
            arqPet = open('pets.txt')
            arqPet.readline()            # Descarta o cabeçalho do arquivo
            for linha in arqPet:         # Instancia os objetos
                pets.append(Pet(linha.strip()))
                # pets.readFile(linha)
            arqPet.close()

            arqPerson = open('pessoas.txt')
            arqPerson.readline()            # Descarta o cabeçalho do arquivo
            for linha in arqPerson:         # Instancia os objetos
                persons.append(Pessoa(linha.strip()))
            arqPerson.close()

            for i in persons: 
                i.exibe_dados()
                i.teste('1')
                print(i.get_teste())




        elif option == '5':
            for i in persons:
                print(f'\nNome:{i.get_nome()}\nId Pet:{i.get_petId()}')

        elif option == '6':
            # Salva Pets
            arqPet = open('pets.txt', 'w')
            arqPet.write('Id;Nome;sexo;tipo')
            for pet in pets:
                arqPet.write(pet.serializar())
            arqPet.close()

            # Salva Pessoas
            arqPerson = open('pessoas.txt', 'w')
            arqPerson.write('Id;Nome;Sexo;Pet')
            for pessoa in persons:
                arqPerson.write(pessoa.serializar())
            arqPerson.close()
            
        else:
            print("\n Instrução Não encontrar! \n")
        
