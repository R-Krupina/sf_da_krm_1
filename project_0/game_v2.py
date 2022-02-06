"""Игра угадай число
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def random_predict(number: int=1) -> int:
    
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предлагаем число
        if number == predict_number:
            break # выход из цикла если угадали
    return count

def score_game(random_predict) -> int:
    '''
    Запускаем игру 1000 раз, чтобы собрать статистику по попыткам отгадывания
    '''
    count_ls = []
    np.random.seed(1) # фиксируем RANDOM SEED чтобы наш эксперемент был воспроизводим
    random_array = np.random.randint(1, 101, size=(1000)) # загадываем числа в массив
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    
# запускаем
score_game(random_predict)