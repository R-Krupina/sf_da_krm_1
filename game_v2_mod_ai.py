"""Игра Угадай число"""
#   определение среднего количнства "угадываний"

import numpy as np

def game_core_v1(number):
    '''
    Просто угадываем на random никак не используя информацию о больше или меньше.
    Функция принимает загаданное число и возвращает число попыток
    '''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1, 101) # предполааемое число
        if number == predict:
            break
    return(count)

def score_game(game_core_v1):
    '''
    Запускаем игру 1000 раз чтобы узнать как быстро игра угадывает число
    '''
    count_ls = []
    np.random.seed(1) # фиксируем RANDOM SEED чтобы наш эксперемент был воспроизводим
    random_array = np.random.randint(1, 101, size=(1000)) # загадываем числа в массив
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    
# запускаем
score_game(game_core_v1)

    