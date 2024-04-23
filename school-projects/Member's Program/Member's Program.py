#Connor Finlay 090570943
def get_new_info():                                                             #setting up subprogram
    n_fname = " "                                                               # setting up variable
    n_sname = " "                                                               # setting up variable
    n_category = " "                                                            # setting up variable
    n_password = " "                                                            # setting up variable
    print("Please enter new members firstname")                                 # asking user to firstname info
    n_fname = input()                                                           # recieving firstname storing it with in f_name
    print("Please enter new members surname")                                   # asking user for surname info
    n_sname = input()                                                           # recieving surname storing it within n_sname
    print("Please enter new members category (Adult, Senior or Junior)")        # asking user to input the category
    n_category = input()                                                        # recieving category, storing it within n_category

    password_result = False                                                     # setting boolean variable

    while not password_result:                                                  # setting up while not function
        print("Please enter new members password")                              # asking the member for their password
        n_password = input()                                                    # recieving and storing variable
        password_result = validatePassword(n_password)                          # calling in subprogram

    return n_fname, n_sname, n_category, n_password                             # returning varibles


def readfile():                                                                 #setting up subprogram
    f_array = []                                                                #setting up first name array
    s_array = []                                                                #setting up surname array
    c_array = []                                                                #setting up category array
    p_array = []                                                                #setting up password array
    entireFile = open("members.txt", "r")                                       #opening the file and reading it
    linesArray = entireFile.read().splitlines()                                 #splitting all the lines of text in the file
    entireFile.close()                                                          #closing the file

    for line in linesArray:                                                     #setting up function
        linesParts = line.split(",")                                            #telling the program how to split the data

        currentItem = linesParts[0]                                             #first bit of data is equal to current item
        f_array.append(currentItem)                                             #appending the value into the array

        currentItem = linesParts[1]                                             #second bit of data is equal to current item
        s_array.append(currentItem)                                             #appending the value into the array

        currentItem = linesParts[2]                                             #third bit of data is equal to current item
        c_array.append(currentItem)                                             #appending the value into the array

        currentItem = linesParts[3]                                             #fourth bit of data is equal to current item
        p_array.append(currentItem)                                             #appending the value into the array

    return f_array, s_array, c_array, p_array                                   #returning arrays


def validatePassword(n_password):                                               #setting up subprogram
    password_valid = False                                                      #setting up boolean
    first_character = n_password[:1]                                            #setting up variable for the first character of the password
    last_character = n_password[len(n_password) - 1:]                           #setting up varible for the last character of the password          

    if first_character.isupper() and (last_character >= chr(35) and last_character <= chr(37)):    #the input validation for finding out if the first character is uppercase and last character is a symbol
        password_valid = True                                                   #changing the state of the boolean to confirm that the input has been validated
        print("Your password is valid")                                         #telling the user that there password is valid
    else:
        print("Your password must include a capital letter at the start and either a '%,$,#' as the last character") #

        password_valid = False

    return password_valid

def append_values(n_fname, n_sname, n_category, n_password, f_array, s_array, c_array, p_array):
    f_array.append(n_fname)
    s_array.append(n_sname)
    c_array.append(n_category)
    p_array.append(n_password)

    return f_array, s_array, c_array, p_array

def counting_occurrences(c_array, f_array):
    length = len(c_array)
    a_count = 0
    j_count = 0
    s_count = 0
    t_count = 0
    for counter in range(0, length):
        if c_array[counter] == "Adult" or c_array[counter] == "adult":
            a_count = a_count + 1

        elif c_array[counter] == "Junior" or c_array[counter] == "junior":
            j_count = j_count + 1

        elif c_array[counter] == "Senior" or c_array[counter] == "senior":
            s_count = s_count + 1

    t_count = t_count + a_count + j_count + s_count

    return a_count, j_count, s_count, t_count


def display_arrays(f_array, s_array, c_array, adult_count, junior_count, senior_count, total_count):
    counter = 0
    print("Our members are:")
    for counter in range(0,len(f_array)):
        currentItem0 = f_array[counter]
        currentItem1 = s_array[counter]
        currentItem2 = c_array[counter]
        counter = counter + 1
    print(currentItem0 + "," + currentItem1 + "," + currentItem2 + "\n")
    print("There are currently", adult_count, "Adult members")
    print("There are currently", junior_count, "Junior members")
    print("There are currently", senior_count, "Senior members")
    print("Total membership is", total_count)


def main():
    n_fname, n_sname, n_category, n_password = get_new_info()
    f_array, s_array, c_array, p_array = readfile()
    f_array, s_array, c_array, p_array = append_values(n_fname, n_sname, n_category, n_password, f_array, s_array, c_array, p_array)
    adult_count, junior_count, senior_count, total_count = counting_occurrences(c_array, f_array)
    display_arrays(f_array, s_array, c_array, adult_count, junior_count, senior_count, total_count)

if __name__ == "__main__":
    main()
#Connor Finlay 090570943
