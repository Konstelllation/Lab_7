#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    A = []
    G = []
    F = []
    s_a = 0
    s_g = 0
    s_f = 0

    # Ввод оценок
    n = int(input('Введите количество учащихся: '))
    for i in range(n):
        print('\n', i + 1, '-й учащийся')
        A.append(int(input('Введите оценку за алгебру: ')))
        G.append(int(input('Введите оценку за геометрию: ')))
        F.append(int(input('Введите оценку за физику: ')))

    # Подсчет суммы баллов по каждому предмету
    for i, x in enumerate(A):
        s_a += x  # Сумма баллов по алгебре
    for i, x in enumerate(G):
        s_g += x  # Сумма баллов по геометрии
    for i, x in enumerate(F):
        s_f += x  # Сумма баллов по физике

    # Вывод лучшей успеваемости по предмету
    if s_a > s_g and s_a > s_f:
        print('\nЛучше всего успеваемость по алгебре')
    elif s_g > s_a and s_g > s_f:
        print('\nЛучше всего успеваемость по геометрии')
    else:
        print('\nЛучше всего успеваемость по физике')
