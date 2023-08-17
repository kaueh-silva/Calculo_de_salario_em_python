
salario = float(input("Digite seu salario \n"))

if salario <=280:
    porcetagem = 20
    porcetagem = porcetagem/100
    aumento = porcetagem * salario
    novo_salario = salario + aumento
    print("Seu salario era de  {}".format(salario))
    print("voce teve aumento de {}".format(aumento))
    print("seu novo salario é {}".format(novo_salario))

elif salario <=700:
     porcetagem = 15
     porcetagem = porcetagem/100
     aumento = porcetagem * salario
     novo_salario = salario + aumento
     print("Seu salario era de  {}".format(salario))
     print("voce teve aumento de {}".format(aumento))
     print("seu novo salario é {}".format(novo_salario))

elif salario <= 1500:
    porcetagem = 10
    porcetagem = porcetagem/100
    aumento = porcetagem * salario
    novo_salario = salario + aumento
    print("Seu salario era de  {}".format(salario))
    print("voce teve aumento de {}".format(aumento))
    print("seu novo salario é {}".format(novo_salario))
else:
    porcetagem = 5
    porcetagem = porcetagem/100
    aumento = porcetagem * salario
    novo_salario = salario + aumento
    print("Seu salario era de  {}".format(salario))
    print("voce teve aumento de {}".format(aumento))
    print("seu novo salario é {}".format(novo_salario))

