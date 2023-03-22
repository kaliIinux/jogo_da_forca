import random
import time
import inquirer
from inquirer.render.console import ConsoleRender
from inquirer.render.console._list import List

class OtherColorList(List):
    def get_options(self):
        choices = self.question.choices

        for choice in choices:
            selected = choice == choices[self.current]

            if selected:
                color = self.terminal.green
                symbol = '✔'
            else:
                color = self.terminal.normal
                symbol = ' '
            yield choice, symbol, color

class OtherListConsoleRender(ConsoleRender):
    
    def render_factory(self, question_type):
        if question_type != 'list':
            return super(ConsoleRender, self).render_factory(question_type)
        return OtherColorList

def modo():
    print("\x1b[2J\x1b[1;1H", end="")
    questions = [
        inquirer.List("opcaomodo", 
                      message="MENU",
                      choices=["FÁCIL", "MÉDIO", "DIFÍCIL", "SAIR"],
                      ),
    ]
    answers = inquirer.prompt(questions,render=OtherListConsoleRender())
    return answers['opcaomodo']

def play():
    print("\x1b[2J\x1b[1;1H", end="")
    questions = [
        inquirer.List("opcaoplay",
                      message="=====MENU=====",
                      choices=["JOGAR", "EDITAR LISTA", "SAIR"],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['opcaoplay']

def adicionar_excluir():
    print("\x1b[2J\x1b[1;1H", end="")
    questions = [
        inquirer.List("opcao", 
                      message="ESTA É A LISTA DE PALAVRAS, VOCÊ DESEJA\n ADICIONAR OU EXCLUIR UMA PALAVRA?",
                      choices=["ADICIONAR", "EXCLUIR", "VOLTAR"],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['opcao']
    
def imprime_mensagem_bem_vindo():
    print("**********************************")
    print("*** BEM VINDO AO JOGO DA FORCA ***")
    print("**********************************")

def carrega_palavra_secreta(palavras):
    palavras = ["maçã", "banana", "uva", "melancia", "abacaxi", "laranja"]
    palavra_secreta = random.choice(palavras).strip()
    return palavra_secreta

def lista_de_palavras():
    palavras = ["maçã", "banana", "uva", "melancia", "abacaxi", "laranja"]
    return palavras

def dicas(palavra_secreta):
    dicas = ["É uma fruta vermelha", "É uma fruta amarela", "É uma futa roxa", "É uma fruta verde por fora e vermelha por dentro", "É uma fruta que tem uma coroa", "É uma fruta laranja"]
    if palavra_secreta == "maçã":
        print(dicas[0])

    elif palavra_secreta == "banana":
        print(dicas[1])

    elif palavra_secreta == "uva":
        print(dicas[2])
    
    elif palavra_secreta == "melancia":
        print(dicas[3])
    
    elif palavra_secreta == "abacaxi":
        print(dicas[4])
    
    elif palavra_secreta == "laranja":
        print(dicas[5])

def chute():
    letra = str(input("Digite uma letra: ")).strip().lower()
    return letra

def mensagem_vitória(letras_certas, letras_erradas):
    print("Pararabéns, você ganhou!")
    print("Letras certas: ", letras_certas)
    print("Letras erradas: ",letras_erradas)

def mensagem_letra_errada(chances, letras_certas, letras_erradas):
    print("Você tem {} chances para acertar".format(chances))
    print("Letras certas: ",letras_certas)
    print("Letras erradas: ",letras_erradas)

def mensagem_chances_0(palavra_secreta):
    print("\x1b[2J\x1b[1;1H", end="")
    print("Você perdeu! Forca!")
    print("A palavra era: ", palavra_secreta.capitalize())

def cabeçalho(chances, mensagem, letras_certas, letras_erradas):
    print("\x1b[2J\x1b[1;1H", end="")
    print("Você tem {} chances".format(mensagem))
    print(f'Para receber uma dica, digite "dica"')
    print("Letras certas: {}".format(letras_certas))
    print("Letras erradas: {}".format(letras_erradas))
    print("A palavra é: {}".format(chances))

def fácil():
    
    palavras = lista_de_palavras
    palavra_secreta = carrega_palavra_secreta(palavras)

    letras_certas = []
    letras_erradas = []
    chances = 6

    while True:

        mensagem = []

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_certas:
                mensagem += letra_secreta
            else:
                mensagem += '_'

        if '_' not in mensagem:
            print("\x1b[2J\x1b[1;1H", end="")
            mensagem_vitória(letras_certas, letras_erradas)
            break
        
        cabeçalho(mensagem, chances, letras_certas, letras_erradas)
        letra = chute()
        print("\x1b[2J\x1b[1;1H", end="")
        
        if letra.isalpha():       
            if letra == "dica":
                dicas(palavra_secreta)
                time.sleep(2)
                
            elif len(letra) > 1 and letra != "dica":
                print("Opção inválida, digite uma letra")
                time.sleep(2)

            if letra in palavra_secreta:
                letras_certas.append(letra)

            elif letra not in palavra_secreta and len(letra) == 1:
                letras_erradas.append(letra)
                chances -= 1
        else:
            print("ERRO. Digite uma opção válida")
            time.sleep(2)
            
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_certas:
                mensagem += letra_secreta
            else:
                mensagem += '_'

        if chances <= 0:
            mensagem_chances_0(palavra_secreta)
            time.sleep(2)
            


def médio():
    
    palavras = lista_de_palavras()
    palavra_secreta = carrega_palavra_secreta(palavras)
    editar_lista = play()
    adicionar = adicionar_excluir()
    letras_certas = []
    letras_erradas = []
    chances = 4
    
    while editar_lista == "EDITAR LISTA":
        
        if adicionar == "ADICIONAR":
            print("LISTA DE PALAVRAS: ",palavras)
            novapalavra = input("DIGITE A PALAVRA: ")
            palavras.append(novapalavra)
            play()
        
        elif adicionar == "EXCLUIR":
            print("LISTA DE PALAVRASS: ", palavras)
            novapalavra = input("DIGITE A PALAVRA: ")
            palavras.remove(novapalavra)
            play()

    while True:
            
        mensagem = []

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_certas:
                mensagem += letra_secreta
            else:
                mensagem += '_'

        if '_' not in mensagem:
            print("\x1b[2J\x1b[1;1H", end="")
            mensagem_vitória(letras_certas, letras_erradas)
            break
        
        cabeçalho(mensagem, chances, letras_certas, letras_erradas)
        letra = chute()
        print("\x1b[2J\x1b[1;1H", end="")
        
        if letra.isalpha():       
            if letra == "dica":
                dicas(palavra_secreta)
                time.sleep(2)
                
            elif len(letra) > 1 and letra != "dica":
                print("Opção inválida, digite uma letra")
                time.sleep(2)

            if letra in palavra_secreta:
                letras_certas.append(letra)

            elif letra not in palavra_secreta and len(letra) == 1:
                letras_erradas.append(letra)
                chances -= 1
        else:
            print("ERRO. Digite uma opção válida")
            time.sleep(2)
            
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_certas:
                mensagem += letra_secreta
            else:
                mensagem += '_'

        if chances <= 0:
            mensagem_chances_0(palavra_secreta)
            time.sleep(2)
            
def difícil():
        
    palavra_secreta = carrega_palavra_secreta()

    letras_certas = []
    letras_erradas = []
    chances = 3

    while True:

        mensagem = []

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_certas:
                mensagem += letra_secreta
            else:
                mensagem += '_'

        if '_' not in mensagem:
            print("\x1b[2J\x1b[1;1H", end="")
            mensagem_vitória(letras_certas, letras_erradas)
            break
        
        cabeçalho(mensagem, chances, letras_certas, letras_erradas)
        letra = chute()
        print("\x1b[2J\x1b[1;1H", end="")
        
        if letra.isalpha():       
            if letra == "dica":
                dicas(palavra_secreta)
                time.sleep(2)
                
            elif len(letra) > 1 and letra != "dica":
                print("Opção inválida, digite uma letra")
                time.sleep(2)

            if letra in palavra_secreta:
                letras_certas.append(letra)

            elif letra not in palavra_secreta and len(letra) == 1:
                letras_erradas.append(letra)
                chances -= 1
        else:
            print("ERRO. Digite uma opção válida")
            time.sleep(2)
            
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_certas:
                mensagem += letra_secreta
            else:
                mensagem += '_'

        if chances <= 0:
            mensagem_chances_0(palavra_secreta)
            time.sleep(2)
            
def jogar():
    
    imprime_mensagem_bem_vindo()
    print()
    dificuldade = modo()
    
    if  dificuldade == "FÁCIL":
        fácil()
        
    elif dificuldade == "MÉDIO":
        médio()
        
    elif dificuldade == "DIFÍCIL":
        difícil()
        
    elif dificuldade == "SAIR":
        exit()
    else:
        print("OPÇÃO INVÁLIDA")

if __name__ == "__main__":
    jogar()
