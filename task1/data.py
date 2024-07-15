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

def normalize_data(salary_data: list[str]) -> list[int]:
    if not salary_data:
        print("Немає зарплатних даних")
        return None

    salary_amounts = []

    for item in salary_data:
        salary_amounts.append(int(item.split(',')[1]))
    return salary_amounts
