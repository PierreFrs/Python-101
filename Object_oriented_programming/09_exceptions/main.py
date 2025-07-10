class NombreInvalidException(Exception):
    pass

while True:
    try:
        nb = int(input("Veuillez saisir un nombre entre 1 et 20 : "))

        if nb < 1 or nb > 20:
            raise NombreInvalidException("Le nombre doit être compris entre 1 et 20.")
        else:
            break
    except ValueError as v:
        print(v, "Veuillez saisir un nombre valide")
    except NombreInvalidException as e:
        print(e)
    except Exception as e:
        print(e)