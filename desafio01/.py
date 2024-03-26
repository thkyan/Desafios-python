def calcular_imc(peso, altura):
    return peso / (altura ** 2)

pessoas = []

while True:
    nome = input("Digite o seu nome: (ou digite 'fim' se deseja encerrar.)")
    if nome == 'fim' :
        break
    peso = int(input("Digite o seu peso:"))
    altura = int(input("Digite a sua altura:"))
    pessoas.append({'nome': nome, 'peso': peso, 'altura': altura })
   
    

for pessoa in pessoas:
    pessoa['imc'] = calcular_imc(pessoa['peso'], pessoa['altura'])

import statistics
imcs = [pessoa['imc'] for pessoa in pessoas]
media_imc = statistics.mean(imcs)
mediana_imc = statistics.median(imcs)
desvio_padrao = statistics.stdev(imcs)

print(f"Média do IMC: {media_imc}")
print(f"Mediana do IMC: {mediana_imc}")
print(f"Desvio padrão do IMC: {desvio_padrao}")