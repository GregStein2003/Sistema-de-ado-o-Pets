from asyncio import constants
import os.path

from pet import Pet
from pessoa import Pessoa

def localiza_pet_id(id):
    for pet in pets:
        if pet.get_id() == id:
            return pet
    return None
            
def localiza_pet_nome(nome):
    for pet in pets:
        if pet.get_nome() == nome:
            return pet
    return None

def localiza_pet_tipo(tipo):
    for pet in pets:
        if pet.get_tipo() == tipo:
            return pet
    return None

def localiza_person_pet(id):
    for person in persons:
        for itemId in person.get_petId():
            if itemId == id:
                return person
    return None

def localiza_person_nome(nome):
    for person in persons:
        if person.get_nome() == nome:
            return person
    return None

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
            adoptPet = input('Digite o nome do pet que deseja adotar: ')
            adoptPerson = input('Digite o nome da pessoa que irá adotar: ')

            pet = localiza_pet_nome(adoptPet)
            person = localiza_person_nome(adoptPerson)

            if pet:
                if person:
                    person.set_pet(pet)
                else:
                    print("\nNão foi possível localizar a Pessoa")
            else:
                print("\nNão foi possível localizar o pet")

        elif option == '4':
            for person in persons:
                person.exibe_dados()

        elif option == '5':
            choosePet = input("Informe o tipo de pet que você gostaria de encontrar? ")

            typePet = localiza_pet_tipo(choosePet)

            print()

            if typePet:
                choosePerson = localiza_person_pet(typePet._id)
                choosePerson.exibe_dados()
            else:
                print("Não encotrou")

        elif option == '6':
            # Salva Pets
            arqPet = open('pets.txt', 'w')
            arqPet.write('id;nome;sexo;tipo')
            for pet in pets:
                arqPet.write(pet.serializar())
            arqPet.close()

            # Salva Pessoas
            arqPerson = open('pessoas.txt', 'w')
            arqPerson.write('id;nome;sexo;pet')
            for pessoa in persons:
                arqPerson.write(pessoa.serializar())
            arqPerson.close()

        elif option == '7':
            arqPerson = open('pessoas.txt')
            arqPerson.readline()
            for linha in arqPerson:
                Pessoa.deserializar(linha)
            arqPerson.close()

            for person in persons:
                person.exibe_dados()
            

        else:
            print("\n Instrução Não encontrar! \n")
        
