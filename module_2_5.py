def get_matrix(n, m, value):
    matrix = []
    if n > 0 and type(n) == int and m > 0 and type(m) == int:
        for i in range(1, n + 1):
            linels = []
            matrix.append(linels)
            for j in range(1, m + 1):
                linels.append(value)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
