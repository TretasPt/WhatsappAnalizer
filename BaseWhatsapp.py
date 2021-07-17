#Programa que conta as mensagens de uma conversa de whatsapp de cada contacto.
#(suporta apenas os ficheiros.txt atuais da exportação de conversas do whatsapp).
#Versão 3.1.


#Necessário para o sys.exit()
import sys 
#Necessário para o time.sleep()
#import time
#Necessário para o os.path.isfile()
import os.path
import main


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
    main.start_function()