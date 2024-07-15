def total_salary(path):
    total_sum = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():  # перевірка, що рядок не пустий
                    surname, salary_str = line.strip().split(',')
                    salary = int(salary_str)
                    total_sum += salary
                    count += 1

        if count > 0:
            average_salary = total_sum / count
        else:
            average_salary = 0

        return total_sum, average_salary

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка при обробці файлу '{path}': {e}")
        return None

# Приклад використання функції
total, average = total_salary("task1/salaries.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
