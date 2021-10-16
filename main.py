#Pede para o usuário os números e escolher qual vai ser o calculo 
x = float(input("Digite o número X:"))
op = input("Escolha a operação:")
y = float(input("Digite o número Y:"))

#Variável para receber o return da função 
resultado = 0

#Chama a função onde o usuário escolhe a operação algébrica 
def operacao(op,x,y,resultado):
	if op == '+':
		resultado = soma(x,y,resultado)
		return resultado
	elif op == '-':
		resultado = sub(x,y,resultado)
		return resultado
	elif op == 'X' or 'x':
		resultado = mult(x,y,resultado)
		return resultado
	elif op == '/':
		resultado = div(x,y,resultado)
		return resultado

#Função para somar 
def soma(x,y,resultado):
	resultado = x + y
	return resultado

#Função para subtrair
def sub(x,y,resultado):
	resultado = x - y
	return resultado

#Função para multiplicação 
def mult(x,y,resultado):
	resultado = x * y
	return resultado

#Função para divisão 
def div(x,y,resultado):
	resultado = x / y
	return resultado

#Recebendo o return da função 
resultado = operacao(op,x,y,resultado)
#Mostra o resultado para o usuário 
print(resultado)