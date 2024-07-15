from data import load_data, normalize_data_str_to_dict

def get_cats_info(path):
    try:
        raw_data = load_data(path)
        cats_info = normalize_data_str_to_dict(raw_data)
        print(cats_info)

    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None

if __name__ == "__main__":
    filename_path = "task2/cats.txt"
    get_cats_info(filename_path)
