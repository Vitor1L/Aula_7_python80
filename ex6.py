import random
n = [3,2,1]
for c in n:
    randomico = random.randint (1,20)
    num1=int(input('Jogador 1, escolha seu número: '))
    num2=int(input('Jogador 2, escolha seu número: '))
    c=c-1
    if randomico==num1 and randomico!=num2:
            print(f'Jogador 1, você acertou! o número é: {randomico}')
    
            print(f'Jogador 2, você errou o número é: {randomico}')
            break
    elif randomico==num2 and randomico!=num1:
             print(f'Jogador 1, você errou, o número é: {randomico}')
             print(f'Jogador 2, você acertou, o número é: {randomico}')
             break
    elif randomico != num1 and randomico != num1:
         print (f'Ambos erraram, o número é: {randomico}')
         print (f'{c} chances restantes')
        
    elif randomico == num1 and randomico == num2:
         print (f'Ambos acertaram, o número é: {randomico}')
         break
    if c == 0:
        print('Vocês perderam')
     
        
        
    
             
             
         
