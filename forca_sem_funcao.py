import random

palavras = ["Maçã", "Banana", "Mange", "Mamão", "Melão", "Melancia", "Uva", "Abacaxi", "Laranja"]
palavra = random.choice(palavras).lower().strip()
chances = 6
letras_certas = []
letras_erradas = []

print("**********************************")
print("*** Bem vindo ao jogo da forca ***")
print("**********************************")

while True:
    mensagem = []
    print()
    letra = str(input("Digite uma letra: "))

    if len(letra) > 1:
        print("Erro, digite somente uma letra")
        continue
    
    if letra in palavra:
        letras_certas.append(letra)

    else:
        letras_erradas.append(letra)
        chances -= 1

    for letra_secreta in palavra:
        if letra_secreta in letras_certas:
            mensagem += letra_secreta
        else:
            mensagem += '_'
            
    if '_' not in mensagem:
        print("Pararabéns, você ganhou!")
        print("Letras certas: ", letras_certas)
        print("Letras erradas: ",letras_erradas)
        break
        
    else:
        print("A palavra é: {}".format(mensagem))
    
    if chances <= 0:
        print("Você perdeu! Forca!")
        print("A palavra era: ", palavra.capitalize)
        break


    print("Você tem {} chances para acertar".format(chances))
    print("Letras certas: ",letras_certas)
    print("Letras erradas: ",letras_erradas)
    print()