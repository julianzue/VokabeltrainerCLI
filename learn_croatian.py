from colorama import Fore, init
import os
import pyfiglet
import time
import random

init()

#colors
y = Fore.LIGHTYELLOW_EX
c = Fore.LIGHTCYAN_EX
g = Fore.LIGHTGREEN_EX
r = Fore.LIGHTRED_EX
re = Fore.RESET

#create file
if not os.path.isfile("vokabeln.txt"):
    os.system("touch vokabeln.txt")


class Main():
    def __init__(self):
        f = pyfiglet.Figlet()
        print(f.renderText("Vokabeltrainer"))

        print("[1] Vokabeln hinzufügen")
        print("[2] Vokabeln üben")
        print("[3] Programm beenden")

        print("")

        choose = input(y + "[+] " + re)

        if choose == "1":
            self.add()

        elif choose == "2":
            self.practise()

        elif choose == "3":
            quit()

    
    def add(self):
        deutsch = input(y + "[+] Deutsch: " + re)
        kroatisch = input(y + "[+] Kroatisch: " + re)

        with open("vokabeln.txt", "a") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M") + " | " + deutsch + " | " + kroatisch + "\n")

        print("")
        print(c + "[*] " + re + "Erfolgreich hinzugefügt!")

        next = input("[+] Weitere Vokabeln? [J|n]: ")

        if next == "j" or  next == "J" or next == "":
            print("")
            self.add()
        else:
            self.__init__()

    
    def practise(self):
        with open("vokabeln.txt", "r") as f:

            file = f.readlines()

            lines = len(file)

            rounds = int(input(y + "[+] Wie viele Runden? " + re))

            print("")

            current = 0

            score = 0

            while True:
                if rounds == current:
                    break
                else:
                    current += 1

                random_line = int(random.randint(0, (lines - 1)))

                line = file[random_line]

                split = line.strip("\n").split(" | ")

                quest = input("[" + str(current) + "] " + split[1] + " = ")

                if quest == split[2]:
                    print(g + "[*] Richige Antwort!" + re)
                    score += 1
                else:
                    print(r + "[*] Falsche Antwort!" + re + " (" + split[2] + ")")

                print("")


            percentage = int(score / rounds * 100)
            print("[*] Spiel vorbei!")
            print("[*] Sie haben " + c + str(percentage) + "% " + re + "richtig!")

            print("")

            print("[1] Nochmal spielen")
            print("[2] Zum Hauptmenü")
            print("[3] Programm beenden")

            print("")

            choose = input(y + "[+] " + re)

            if choose == "1":
                self.practise()

            elif choose == "2":
                self.__init__()

            elif choose == "3":
                quit()

            else:
                self.__init__()

Main()