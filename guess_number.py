# -*- coding: utf-8 -*-
from random import randint

print("""
	Como vai a sua PARANORMALIDADE?
	Vamos ver quantos chutes você leva
	para acertar um número de 1 a 10
 
 """)
number = randint(1,10)
guess = -1   #numero a adivinhar
steps = 0    #chutes

while number != guess:    
	guess = int(input("Escolha um numero de 1 a 10 \n"))
	
	if guess < number:
		print("Muito baixo")
	elif guess > number: # elif means else if
		print ("Muito alto")

if steps == 1:
	print("Parabens! Voce é um médium")
elif steps > 1 and steps < 4:
	print ("Você tem potencial mas precisa praticar")
elif steps > 4:
	print ("Desculpe, você é um muggle")
