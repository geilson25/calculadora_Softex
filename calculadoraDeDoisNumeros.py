def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida.")
            return 0
    else:
        print("Operação inválida.")
        return 0

# Exemplo de uso da função:
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite o número da operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))

resultado = calculadora(numero1, numero2, operacao)
print("Resultado: ", resultado)

# Nesta função calculadora, os três parâmetros são num1, num2 e operacao.
# Com base no valor do parâmetro operacao...
# ...a função realiza a operação apropriada (soma, subtração, multiplicação ou divisão) entre num1 e num2 e retorna o resultado.

# Caso o valor de operacao não seja um número válido (1, 2, 3 ou 4), a função exibirá a mensagem "Operação inválida." e retornará 0.
# Se a operação for divisão (valor 4) e num2 for igual a zero, a função exibirá a mensagem "Erro: Divisão por zero não é permitida." e retornará 0.
# Caso contrário, a função retornará o resultado da operação.