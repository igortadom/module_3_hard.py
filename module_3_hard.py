data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
  "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data):
    count = 0
    for item in data:
        if isinstance(item, list | tuple | set):
          count += calculate_structure_sum(item)
        if isinstance(item, dict):
          for i in item:
            count += len(i)
          count += sum(item.values())
        if isinstance(item, int):
          count += item
        if isinstance(item, str):
          count += len(item)

    return count



result = calculate_structure_sum(data_structure)
print(result)