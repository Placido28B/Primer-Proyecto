from io import open

identification_card = ""
name = ""
lastname = ""
print("Welcome, enter your ID, the ID can only contain numbers. \n")

def registro():
    ID_LENGTH = 9
    while True :
        try:
            id = str(int(input("Write the student ID: \n")))
        except ValueError:
            print("Only numbers are allowed.")
            continue

        if len(str(id)) > ID_LENGTH:
            print("Wrong, you have extra numbers.")
            continue

        if len(str(id)) < ID_LENGTH:
            print("Wrong, you are missing numbers")
            continue
        
        print("The ID is valid. Saved.")
        break    
    identification_card = id

    print("\n" "Welcome, in this space you must register your name, only letters are allowed in the name. \n")

    while True:
        new_name = str(input("Write your name: \n"))
        
        secondary_letters = new_name[1::]
        first_letter = new_name[0]

        #VALIDAR NUMEROS
        if new_name.isdigit():
            print("Only letters are allowed")
            continue
        if new_name.isalpha():
            pass
        else:
            print("Only letters are allowed.")
            continue

        #VALIDAR MAYUS_MINIS
        if not first_letter.isupper():
            print("The first letter must be uppercase") 
            continue

        if not secondary_letters.islower():
            print("Only the first letter can be capitalized")
            continue
       
        if first_letter.isupper and secondary_letters.islower():
            print("Name Save")
            break

    name = new_name

    while True:
        new_lastname = str(input("Write your lastname: \n"))
    
        secondary_letters = new_lastname[1::]
        first_letter = new_lastname[0]

        if new_lastname.isdigit():
            print("Only letters are allowed")
            continue
        if new_lastname.isalpha():
            pass
        else:
            print("Only letters are allowed.")
            continue

        #VALIDAR MAYUS_MINIS
        if not first_letter.isupper():
            print("The first letter must be uppercase") 
            continue

        if not secondary_letters.islower():
            print("Only the first letter can be capitalized")
            continue
    
        if first_letter.isupper and secondary_letters.islower():
            print("Lastname Save")
            break  
    lastname = new_lastname

    with open("Excel_Bases.csv","a") as archivo_texto: 
        archivo_texto.write(str(identification_card)+",")
        archivo_texto.write(str(name)+",")
        archivo_texto.write(str(lastname)+",")
        archivo_texto.write("\n")
registro()