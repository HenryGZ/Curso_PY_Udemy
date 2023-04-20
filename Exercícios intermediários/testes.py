'''int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça
{
K = K + 1;
SOMA = SOMA + K;
}

imprimir(SOMA);'''


i = 13
soma = 0
k = 0
while True:
    
    k = k + 1
    soma = soma + k
    if k > i:
        break
print(soma)