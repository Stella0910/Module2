def get_numbers():
    for j in range(len(list_) - 1):
        sum_ = list_[0] + list_[j + 1]
        if n % sum_ == 0:
            result.append(list_[0])
            result.append(list_[j + 1])
    return result


stones1 = list(range(3, 21))
while True:
    n = int(input('Введите число от 3 до 20: '))
    if n in stones1:
        result = []
        list_ = list(range(1, n))
        for i in range(len(list_)):
            if len(list_) > 1:
                get_numbers()
                list_.remove(list_[0])
        print('Пароль: ', ''.join(map(str, result)))
        print('--------------------------------------------------------------------------')
    else:
        print('Вы ошиблись. На первой каменной вставки нет такого числа. Введите заново.')
        print('--------------------------------------------------------------------------')
