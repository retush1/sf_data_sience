"""Игра угадай число."""


import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0
    min1 = 1
    max1 = 101
    predict_current = np.random.randint(1, 101)
    while True:
        count += 1

        if predict_current == number: break 
        elif predict_current > number: 
            max1 = predict_current  
            predict_current -= int((max1 - min1) // 2)
        else:
            min1 = predict_current
            predict_current += int((max1 - min1) // 2)

    return count


def score_game(random_predict, size=20) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size)  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    print(f'Среднее число попыток {int(np.mean(count_ls))}') 
    print(f'Максимальное количество попыток {max(count_ls)}') 
    print(f'Минимальное количество попыток {min(count_ls)}') 
    
    
if __name__ == "__main__":
    # RUN
    score_game(random_predict)