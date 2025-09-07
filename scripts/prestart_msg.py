from rich.console import Console
from rich.text import Text
from pyfiglet import Figlet

def prestart_message():
    console = Console()

    figlet = Figlet(font="big")
    ascii_art = figlet.renderText("> neoGen")

    gradient = ["#ff6b6b", "#ff922b", "#ffd93d", "#6bcB77", "#4d96ff"]

    output = Text()
    lines = ascii_art.splitlines()
    for line in lines:
        for i, ch in enumerate(line):
            if ch.strip():
                color = gradient[i % len(gradient)]
                output.append(ch, style=f"bold {color}")
            else:
                output.append(" ")
        output.append("\n")

    console.print(output)

    print("Tips for getting started")
    print("1. Clearly state what you want to build in simple words.")
    print("2. List the key features and requirements for the best results.")
    print("3. Make sure to add GEMINI_API_KEY in your .env file")
    print("\n")
    