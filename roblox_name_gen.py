import requests, random, json, string, os
from colorama import Fore, init

init()

os.system('cls')
os.system("title Gabin GitHub Generator")

def hiddenNameGen():
    length = random.randint(4, 16)
    letters = "Il"
    return ''.join(random.choice(letters) for i in range(length))

def regularNameGen():
    length = random.randint(4, 16)
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def lengthNameGen(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

choice = input('Choisissez votre option de générateur de noms !\n(1) Générateur de noms normaux\n(2) Générateur de noms cachés\n(3) Générer par longueur\nChoix : ')
how_many = int(input("Entrez le nombre de pseudo a générer: "))

tried = 0
used = 0
available = 0

if choice == '1':
    while how_many != tried:
        name = regularNameGen()
        r = requests.get("https://api.roblox.com/users/get-by-username?username=" + name)
        a = r.text
        if a.find('Id') == -1:
            tried = tried + 1
            available = available + 1
            print(Fore.GREEN + '[+]: ' + name + ' est disponible!')
        else:
            print(Fore.RED + "[-]:" + name + "n'est pas disponible!")
            tried = tried + 1
            used = used + 1

if choice == '2':
    while how_many != tried:
        name = hiddenNameGen()
        r = requests.get("https://api.roblox.com/users/get-by-username?username=" + name)
        a = r.text
        if a.find('Id') == -1:
            tried = tried + 1
            available = available + 1
            print(Fore.GREEN + '[+]: ' + name + ' est disponible!')
        else:
            print(Fore.RED + "[-]:" + name + "n'est pas disponible!")
            tried = tried + 1
            used = used + 1

if choice == '3':
    length = int(input("Combien de longeur voulez-vous que le nom d'utilisateur ai? (4-16): "))
    while how_many != tried:
        name = lengthNameGen(length)
        r = requests.get("https://api.roblox.com/users/get-by-username?username=" + name)
        a = r.text
        if a.find('Id') == -1:
            tried = tried + 1
            available = available + 1
            print(Fore.GREEN + '[+]: ' + name + ' est disponible!')
        else:
            print(Fore.RED + "[-]: " + name + "n'est pas disponible!")
            tried = tried + 1
            used = used + 1

print(f"J'ai bien généré : {available} pseudos qui sont disponibles, et {used} qui ne le sont pas.")