"""faça um programa em Python que simula a distribuição de cédulas para um valor informado a ser sacado. use um loop while para iterar sobre as diferentes denominações de cédulas (R$100, R$50, R$20, R$10, R$5, R$1) e determina a quantidade de cada cédula necessária para atingir o valor desejado."""

valor = int(input("Digite o valor a Sacar:"))
cédulas = 0
atual = 100
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cédulas += 1
    else:
        print(f"{cédulas} cédula(s) de R${atual}")
        if apagar == 0:
            break
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cédulas = 0
