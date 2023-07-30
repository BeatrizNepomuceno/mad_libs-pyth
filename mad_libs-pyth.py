

# Mad Libs em Python | Concatenação | English Fun Game
# Obs: noun = substantivo traduzido; verb = verbo traduzido | Exercício 
# Sujeito a modificações futuras

apresentação = input ('Olá, qual é o seu nome?')
print (apresentação, ', é um prazer te conhecer! Meu nome é Moshi! Vamos jogar?!')

apresentação2 = input ('Você já ouviu falar do MadLibs?') 
print ('Vou te explicar! MadLibs é um joguinho de palavras que formam frases divertidas, ele é bem famoso, talvez só você não conheça!')

print ('Vamos tentar?! O que será que vai acontecer? É impossível saber a frase final!')

print('É bom que você saiba diferenciar Substantivo de Verbo!')

noun = input("Substantivo: ")
verb = input("Verbo: ")
noun2 = input("Substantivo : ")
noun3 = input("Substantivo (plural): ")
verb2 = input("Verbo: ")
noun4 = input("Substantivo: ")

madlibs = f"Olá! Bem vindo ao {noun}. Aqui nós vamos {verb} sobre {noun2} e nos divertir {noun3}. Tenha certeza que iremos {verb2} para {noun4}."

print(madlibs) 

final = input ('Não é divertido?')
print ('Eu disse que era impossível advinhar!')