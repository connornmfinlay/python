def readfile():
    DArray = [] ; NArray = [];CArray = [];

    entireFile = open("DiverDataREAL.txt","r")
    linesArray = entireFile.read().splitlines()
    entireFile.close()

    for line in linesArray:
        linesParts = line.split(",")

        currentItem = linesParts[0]
        DArray.append(currentItem)

        currentItem = linesParts[1]
        NArray.append(currentItem)

        currentItem = linesParts[2]
        CArray.append(currentItem)

    return DArray,NArray,CArray

def validate_score(loops,NArray,counter):

    valid_score = False
    valid_NScore=0

    while valid_score == False:
        print("Judge ", loops + 1 , " please enter your score for",NArray[counter])
        NScore = int(input())
        
        if NScore >= 1 and NScore <=10:
            valid_score = True
        else:
            valid_score = False
            print("Please enter a value between 1 and 10")
    valid_score = False
    return NScore


def Calc_totalScore(NArray):
    winner = 0
    counter = 0
    loops = 0
    jScore = []
    NewTotalArray = [] 
    for counter in range(0,len(NArray)):
        jScore.clear()

        total =0
        for loops in range(0,5):
            currentScore = validate_score(loops,NArray,counter)
            jScore.append(currentScore)
            print("The judge gave", jScore[loops], "to", NArray[counter])
                    
                    
            total = total + jScore[loops]
            
        minimum,maximum = Calc_New_totalScore(jScore)
        total = total - (maximum + minimum)
        NewTotalArray.append(total)
    return NewTotalArray


def Calc_New_totalScore(jScore):
    #calc total score
    
    min= 100 #finding min
    max = 0#findmax()

    for counter in range (0,5):
        if jScore[counter] < min:
            min = jScore[counter]
        if jScore[counter] > max:
            max = jScore[counter]

    print(max)
    print(min)
    
    return(min, max)

def Finding_Winner(NewTotal,NArray):
    max = 0
    for counter in range(0,len(NArray)):
        if NewTotal[counter] >= max:
            max = NewTotal[counter]
            winner = NArray[counter]
    print(winner, "is the winner, they got ", max) 

    
DiverIDArray,DiverNamesArray,DiverCountryArray = readfile()
New_Total = Calc_totalScore(DiverNamesArray)
for counter in range(0,5):
    print(New_Total[counter])
Finding_Winner(New_Total,DiverNamesArray)
