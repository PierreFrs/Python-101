import os

# relative path
file_path = r"09_files\fichier1.txt"

# absolute path
absolute_file_path = r"C:\Users\Administrateur\Documents\Code\Python 101\09_files\fichier1.txt"

if os.path.exists(file_path):
    file = open(file_path, "r")
    data = file.read()
    file.close()
    print(data)
else:
    file = open(file_path, "w")
    file.write("Test")
    file.close()

with open(file_path, "r") as file: # Good practice
    print(file.read())

