from data import load_data, normalize_data
from processing import calculate_statistics

def total_salary(path):
    try:
        raw_data = load_data(path)
        salaries = normalize_data(raw_data)
        total, average = calculate_statistics(salaries)
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None

if __name__ == "__main__":
    filename_path = "task1/salaries.txt"
    total_salary(filename_path)
