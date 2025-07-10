class InvalidLogin(Exception):
    pass

class InvalidPassword(Exception):
    pass

def main():
    try:
        while True:
            login = input("Veuillez entrer un login SVP (celui-ci ne doit posséder que des lettres minuscules) : ")

            if not login.isalpha() or not login.islower():
                raise InvalidLogin("Il ne dois y avoir que des minuscules dans le login !")
            break
    except InvalidLogin as e:
        print(e)
    except Exception as e:
        print(e)
    
    try:
        while True:
            password = input("Veuillez entrer un mot de passe SVP (celui-ci ne doit posséder que des chiffres) : ")

            if not password.isdigit():
                raise InvalidPassword("Le mot de passe ne dois posséder que des nombres !")
            break
    except InvalidPassword as e:
        print(e)
    except Exception as e:
        print(e)

main()