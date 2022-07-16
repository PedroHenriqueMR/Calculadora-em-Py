print("Bem vindo a plataforma de calculo!\n");

cont = False;
nome = input("Qual se nome? ");
usuario = nome.upper();

print("\nOlá","\033[0;36m",usuario,"\033[m","Sejá bem-vindo a plataforma de calculo\n");

print("\033[0;36m",usuario,"\033[m","você gostaria de realizar algum calculo?");

while usuario:

    opcao = str(input("S para continuar\nN para finalizar\n"));

    if opcao == "s" or opcao == "S":
        print("\33[0;32mVoce escolheu continuar o Porcesso\033[m");
    elif opcao == "n" or opcao == "N":
        print("\033[0;31mVocê optou por finaliazr\033[m");
        break;
    else:
        print("\n\033[0;31mOpção invalida\033[m");
        print("Digite novamente!!");
        continue;

    while cont == False:
        soma1 = str(input("\nDigite o primeiro numero que você deseja calcular: "))
        if soma1.isnumeric():
            break
        else:
            print("\n\033[0;31mValor invalido!\033[m")
            print("Dígite apenas numeros!!\n")
            continue;

    while cont == False:
        print("Qual calculo você deseja fazer?")
        print("(+) = Adção")
        print("(-) = Subtração")
        print("(*) = Multiplicação")
        print("(/) = divisão")
        calculo = input("")

        if calculo == "+" or calculo == "-" or calculo == "*" or calculo == "/":
            break
        else:
            print("\n\033[0;31mOpção invalida\033[m");
            print("Digite novamente!!\n");
            continue;
    while cont == False:
        soma2 = str(input("\nDigite o segundo numero que você deseja calcular: "))
        if soma2.isnumeric():
            break
        else:
            print("\n\033[0;31mValor invalido!\033[m")
            print("Dígite apenas numeros!!\n")
            continue;

    if calculo == "+":
        total = int(soma1) + int(soma2)
        print(soma1,"+",soma2,"=",total)
    elif calculo == "-":
        total = int(soma1) - int(soma2)
        print(soma1, "-", soma2, "=", total)
    elif calculo == "*":
        if soma1 == "0" or soma2 == "0":
            print("\033[0;31mSé o numerador ou denominador dor multiplicado por zero(0) sempre será zero(0)!!\033[m")
        else:
            total = int(soma1) * int(soma2)
            print(soma1, "*", soma2, "=", total)
    elif calculo == "/":
        if soma1 == "0":
            print("\033[0;31mSe o numerador for zero(0) resultado sempre será zero(0)\033[m")
        elif soma2 == "0":
            print("\033[0;31mNão é possível dividir por zero\033[m")
        else:
            total = int(soma1) / int(soma2)
            print(soma1, "/", soma2, "=", total)

    print("\nVocê deseja realizar mais algum calculos?")