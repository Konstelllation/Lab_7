#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    li = []
    s = 0
    mn = 0
    mx = 0
    pr = 1

    # Ввод элементов
    n = int(input('Введите количество переменных: '))
    for i in range(n):
        li.append(int(input()))

    # Определение суммы положит. эл. и индексы макс. и мин. эл. строки
    for i, x in enumerate(li):
        if x > 0:
            s += x
        if abs(x) < li[mn]:
            mn = i
        if abs(x) > li[mx]:
            mx = i

    # Произведение эл. между макс. и мин. эл.
    if mx < mn:
        for i in range(mx + 1, mn):
            pr *= li[i]
    else:
        for i in range(mn + 1, mx):
            pr *= li[i]

    # Вывод s, pr, и отсортированного списка
    print('Сумма положительных элементов списка = ', s)
    print('Произведение элементов списка, расположенных между максимальным'
          ' по модулю и минимальным по модулю элементами = ', pr)
    li.sort(reverse=True)
    print('Отсортированный список по убыванию: ', li)
