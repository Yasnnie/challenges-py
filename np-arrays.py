# Desafio -> https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true
# Yasmin Carvalho Targino de Alencar - 07/10/2022

import numpy

def arrays(arr):
    arr.reverse()
    a = numpy.array(arr,float)

    return a

arr = input().strip().split(' ')
result = arrays(arr)
print(result)