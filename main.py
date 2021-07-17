#Programa que conta as mensagens de uma conversa de whatsapp de cada contacto.
#(suporta apenas os ficheiros.txt atuais da exportação de conversas do whatsapp).
#Versão 3.1(versão 3 é semelhante, mas no Thonny)


#Necessário para o sys.exit()
import sys 
#Necessário para o time.sleep()
#import time
#Necessário para o os.path.isfile()
import os.path


print("Comandos disponiveis: ajuda, iniciar e sair.")
print("Available commands: help, start and exit.")

#Função que funciona como launcher/hub para tudo.
def start_function():
    start = input()
    if start == "start" or start == "" or start== "RUN" or start== "Run" or start== "run" or start == "Start" or start == "iniciar" or start == "Iniciar" or start == "começar" or start == "Começar":
        print("A iniciar...")
        print("Starting...")
        print()
        gotofile()
    elif start == "help" or start == "Help" or start == "HELP" or start == "ajuda" or start == "Ajuda" or start == "AJUDA":
        print('Escreve um comando ("ajuda", "iniciar" ou "sair").')
        print("Atenção á capitalização.")
        print()
        print('Enter a command ("help", "start" or "exit").')
        print("Be aware of the capitalization.")
        start_function()
    elif start == "exit" or start == "Exit" or start == "EXIT" or start == "sair" or start == "Sair" or start == "SAIR" or start == "Let me out" or start == "LET ME OUT" or start == "Pó caralho!" :
        end()
    else:
        print("Comando não reconhecido.")
        print("Comandos disponiveis: ajuda, iniciar e sair.")
        print()
        print("Invalid command.")
        print("Available commands: help, start and exit.")
        start_function()
        

def gotofile():
    Speakers = []
    SpeakerNumbers = []
    SpeakerCharacters = []
    SpeakerSpaces = []
    AnomalyCount = 0
    mensagens = 0

    print('Cola o nome do fixeiro aqui (Inclui o ".txt").')
    print("Deixa em branco para usar o ficheiro default.")
    print()
    print("Paste the file name here (don't forget the" + ' ".txt" extention).')
    print("Leave it blanck to use the default file.")
    file = input()
    if file == "":
        file = "Teste.txt"
    if file[-4:] != ".txt":
        file += ".txt"
    if os.path.isfile(file) == False:
        print("Ficheiro não encontrado.")
        print("File not found.")
        print()
        gotofile()
    
    myfile = open(file, "r" , encoding="UTF-8")
    while myfile:
        line  = myfile.readline()
        Anomalia = False
        if line[2:3] == "/" and line[5:6] == "/" and line[8:9] == "," and line[12:13] == ":" and line[16:17] == "-":
            mensagens += 1
            i = 18
            while line[i:i+2] != ": " :
                
                if line[i:i+1] == "":
                    print("Anomalia.")
                    print("Anomaly.")
                    print(line)
                    print()
                    Anomalia = True
                    break
                i += 1
                
            if Anomalia == False:
                Speaker = line[18:i]
                i = 18
                spaces = 0
                letras = 0
                while line[i:i+1] != "":
                    if line [i] == " ":
                        spaces += 1
                    else:
                        letras += 1
                    i +=1
                if not Speaker in Speakers:
                    Speakers.append(Speaker)
                    SpeakerNumbers.append(0)
                    SpeakerCharacters.append(0)
                    SpeakerSpaces.append(0)
                n = Speakers.index(Speaker)
                SpeakerNumbers[n] += 1
                SpeakerCharacters[n] += letras
                SpeakerSpaces[n] += spaces
                
            elif Anomalia == True:
                AnomalyCount += 1
                Anomalia = False
            else:
                print("Erro determinação da identidade.")
                print("Failed to identify the speaker.")
                sys.exit()

        if line == "":
            break
    myfile.close()


    print(str(mensagens-AnomalyCount) + " Mensagens.")
    print(str(AnomalyCount) + "Anomalias.")
    print()
    print(str(mensagens-AnomalyCount) + " Mensages.")
    print(str(AnomalyCount) + "Anomalies.")

    ##apenas usado para testes (troubleshooting)
    #print (Speakers)
    #print (SpeakerNumbers)
    #print (SpeakerSpaces)
    #print (SpeakerCharacters)
    
    print()
    print("Who: - Messages: - Spaces: - Characters: - Words: - Words per message: - words per character")
    print("\n")
    lenght = len(Speakers)
    y = 0
    while y < lenght:
        print(str(Speakers[y]) + "  Messages:" + str(SpeakerNumbers[y]) + "  Spaces:" + str(SpeakerSpaces[y]) + "  Characters:" + str(SpeakerCharacters[y]) + "  Words:" + str(SpeakerSpaces[y] + 1) + "  Words per message:" + str((SpeakerSpaces[y] + 1)/SpeakerNumbers[y]) + "  characters per word:" + str((SpeakerCharacters[y])/(SpeakerSpaces[y] + 1)))
        y += 1
        print()
    start_function()
    
def end():
    print("Obrigado por utilizar.")
    print("Thank you for using my program.")
    sys.exit()
 
 
start_function()