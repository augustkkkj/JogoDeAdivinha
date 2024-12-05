import random

numeroSecreto = random.randint(1, 20)
tentativas = 0

while True:
    palpite = int(input('tente adivinhar o numero de 1 a 20: '))
    tentativas += 1
    
    if palpite < numeroSecreto:
        print('o numero é maior. tente novamente!')
    
    elif palpite > numeroSecreto:
        print('o numero que vc digitou é maior que o numero secreto. tente novamente!')
    
    else:
        print(f'parabens, vc acertou!\no numero secreto era: {numeroSecreto}\n vc tentou {tentativas} vezes!')

        break