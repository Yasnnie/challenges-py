# Desafio -> https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true
# Yasmin Carvalho Targino de Alencar - 07/10/2022

text = input()

odd_list = []
even_list = []
uppercase = []
lowercase = []

is_odd = lambda number: number % 2 != 0

for letter in text:
    try:
        number = int(letter)
        if is_odd(number):
           odd_list.append(letter)
          
        else:
           even_list.append(letter)

    except:
        if (letter.islower()):
            lowercase.append(letter)
        else:
            uppercase.append(letter)

odd_list.sort()
even_list.sort()
uppercase.sort()
lowercase.sort()

final = lowercase + uppercase + odd_list + even_list

print("".join(final))


