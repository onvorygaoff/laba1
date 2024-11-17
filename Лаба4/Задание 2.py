def task() -> float:
    import json
    with open('input.json', 'r', encoding='utf-8') as file:
        main_data = json.load(file)
    total_sum = 0
    for entry in main_data:
        score = entry.get('score', 0)
        weight = entry.get('weight', 0)
        total_sum += score * weight
    return round(total_sum, 3)
print(task())

