# Desafio -> https://www.hackerrank.com/challenges/linkedin-practice-dictionaries-and-maps/problem?h_r=internal-search
# Yasmin Carvalho Targino de Alencar - 07/10/2022

phoneBook = {}

range_number = range(int(input()))
 
for number in range_number:
    input_new_number =   input()
    new_number = input_new_number.split(" ")
    phoneBook[new_number[0]] = new_number[1]


for options in range_number:
    name = input()

    if(name in phoneBook):
        print(name+"="+phoneBook[name])
    else:
        print("Not found")

