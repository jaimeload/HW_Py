def print_operation_table(operation, num_rows = 6, num_columns = 6):
    for i in range(1, num_rows + 1):
        values = []
        for j in range(1, num_columns + 1):
            values.append(operation(i, j))
        print(*values)

print_operation_table(lambda x, y: x * y)
