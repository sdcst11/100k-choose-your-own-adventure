from os import system
from rich import print

system("clear||cls")

print("[red on white]Welcome to your first day of Dragon Training![/red on white]")

print("Today you will start your journey as a [bold cyan underline]dragon hunter[/bold cyan underline]. This class will help you learn all of the tricks and treats of training your own dragon pet")
print("")
print("What do you want to do next?")
print("1. Look at the [bold red]dragon pen")
print("2. Introduce yourself to some of the people in your class")

choice = input("Make a choice!:")
if input == "1":
    print("You are looking at the dragon pen.")
elif input == "2":
    print("You say, 'Hi, I'm Widget!'")
    print("What do you want to do next?")
    print("1. Look at the people in your class")