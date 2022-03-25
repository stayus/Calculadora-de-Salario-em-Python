from time import sleep
inss = 0


def resumo(resultado, inss, descontos=0):
    """
    :param resultado: Valor do Salário Brunto
    :param inss: Valor atualizado na tabela de 2022. Cálculo feito só com o sálario bruto.
    :param irrf: Valor atualizado na tabela de 2022. Cálculo feito com o sálario bruto - inss 
    :param descontos: Pega o valores (inss + irrf) + entrada de valor de desconto(caso coloque algum valor extra negativo
    :return: informando valores de Horas trabalhadas, valor na semana, e diarias.
    """
    liquido = horas = 0
    titulo = 'RESUMO DO VALOR'
    print('-' * (len(titulo) + 27))
    print(f'{titulo.center(40)}')
    print('-' * (len(titulo) + 27))
    if resultado <= 1903.98:
        irrf = 0
        desconto = inss + descontos
        liquido = salario - desconto
        print(
            f'Desconto de INSS:\t7.5% \tR${inss:>4.2f}\nDesconto de IRRF:\t\tR$INSENTO\nDesconto Geral: \t\tR${desconto:>3.2f}\n\nValor Liquido: \t\t\tR${liquido:>3.2f}')
    elif resultado <= 2826.65:
        irrf = resultado * (7.5 / 100) - 142.80
        desconto = inss + irrf + descontos
        liquido = salario - desconto
        print(
            f'Desconto de INSS: \t9% \tR${inss:>4.2f}\nDesconto de IRRF:\t7.5% \tR${irrf:>3.2f}\nDesconto Geral: \t\tR${desconto:>3.2f}\n\nValor Liquido: \t\t\tR${liquido:>3.2f}')
    elif resultado <= 3641.03:
        irrf = resultado * (9 / 100) - 91
        desconto = inss + irrf + descontos
        liquido = salario - desconto
        print(
            f'Desconto de INSS: \t12% \tR${inss:>4.2f}\nDesconto de IRRF:\t9% \tR${irrf:>3.2f}\nDesconto Geral: \t\tR${desconto:>3.2f}\n\nValor Liquido: \t\t\tR${liquido:>3.2f}')
    elif resultado <= 7087.22 or resultado > 7087.22:
        irrf = resultado * (14 / 100) - 163.82
        desconto = inss + irrf + descontos
        liquido = salario - desconto
        print(
            f'Desconto de INSS: \t14% \tR${inss:>4.2f}\nDesconto de IRRF:\t14% \tR${irrf:>3.2f}\nDesconto Geral: \t\tR${desconto:>3.2f}\n\nValor Liquido: \t\t\tR${liquido:>3.2f}')

    # Resultados semanais, dias, horas...
    horas = (liquido / 220)
    diaria = horas * 8
    semanal = horas * 44

    print('-' * 11, 'Resumo do Salário', '-' * 11)
    return f'Semanal: \t\t\tR${semanal:>3.2f}\nDiaria: \t\t\tR${diaria:>3.2f}\nHoras: \t\t\t\tR${horas:>3.2f}'


salario = float(input('Salário Bruto: '))
if salario <= 1212:
    inss = salario * (7.5/100)
elif salario <= 2427.35:
    inss = salario * (9/100) - 18.18
elif salario <= 3641.03:
    inss = salario * (12/100) - 91
elif salario <= 7087.22:
    inss = salario * (14/100) - 163.82
resultado = salario - inss
print('Processando...')
sleep(2.5)
print(resumo(resultado, inss))
print('-' * 41)
