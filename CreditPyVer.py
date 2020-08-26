def checksum (number):
    counter = 0
    purelynumbers = 0
    doublednumbers = 0 
    rem = 0 
    while True: # forever loops unless break condition is met
        rem = number%10 # stores remainder as the digit
        number = number//10 # slices the last digit of the number // is int divide in python
        if counter%2 == 0:
            purelynumbers += rem
        else:
            #in the case we have a digit like 6
            #the doubled number is 12, but we need
            #to split it into the DIGITS 1 and 2
            #for the algorithm to work properly.
            if rem*2 >= 10:
                #adds the first digit of two digit num
                # to doublednumbers
                doublednumbers += (rem*2)//10 
                #adds the second digit
                doublednumbers += (rem*2)%10
            else:
                doublednumbers += (rem*2)
        counter += 1 
        #since the last loop will be when the number is a single digit.
        #it still stores the rem and then adds that digit so it is counted
        # if we have number = 0 rather than number < 10
        # 
        if number == 0:
            break
    return ((purelynumbers + doublednumbers)%10 == 0)
def getfirsttwodigits (num):
    while num >= 100:
        num = num//10
    return num
def getfirstdigit (num):
    while num >= 10:
        num = num//10
    return num
def getfirstnthdigits (n, num): 
    #set aside for more abstract use cases, like getting first
    #three digits
    while num >= 10**n:
        num = num//10
    return num
def getlength (num):
    counter = 0
    while num != 0:
        num = num // 10 # // means integer division in python
        counter+=1
    return counter
def identifycard(num):
    if checksum(num) and getlength(num) >= 13:
        if getfirstdigit(num) == 4:
            return("VISA\n")
        elif getfirsttwodigits(num) == 34 or getfirsttwodigits(num) == 37:
            return("AMEX\n")
        elif getfirsttwodigits(num) == 51 or getfirsttwodigits(num) == 52 or getfirsttwodigits(num) == 53 or getfirsttwodigits(num) == 54 or getfirsttwodigits(num) == 55:
            return("MASTERCARD\n")
    else:
        return("INVALID\n")

userinput = input("Number: ")
print(identifycard(userinput))