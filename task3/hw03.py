import sys
from pathlib import Path
from colorama import Style
from log import log_dir, log_file, log_warning

def visualize_directory_structure(directory, indent=""):
    path = Path(directory)
    if not path.exists() or not path.is_dir():
        log_warning(f"Директорія '{directory}' не існує або не є директорією.")
        return

    # Рекурсивний обхід директорій та виведення імен
    for item in path.iterdir():
        if item.is_dir():
            log_dir(item.name, indent)
            visualize_directory_structure(item, indent = indent + "    ")
        elif item.is_file():
            log_file(item.name, indent)
        else:
            log_warning(f"📄 {item.name} (інший тип об'єкту)")

    print(Style.RESET_ALL)  # Скидання кольорів

if __name__ == "__main__":
    if len(sys.argv) != 2:
        log_warning("Введіть шлях до директорії!")
        sys.exit(1)

    directory_path = sys.argv[1]
    visualize_directory_structure(directory_path)

# щоб запустити введіть python task3/hw03.py /шлях/до/вашої/директорії
