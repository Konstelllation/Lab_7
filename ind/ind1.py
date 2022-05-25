#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    A = []
    G = []
    F = []
    s_a = 0
    s_g = 0
    s_f = 0

    n = int(input('Введите количество учащихся: '))
    for i in range(n):
        print('\n', i + 1, '-й учащийся')
        A.append(int(input('Введите оценку за алгебру: ')))
        G.append(int(input('Введите оценку за геометрию: ')))
        F.append(int(input('Введите оценку за физику: ')))
        s_a += A[i]
        s_g += G[i]
        s_f += F[i]

    if s_a > s_g and s_a > s_f:
        print('\nЛучше всего успеваемость по алгебре')
    elif s_g > s_a and s_g > s_f:
        print('\nЛучше всего успеваемость по геометрии')
    else:
        print('\nЛучше всего успеваемость по физике')
