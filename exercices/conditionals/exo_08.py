temp = ""

while(temp == ""):
    temp = input("Veuillez entrer la température observée : ").strip()
    temp = float(temp)

if (temp < 0):
    print("Solide")
elif (temp <= 100):
    print("Liquide")
else:
    print("Gazeux")
