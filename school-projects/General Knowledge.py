"""
Connor Finlay
General Knowledge Questions
"""
answer = " "
score = 0
print("What is the biggest state by population in America?")
answer = str(input())

answer = answer.upper()

if answer == "CALIFORNIA":
    print("Correct")
    score = score + 1
    print("Your score is", score)
else:
    print("Incorrect")


print("Who is the president of Russia?")
answer = str(input())

answer = answer.upper()

if answer == "VLADIMIR PUTIN":
    print("Correct")
    score = score + 1
    print("Your score is", score)
else:
    print("Incorrect")


print("Where is Quantanimo Bay?")
answer = str(input())

answer = answer.upper()

if answer == "CUBA":
    print("Correct")
    score = score + 1
    print("Your score is", score)
else:
    print("Incorrect")


print("What is the native language of Scotland?")
answer = str(input())

answer = answer.upper()

if answer == "GAELIC":
    print("Correct")
    score = score + 1
    print("Your score is", score)
else:
    print("Incorrect")

    
print("When did Israel become a country?")
answer = int(input())

if answer == 1948:
    print("Correct")
    score = score + 1
    print("Your score is", score)
else:
    print("Incorrect")



print("Who invented the computer?")
answer = str(input())

answer = answer.upper()

if answer == "CHARLES BAGGAGE":
    print("Correct")
    score = score + 1
    print("Your score is", score)
else:
    print("Incorrect")

print("What is the biggest state by land mass in America?")
answer = str(input())

answer = answer.upper()

if answer == "TEXAS":
    print("Correct")
    score = score + 1
    print("Your score is", score)
else:
    print("Incorrect")

#8
print("Who invented python?")
answer = str(input())

answer = answer.upper()

if answer == "GUIDO VAN ROSSUM":
    print("Correct")
    score = score + 1
    print("Your score is", score)
else:
    print("Incorrect")


print("What is the primary colour in the BMW logo?")
answer = str(input())

answer = answer.upper()

if answer == "BLACK":
    print("Correct")
    score = score + 1
    print("Your score is", score)
else:
    print("Incorrect")


print("Which manufacture created the first sports motorbike?")
answer = str(input())

answer = answer.upper()

if answer == "PETROLEUM REITWAGEN":
    print("Correct")
    score = score + 1
    print("Your score is", score)
else:
    print("Incorrect")


if score >=6:
    print("Well done you got 60%,you have passed with a score of" ,score)

else:
    print("You need to do some studying because you have failed with a score of",score)
