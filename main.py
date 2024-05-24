def calcula_imposto(salario):
    if salario <= 1903.98:
        imposto = 0
    elif salario > 1903.98 and salario <= 2826.65:
        imposto = salario * 7.5 / 100
    elif salario > 2826.65 and salario <= 3751.05:
        imposto = salario * 15 / 100
    elif salario > 3751.05 and salario <= 4664.68:
        imposto = salario * 22.5 / 100
    elif salario > 4664.68:
        imposto = salario * 27.5 /100
    return imposto

salario = float(input("Digite o salário do colaborador: "))
imposto = calcula_imposto(salario)
print(f"O seu imposto a pagar é de: R${imposto:.2f}")
salario_liquido = salario - imposto
print(f"Total a receber: R${salario_liquido: .2f}")
