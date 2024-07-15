def calculate_statistics(salary: list[int]) -> tuple[int]:
    if not salary:
        return None
    
    total = sum(salary)
    average = int(sum(salary) / len(salary))

    return [total, average]
