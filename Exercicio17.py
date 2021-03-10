#crie uma variavel que receb um saldo de 359.56, inserir uma nota quantia por meio de input. Remover o valor de 125.98. Imprimir o valor final usando string dinamica.

saldoatual = 359.56
consumodomes = float(input("Consumo do mes "))
credito = 125.98

print(saldoatual + consumodomes - credito)
