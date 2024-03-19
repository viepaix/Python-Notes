#!/usr/bin/env python3

import os

from colored import Fore, Back, Style
from gestor_notes import GestorNotes

st = Style.reset

def main():

    gestor = GestorNotes()

    while True:

        print(f"\n{Fore.light_yellow} Menu\n")
        print(f"1. add note")
        print(f"2. read all notes note")
        print(f"3. search one note")
        print(f"4. delete a note")
        print(f"5. exit{Style.reset}")

        option = input(f"\n{Fore.green} Select your option:{Style.reset} ")
        
        if option == "1":
            content = input(f"\n{Back.light_blue}{Fore.black}Content of the note:{Style.reset} ")
            gestor.add_note(content)
        elif option == "2":
            notes = gestor.show_note()
            
            print(f"{Fore.light_yellow}\n Showing all the notes 󱞣 \n{Style.reset}")
            for i, note in enumerate(notes):
                print(f"{i} | {note}")

        elif option == "3":
            search_text = input(f"\n{Fore.green}Search a note with a specific text:{Style.reset} ")
            notes = gestor.search_note(search_text)

            print(f"\n{Fore.light_yellow}These are the notes with the word {search_text}:{st} \n")
            for i, note in enumerate(notes):
                print(f"{i} | {note}")

        elif option == "4":
            index = int(input("\nNote you want to remove: "))
            gestor.del_note(index)
            

        elif option == "5":
            break
        else:
            print(f"\n{Back.red}{Fore.black}{Style.bold}The input of your option is incorrect{st}\n")

        input(f"\n {Fore.red}{Style.bold}Press <Enter> to continue...{Style.reset}")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
