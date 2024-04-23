def readfile():
    DArray = [] ; diversArray = []; CArray = []; #setting variables

    entireFile = open("DiverDataREAL.txt","r") #openingfile
    linesArray = entireFile.read().splitlines() #ordering arrays
    entireFile.close() #closing file

    for line in linesArray: #setting up fixed loop
        linesParts = line.split(",") #

        currentItem = linesParts[0] #setting up arrays
        DArray.append(currentItem) #adding on values

        currentItem = linesParts[1] #setting up arrays
        diversArray.append(currentItem)

        currentItem = linesParts[2]
        CArray.append(currentItem)

    return DArray,diversArray,CArray

def Calc_totalScore(diversArray):
    winner = 0
    counter = 0
    loops = 0
    diversScores = [len(diversArray), 5]
    for diverI in range(0,len(diversArray)):
        for scoreI in range(0,5):
            print("Enter judges score for", diversArray[diverI], scoreI + 1)
            score = int(input())
            diversScores[diverI, scoreI] = score
                    
        print("The judge gave", diversArray[diverI], "to", diversScores[diverI, scoreI])
            
    return diversScores


def CalculateTotalScores(dScores):

    diversTotalScore = [len(diversArray)]
    
    for diverI in range(0, len(dScores[0])):        
        for scoreI in range(0, len(dScores[,0])):
            #calc total score
            diversTotalScore[diverI] = dScores[diverI, scoreI]   

    return diversTotalScore


#compute the min and max
#print it out



    #calc total score
    totalscore = jScore[0] + jScore[1] + jScore[2] + jScore[3] + jScore[4]   
    min = 10000000 #finding min
    max = 0#findmax() 
    for counter in range (0,5):

        if jScore[counter] < min:
            min = jScore[counter]

        if jScore[counter] > max:
            max = jScore[counter]
    print(min)
    print(max)

    N_totalscore = totalscore - (max + min)
    return N_totalscore

DiverIDArray, DiverNameArray, DiverCountryArray = readfile()
DiversScores = Calc_totalScore(diversArray)
New_totalScore = AddScore(DiversScores)

