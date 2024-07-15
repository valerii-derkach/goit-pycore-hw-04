from colorama import Fore

def log_dir(message, tab=""):
    print(f"{Fore.BLUE} {tab} 📁 {message}/")

def log_file(message, tab=""):
    print(f"{Fore.GREEN} {tab} 📄 {message}")

def log_warning(message):
    print(f"{Fore.YELLOW} {message}")
