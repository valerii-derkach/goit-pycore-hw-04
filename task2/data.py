def load_data(filename: str) -> list[str]:
    try:
        with open(filename, "r", encoding='utf-8') as file:
            return file.readlines()

    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
        return None

    except Exception as e:
        print(f"Сталася помилка при обробці файлу '{filename}': {e}")
        return None

def normalize_data_str_to_dict(cats_data: list[str]) -> list[dict]:
    if not cats_data:
        print("Немає даних")
        return None

    cats = []

    for item in cats_data:
        id, name, age = item.split(',')
        cat = { "id": id, "name": name, "age": int(age) }
        cats.append(cat)
    return cats
