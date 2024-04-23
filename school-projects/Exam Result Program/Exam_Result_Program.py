from os import path, remove

fn_array = []
sn_array = []
sc_array = []

def readfile():
    entireFile = open("UASHSDDP1efiles notepad.txt", "r")
    linesArray = entireFile.read().splitlines()
    entireFile.close()

    for line in linesArray:
        linesParts = line.split(",")
        currentItem = linesParts[0]
        fn_array.append(currentItem)
        currentItem = linesParts[1]
        sn_array.append(currentItem)
        currentItem = linesParts[2]
        sc_array.append(currentItem)

    return fn_array, sn_array, sc_array


def calc_top_mark():
    maximum = max(sc_array)

    return maximum


def createFile(maximum):
    if path.exists("Highest Mark.txt"):
        remove("Highest Mark.txt")

    entireFile = open("Highest Mark.txt", "w")

    for m, fn, sn in zip(maximum, fn_array, sn_array):
        entireFile.write(m + ',' + fn + ',' + sn + '\n')
        entireFile.close()

def main():
    readfile()
    max = calc_top_mark()
    createFile(max)

if __name__ == "__main__":
    main()
