# -*- coding: utf-8 -*-
"""CalculadoraEBAC.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18kRWrnVsVbXANoYSlNPNuZ-on5P5O6iI

EXERCICIO 1:

Agora, você fará a primeira parte do seu primeiro projeto! Como disse o professor Rodrigo, não há uma forma fixa: o importante é que seu código siga uma sequência lógica e tenha, ao menos, os critérios abaixo, ok?

Passo a passo:

Utilize o comando 'input' para receber ao menos 2 números de entrada do usuário;

Converta os valores recebidos pelo usuário para número inteiro (int) ou ponto flutuante (float);

Implemente ao menos 4 operações matemáticas em seu código;

Adicione um laço de repetição ou uma condicional. Por exemplo: você pode permitir que o usuário escolha qual operação realizar ou criar um loop que permita ao usuário realizar várias operações consecutivas;

Utilize o comando 'print' para exibir o resultado da operação matemática.
"""

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

{}