from Calculo import calculo

ca = calculo

numero1 = str(input("\nDigite o primeiro numero que você deseja calcular: "))
if numero1.isnumeric():
    print("Numero ok")
else:
    print("\n\033[0;31mValor invalido!\033[m")
    exit()

cal = input("Qual calculo gostaria de realizar?"
            "\n(+) - Adção"
            "\n(-) - Subtração"
            "\n(*) - Multiplicação"
            "\n(/) - Divisão"
            "\n\nOpção: "
)

if cal == "+" or cal == "-" or cal == "*" or cal =="/":
    print("ok")
else:
    print("\n\033[0;31mValor invalido!\033[m")
    exit()

numero2 = str(input("\nDigite o segundo numero que você deseja calcular: "))

if numero1.isnumeric():
    print("Numero ok")
else:
    print("\n\033[0;31mValor invalido!\033[m")
    exit()



if cal == "+":
    resul = ca.adcao(int(numero1), int(numero2))
elif cal == "-":
    resul = ca.subtracao(int(numero1), int(numero2))
elif cal == "*":
    resul = ca.multiplicacao(int(numero1), int(numero2))
elif cal == "/":
    resul = ca.divisao(int(numero1), int(numero2))