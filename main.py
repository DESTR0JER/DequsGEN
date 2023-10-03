import random
import string
import colorama
from colorama import Fore

colorama.init()

def generator(filename, look, lenght):
    def generate_random_code():
        characters = list(string.ascii_uppercase + string.digits)
        
        random_characters = random.sample(characters, lenght)
        
        code = f'{look}'.format(*random_characters)
        
        return code
    random_code_list = ""
    for i in range(100000):
        random_code = generate_random_code()

        print(f"{i}. {random_code}")
        random_code_list += f"\n{random_code}"
        
    with open(f"100k {filename}.txt", "w") as f:
        f.write(random_code_list + "\n")
    
red = Fore.RED
main = Fore.CYAN
reset = Fore.WHITE



def menu():
    print(f"""{red}
▓█████▄ ▓█████   █████   █    ██   ██████   ▄████ ▓█████  ███▄    █ 
▒██▀ ██▌▓█   ▀ ▒██▓  ██▒ ██  ▓██▒▒██    ▒  ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
░██   █▌▒███   ▒██▒  ██░▓██  ▒██░░ ▓██▄   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
░▓█▄   ▌▒▓█  ▄ ░██  █▀ ░▓▓█  ░██░  ▒   ██▒░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
░▒████▓ ░▒████▒░▒███▒█▄ ▒▒█████▓ ▒██████▒▒░▒▓███▀▒░▒████▒▒██░   ▓██░
 ▒▒▓  ▒ ░░ ▒░ ░░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░ ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
 ░ ▒  ▒  ░ ░  ░ ░ ▒░  ░ ░░▒░ ░ ░ ░ ░▒  ░ ░  ░   ░  ░ ░  ░░ ░░   ░ ▒░
 ░ ░  ░    ░      ░   ░  ░░░ ░ ░ ░  ░  ░  ░ ░   ░    ░      ░   ░ ░ 
   ░       ░  ░    ░       ░           ░        ░    ░  ░         ░ 
 ░         {reset}       
                        {main}Author:{reset} dequs
                        {main}Github:{reset} DESTR0JER/DequsGen
 {main}1.{reset} Start
 {main}2.{reset} Exit
 """)
    option = int(input(f"{main}>>{reset}"))
    
    if option == 1:
        name = input(f"Enter the file name {main}>>{reset}")
        print("What should the generated code look like? Example: {}{}{}-{}{}{}-{}{}{}")
        look = input(f"Type here {main}>>{reset}")
        znak = "{"
        lenght = look.lower().count(znak.lower())
        generator(name, look, lenght)
    

    
    
menu()
        