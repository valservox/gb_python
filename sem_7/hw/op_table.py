# print(list(zip([i // 3 + 1 for i in range(9)],[i for i in range(3)] * 3)))

def print_operation_table(operation, num_rows, num_columns):

    if num_rows < 2:
        return print('ОШИБКА! Размерности таблицы должны быть больше 2!')

    print(*[i for i in range(1,num_columns + 1)])

    for j in range(2,num_rows + 1):
        print(*[operation(j, i) if i > 1 else j for i in range(1, num_columns + 1)])

print_operation_table(lambda x, y: x + y, 4, 4)