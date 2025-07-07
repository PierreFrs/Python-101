import json, os

def main():
    file_path = "exercices/files/exo_29/data/music.json"
    song_list = load_list(file_path)

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
            save_file(file_path, song_list)
            exit()
        case 1:
            print("=== AJOUTER UNE CHANSON ===")
            song_list = add_song(file_path, song_list)
            print()
            exit_to_main()
        case 2:
            print("=== VOS CHANSONS ===")
            read_songs(song_list)
            print()
            exit_to_main()
        case 3:
            print("=== MODIFIER UNE CHANSON ===")
            song_list = update_song(file_path, song_list)
            print()
            exit_to_main()
        case 4:
            print("=== SUPPRIMER UNE CHANSON ===")
            song_list = delete_song(file_path, song_list)
            print()
            exit_to_main()

def load_list(file_path):
    if os.path.exists(file_path) and os.path.getsize(file_path) != 0:
        with open(file_path, "r", encoding="UTF-8") as file:
            return json.load(file)
    else:
        return []

def save_file(file_path, list):
    with open(file_path, "w", encoding="UTF-8") as file:
        json.dump(list, file, indent=4, ensure_ascii=False)

def exit_to_main():
    input("Lorsque vous souhaitez revenir au menu principal, tapez 'Entrée'")
    main()

def add_song(file_path, song_list):
    if not song_list:
        new_id = 1
    else:
        last_recorded_song = song_list[-1]
        new_id = last_recorded_song["id"] + 1
            
    new_song = song_creation(new_id)

    song_list.append(new_song)

    with open(file_path, "r", encoding="UTF-8") as file:
        song_list = json.load(file)
        if song_list[-1] == new_song:
            try:
                print("Votre morceau a bien été enregistré")
                return song_list
            except:
                print("Quelque chose empêche votre morceau d'être sauvé, veuillez contacter le service technique (pensez à faire un ticket)")
                exit_to_main()

def song_creation(id):
    id = id
    title = input("Titre de la chanson : ")
    artist = input("Artiste de la chanson : ")
    category = input("Catégorie de la chanson : ")
    score = input("Score de la chanson (sur 5) : ")

    return {
        "id" : id,
        "titre" : title,
        "artiste" : artist,
        "categorie" : category,
        "score" : score
    }

def read_songs(song_list):
    for song in song_list:
        display_song(song)
        print("-" * 50)

def display_song(song):
    for key, value in song.items():
        print(f"{key} : {value}")

def update_song(file_path, song_list):
    read_songs(file_path, song_list)
    song_id = int(input("Veuillez renseigner l'id de la chanson à mettre à jour : "))
    song_to_update = {}
    song_index = 0

    for song in song_list:
        if song["id"] == song_id:
            song_to_update = song
            song_index = song_list.index(song)

    print("Le morceau que vous avez choisi : ")
    display_song(song_to_update)

    updated_song = update_song_fields(song_to_update) 
    
    song_list.pop(song_index)
    song_list.insert(song_index, updated_song)
    
    print("Votre morceau a bien été mis à jour.")
    return song_list

def update_song_fields(song):
    new_title = input("Veuillez renseigner un nouveau titre (Entrée pour passer) : ")
    new_artist = input("Veuillez renseigner un nouvel artiste (Entrée pour passer) : ")
    new_category = input("Veuillez renseigner une nouvelle catégorie (Entrée pour passer) : ")
    new_score = input("Veuillez renseigner un nouveau score (Entrée pour passer) : ")

    if new_title != "":
        song["titre"] = new_title
    if new_artist != "":
        song["artiste"] = new_artist
    if new_category != "":
        song["categrorie"] = new_category
    if new_score != "":
        song["score"] = new_score   
    
    return song

def delete_song(file_path, song_list):
    read_songs(song_list)
    song_id = int(input("Veuillez renseigner l'id de la chanson à supprimer : "))
    song_to_delete = {}
    song_index = 0

    for song in song_list:
        if song["id"] == song_id:
            song_to_delete = song
            song_index = song_list.index(song)
    
    print("Le morceau que vous avez choisi : ")
    display_song(song_to_delete)
    confirm = input("Etes vous sur de vouloir le supprimer ? (y / n) : ")

    if confirm :
        song_list.pop(song_index)
        print("Votre morceau a bien été supprimé.")
        return song_list
    else:
        exit_to_main()

main()