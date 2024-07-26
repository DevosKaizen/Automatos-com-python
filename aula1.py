
estados = []
alfabeto = []
funcao_transicao = {}
estado_inicial = None
estados_finais = []


while True:
    estado = input('Informe o estado: ')

    if estado =='':
        break
    estados.append(estado)




while True:
    caractere = input('Informe o caractere: ')

    if caractere =='':
        break
    alfabeto.append(caractere)


for estado in estados:
    transicao_local = {}
    for caractere in alfabeto:
        temp = input(f'({estado}, {caractere}): ')
        transicao_local[caractere] = temp

    funcao_transicao[estado] = transicao_local
while True:
    estado_final = input('Informe o estado final: ')
    if estado_final == '':
        break
    estados_finais.append(estado_final)
while True:
    estado_inicial = input('Informe o estado inicial: ')
    if estado_inicial == '':
        break

    for caractere in palavra:
        proximo_estado = funcao_transicao[estado_atual][caractere]
        estado_atual = proximo_estado

    if estado_atual in estados_finais:
        print('Palavra aceita')
    else:
        print('Palavra rejeitada')

while True:
    estado_atual = estado_inicial
    palavra = input('Informe a palavra: ')

print(f'Estados informados: {estados}')
print(f'Alfabeto: {alfabeto}')
print(f'Função de transição: {funcao_transicao}')
print(f'Estados_iniciais: {estado_inicial}')
print(f'Estados_finais: {estados_finais}')