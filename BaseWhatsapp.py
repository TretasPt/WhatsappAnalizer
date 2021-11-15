#Programa que conta as mensagens de uma conversa de whatsapp de cada contacto.
#(suporta apenas os ficheiros.txt atuais da exportação de conversas do whatsapp).
#Versão 4.1.


#Necessário para o sys.exit()
import sys 
#Necessário para o time.sleep()
#import time
#Necessário para o os.path.isfile()
import os.path
import main


#Pede o nome do ficheiro e caso não exista, avisa o utilizador. 
def getfile():
    print('Cola o nome do fixeiro aqui (Inclui o ".txt").')
    print("Deixa em branco para usar o ficheiro default." 'Escreve "sair" para sair.')
    print()
    print("Paste the file name here (don't forget the" + ' ".txt" extention).')
    print("Leave it blanck to use the default file." 'Write "quit" to exit.' )
    file = input()
    if file == "quit" or file == "sair":
        main.hub_start();
    if file == "":
        file = "Teste.txt"
    if file[-4:] != ".txt":
        file += ".txt"
    if os.path.isfile(file) == False:
        print("Ficheiro não encontrado.")
        print("File not found.")
        print()
        getfile()
    analize(file)

def analize(file):
    filevar = file
    Speakers = []
    SpeakerNumbers = []
    SpeakerCharacters = []
    SpeakerSpaces = []
    AnomalyCount = 0
    mensagens = 0

    
    
    myfile = open(filevar, "r" , encoding="UTF-8")
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



    columns =(Speakers,SpeakerNumbers,SpeakerSpaces,SpeakerCharacters)

    longElement=[]
    for j in range(len(columns)):
        longElement.append(100)
        longElement[j] = len(str(columns[j][0]))
        for i in range(len(columns[j])):
            if longElement[j] < len(str(columns[j][i])):
                longElement[j] = len(str(columns[j][i]))

    output(longElement,columns)
   

def howLong(string,max):
    return max-len(str(string))


def output(longElement,columns):
 
    print()

    for j in range(len(columns[0])):#LINE
        # for k in range(4):
        for i in range(len(columns)):#COLUMN
            print('|' + '-'* longElement[i],end="")
        print("|")
        for i in range(len(columns)):#COLUMN
            print('|' + str(columns[i][j]) + ' '* howLong(columns[i][j],longElement[i]),end="")
        print("|")
        for i in range(len(columns)):#COLUMN
            print('|' + ' '* longElement[i],end="")
        print("|")
        for i in range(len(columns)):#COLUMN
            print('|' + ' '* longElement[i],end="")
        print("|")
    for i in range(len(columns)):#COLUMN
            print('|' + '-'* longElement[i],end="")
    print("|")