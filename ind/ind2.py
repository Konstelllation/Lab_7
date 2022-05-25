#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__ == '__main__':
    li = []
    s = 0
    mn = 0
    mx = 0
    pr = 1
    n = int(input('Введите количество переменных: '))
    for i in range(n):
        li.append(int(input()))
        if i == 0:
            mn = li[i]
            mx = li[i]
        if li[i] > 0:
            s += li[i]
        if abs(li[i]) < mn:
            mn = i
        if abs(li[i]) > mx:
            mx = i
    if mx < mn:
        for i in range(mx + 1, mn):
            pr *= li[i]
    else:
        for i in range(mn + 1, mx):
            pr *= li[i]
    print('Сумма положительных элементов списка = ', s)
    print('Произведение элементов списка, расположенных между максимальным'
          ' по модулю и минимальным по модулю элементами = ', pr)
    li.sort(reverse=True)
    print('Отсортированный список по убыванию: ', li)
