# Desafio -> https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true
# Yasmin Carvalho Targino de Alencar - 07/10/2022

import numpy


def mean(array):
    my_array = numpy.array(array)
    print(numpy.mean(my_array, axis = 1))

def var(array):
    my_array = numpy.array(array)
    print(numpy.var(my_array, axis = 0))

def std(array):
    my_array = numpy.array(array)
    print(round(numpy.std(my_array, axis = None), 11))

def generate_array_number(array):
    numbers = []

    for x in array:
        numbers.append(int(x))

    return numbers

space = generate_array_number(input().split(" "))

array_to_process = []

for x in range(space[1]):
    new_values = generate_array_number(input().split(" "))
    array_to_process.append(new_values)


mean(array_to_process)
var(array_to_process)
std(array_to_process)