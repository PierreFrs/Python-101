import json, os

def main():
    file_path = "exercices/files/exo_28/data/music.json"

    if os.path.exists(path):
        pass
    else:
        with open(path, "w", encoding="UTF-8") as file:
            new_dict = []
            json.dump(new_dict, file, indent=4)

    print("=== MENU PRINCIPAL ===")
    print("1. Ajouter une chanson")
    print("2. Voir les chansons")
    print("3. Editer une chanson")
    print("4. Supprimer une chanson")
    print("0. Quitter le programme")

    users_choice = int(input("Faites votre choix : "))

    print()

    match users_choice:
        case 0:
            exit()
        case 1:
            add_song(file_path)
            print()
            exit_to_main()
        case 2:
            read_songs(file_path)
            print()
            exit_to_main()
        case 3:
            edit_song(file_path)
            print()
            exit_to_main()
        case 3: 
            delete_song(file_path)
            print()
            exit_to_main()
    
def exit_to_main():
    input("Lorsque vous souhaitez revenir au menu principal, tapez 'Entrée'")
    main()

def add_song(file_path):
    print("=== AJOUTER UNE CHANSON ===")

    with open(file_path, "r", encoding="UTF-8") as file:
        song_list = json.load(file)
        last_recorded_song = song_list[-1]
        new_id = last_recorded_song["id"] + 1

    id = new_id
    title = input("Titre de la chanson")
    artist = input("Artiste de la chanson : ")
    category = input("Catégorie de la chanson : ")
    score = input("Score de la chanson (sur 5) : ")

    new_song = {
        "id" : id,
        "titre" : title,
        "artiste" : artist,
        "categorie" : category,
        "score" : score
    }

    with open(file_path, "w", encoding="UTF-8") as file:
        song_list = json.load(file)
        song_list.append(new_song)
        json.dump(song_list, file, indent=4)

    with open(file_path, "r", encoding="UTF-8") as file:
        song_list = json.load(file)
        if song_list[-1] == new_song:
            print("Votre morceau a bien été enregistré")
        else:
            print("Quelque chose empêche votre morceau d'être sauvé, veuillez contacter le service technique (pensez à faire un ticket)")

def read_songs(file_path):
     print("=== VOS CHANSONS ===")
     with open(file_path, "r", encoding="UTF-8") as file:
        song_list = json.load(file)
        for song in song_list:
            display_song(song)
            print("-" * 50)

def display_song(song):
    for key, value in song.items():
        print(f"{key} : {value}")

def update_song(file_path):
    read_songs(file_path)
    song_id = int(input("Veuillez renseigner l'id de la chanson à mettre à jour : "))
    song_to_update = {}

    with open(file_path, "r", encoding="UTF-8") as file:
        song_list = json.load(file)
        for song in song_list:
            if song["id"] == song_id:
                song_to_update = song
    
    

    with open(file_path, "w", encoding="UTF-8") as file:
        song_list = json.load(file)
        song_list.append(new_song)
        json.dump(song_list, file, indent=4)







