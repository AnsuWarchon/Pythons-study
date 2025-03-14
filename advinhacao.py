import random

num_ale = random.randint(1, 100)
tent = 0


while True:

    num_escolhido = int(input("Advinhe o um número de 1 a 100:"))

    if num_escolhido == num_ale:
        print("Acertou!")
        tent += 1
        break

    elif num_escolhido < num_ale:
        print("Tente um número maior!")
        tent += 1

    elif num_escolhido > num_ale:
        print("Tente um número menor!")
        tent += 1
    
    

print("Voce acertou o número", num_ale, "com", tent, "tentativas!")
              

