from sys import argv
from PIL import Image
from pathlib import Path
from datetime import date
from time import strftime, localtime
from colorama import Fore, Style

status_color = {
    '+': Fore.GREEN,
    '-': Fore.RED,
    '*': Fore.YELLOW,
    ':': Fore.CYAN,
    ' ': Fore.WHITE
}

def display(status, data):
    print(f"{status_color[status]}[{status}] {Fore.BLUE}[{date.today()} {strftime('%H:%M:%S', localtime())}] {status_color[status]}{Style.BRIGHT}{data}{Fore.RESET}{Style.RESET_ALL}")

if __name__ == "__main__":
    display(':', "Creating 'JPG' Directory")
    dir = Path.cwd() / "JPG"
    dir.mkdir(exist_ok=True)
    for arg in argv[1:]:
        display('+', f"Converting {arg}")
        image = Image.open(arg)
        image.save(f"JPG\{arg[:len(arg)-3]}jpg")