# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(n):
    if n < 0: return False
    elif n < 2 and n >= 0:  return True
    else:
        a, b = 0, 1
        while True:
            c = a + b
            if c == n: return True
            elif c > n: return False
            a, b = b, c

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
pertence = fibonacci(numero)

if pertence: print(f"O número {numero} pertence à sequência de Fibonacci.")
else: print(f"O número {numero} não pertence à sequência de Fibonacci.")
