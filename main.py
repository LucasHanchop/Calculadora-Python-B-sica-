
x = float(input("Digite o número X:"))
op = input("Escolha a operação:")
y = float(input("Digite o número Y:"))

resultado = 0

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


def soma(x,y,resultado):
	resultado = x + y
	return resultado

def sub(x,y,resultado):
	resultado = x - y
	return resultado

def mult(x,y,resultado):
	resultado = x * y
	return resultado

def div(x,y,resultado):
	resultado = x / y
	return resultado

resultado = operacao(op,x,y,resultado)

print(resultado)