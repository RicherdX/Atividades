# Conversor de moeda
print("|Conversor de moeda|")
valor_reais = float(100.00)
taxa_dolar= float(5.60)
taxa_euro = float(6.60)
valor_convertido_dolar = valor_reais * taxa_dolar
valor_convertido_euro = valor_reais * taxa_euro
print(f"O valor R${valor_reais} convertido para: ")
print(f"Dólar: ${valor_convertido_dolar}")
print(f"Euros: €{valor_convertido_euro}")
print (" ")

# Calculadora de desconto
print("|Calculadora de desconto|")
produto = str("Camiseta")
preco_produto = float(50.00)
porcentagem_desconto = float(0.2)
desconto_calc = preco_produto * porcentagem_desconto
print(f"O preco final do produto {produto}, já com o desconto calculado, é de: R${desconto_calc:.2f}" )
print (" ")

# Calculadora de media escolar
print ("|Calculadora de media escolar|")
nota1 = float(7.5)
nota2= float(8.0)
nota3 = float(6.5)
mediafinal = (nota1 + nota2 + nota3) / 3
if mediafinal > 7.0:
    print(f"A media final do aluno é: {mediafinal:.2f}, logo está aprovado! ")
else: 
    print(f"A media final do aluno é: {mediafinal:.2f}, logo está reprovado")
print (" ")

# Calculadora de consumo médio
print ("|calculadora de consumo médio|")
dist_percorrida = float(300.00)
combust_gasto = float(25.00)
consumo_medio = dist_percorrida / combust_gasto
print(f"O veículo percorreu {dist_percorrida:.2f}Km, e gastou {combust_gasto:.2f}L de combustível. ")
print(f"Logo, o consumo médio(Km/L) foi de {consumo_medio:.2f}Km/L.")
print (" ")

# Calculadora de soma com entrada de usuário
print("|Calculadora de soma com entrada de usuário|")
A = int(input("Insira um número inteiro: "))
B = int(input("Insira um número inteiro: "))
X = A + B
print(f"X = {X}")
print(f"//Fim de código")
print (" ")

# Calculadora de salário por horas trabalhadas
print("|Calculadora de salário|")
numero_funcionario = int(input("Insira o número do funcionário: "))
horas_trabalhadas = int(input("Informe a quantidade de horas trabalhas: "))
valor_por_hora = float(input("Informe o valor por hora trabalhada: "))
salario = horas_trabalhadas * valor_por_hora
print(f"Salário por horas do funcionario N°{numero_funcionario} = R$ {salario:.2f}")
print (" ")
print("//Fim de códigos")