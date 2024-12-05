# Lab 2 - Calculadora

print("""***Calculadora Python!***
    + soma
    - subtração
    * multiplicação
    / divisão""")

#Primeira versão de entradas:

# Digite a operacao (+: soma, -: subtração, *: multiplicação, /: divisão)
#operacao = input("\nQual a operacao desejada? ")
# Digite o primeiro número
#num1 = float(input("Digite o primeiro número: "))
# Digite o segundo número
#num2 = float(input("Digite o segundo número: "))


#Minha versão de entrada:

entry = input("Escreva a expressão como no exemplo '2 + 2': ")
conta = entry.split(" ")

num1 = int(conta[0])
num2 = int(conta[2])
operacao = conta[1]

# Faça as operações
def soma(x,y): 
    return x + y
    
def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    return x / y

# Mostre a operacao e o resultado

if operacao == "+":
    print(num1, "+", num2, "=", soma(num1, num2))

elif operacao == "-":
    print(num1, "-", num2, "=", subtracao(num1, num2))

elif operacao == "*":
    print(num1, "*", num2, "=", multiplicacao(num1, num2))

elif operacao == "/":
    if num2 == 0:
        print("Não é possível dividir por zero!")
    else:
        print(num1, "/", num2, "=", divisao(num1, num2))
    
else:
    print("Operacao Inválida!")
