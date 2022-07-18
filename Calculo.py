class calculo:

    __total: float

    def adcao(numero1, numero2):
        total = numero1 + numero2
        return print(f"Resultado: {numero1} + {numero2} = {total}")

    def subtracao(numero1, numero2):
        total = numero1 - numero2
        return print(f"Resultado: {numero1} - {numero2} = {total}")

    def multiplicacao(numero1, numero2):

        if numero1 == 0 or numero2 == 0:
            return print("Quaquer numero multiplicado por zero, sempre será zero!")
        else:
            total = numero1 * numero2
            return print(f"Resultado: {numero1} * {numero2} = {total}")

    def divisao(numero1, numero2):

        if numero1 == 0:
            return print("Sé o numerador for igual a zero, sempre será zero!")

        elif numero2 == 0:
                return print("Não é possível dividir por zero")
        else:
            total = numero1 / numero2
            return print(f"Resultado: {numero1} / {numero2} = {total}")