palavra_secreta_string = 'secreta'
palavra_secreta_vetor = correta = []
tentativas = 0;

for j in range(len(palavra_secreta_string)):
    palavra_secreta_vetor.append(palavra_secreta_string[j])

palavra = len(palavra_secreta_string) * ('*')

for j in range(len(palavra_secreta_string)):
    correta.append(palavra[j])

palavra = ''

while True:
    chute = str(input('informe uma letra: '))
    if len(chute) > 1:
        print('Informe apenas uma letra!!')
    else:
        for c in range(len(palavra_secreta_string)):
            if chute == palavra_secreta_vetor[c]:
                    correta[c] = chute
        tentativas+=1
        final = palavra.join(correta)
        print(final)
        if final == palavra_secreta_string:
            break

print('parabens!! voce descobriu a palavra secreta!!')
print(f'foram realizadas {tentativas} tentativas ao total')