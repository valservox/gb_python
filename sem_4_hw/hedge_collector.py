arr = [5, 8, 6, 4, 9, 2, 7, 3]

# Введите ваше решение ниже

max_collected = sum(arr[:3])
collected = max_collected

for i in range(1,len(arr) - 2):

    collected -= arr[i - 1]
    collected += arr[i + 2]

    max_collected = collected if collected > max_collected else max_collected

edge_1 = sum(arr[:2]) + arr[-1]
edge_2 = sum(arr[-2:]) + arr[0]

max_collected = edge_1 if edge_1 > max_collected else max_collected
max_collected = edge_2 if edge_2 > max_collected else max_collected

print(max_collected)