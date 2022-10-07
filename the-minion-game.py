# Desafio -> https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
# Yasmin Carvalho Targino de Alencar - 07/10/2022

def minion_game(string):
    vogais = ["a","e","i","o","u"]
    lowercase = string.lower()
    kevin = 0
    stuart = 0

    for i in range(len(lowercase)):

        if lowercase[i] in vogais:
            kevin += len(lowercase[i:])
        else:
            stuart += len(lowercase[i:])
    
    if kevin > stuart: 
        print("Kevin",kevin)
    elif kevin < stuart: 
        print("Stuart",stuart)
    else:
       print("Draw")
           
            


word = input()

minion_game(word)

