#!/usr/bin/env python3



print("BEM VINDO A TOP 10 MAIORES CALCULADORAS DO BRASIL!")
num1 = int(input("Digite o primeiro número  "   ) )
num2 = int(input("Digite o segundo número   "   ) )

print("Escolha agora sua operação para ser calculado por mestres chineses:")
operacoesMat = {
    "+": "Para Adição",
    "-": "Para Subtrair",
    "*": "Para Mutiplicar",
    "/": "Para Dividir"
}
for operacao, tipo in operacoesMat.items():
  print(f"Você pode escolher {operacao} {tipo}")
escolha = input()
print(f"Tu escolheu {escolha} que fica configurado assim {num1} {escolha} {num2}")

if escolha in operacoesMat:
  if escolha == "+":
    resultado = num1 + num2;
  elif escolha == "-":
    resultado = num1 - num2;
  elif escolha == "*":
    resultado = num1 * num2;
  elif escolha == "/":
    resultado = num1 / num2;
  print(f"E a resposta é: {resultado}")
else:
  print("Da onde isso existe irmão? Faz direito aí pfvr")
