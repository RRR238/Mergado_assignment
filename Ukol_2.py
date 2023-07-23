#function for checking whether the given number is prime or not
def check_prime(checking_value):
    if checking_value in [1, 2]:
        return True
    else:
        for i in range(2, int(checking_value / 2) + 1):
            if checking_value % i == 0:
                return False
                break
    return True

#create infinite loop so user can terminate the program by his/her decision
while True:

    user_input = input("vstup: ")
    input_converted = None

    #until user does not enter valid value, loop will run and ask for another input
    while type(input_converted) != int:
        try:
            input_converted = int(user_input)
        except:
            print("výstup: ","Invalid input!")
            user_input = input("vstup: ")

    check = False

    #loop which run until the nearest palindrome prime number is found
    while check == False:
        input_converted += 1
        s = str(input_converted)[::-1]
        #firstly check whether or not the incremented number is palindrome
        if s == str(input_converted):
            #then test if it is prime number
            check = check_prime(input_converted)

    print("výstup: ",input_converted)
