# first, second, third = map(int, input('Введите три целых числа: ').split())
print('Введите три целых числа:')
first = int(input())
second = int(input())
third = int(input())
if first == second == third:
    print(3)
elif first == second != third or second == third != first or first == third != second:
    print(2)
else: print(0)