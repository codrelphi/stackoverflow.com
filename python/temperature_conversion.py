'''
Python program to convert temperature from Celsius,
Fahrenheit or Kelvin. These next lines of code (loc) introduce
the program and ask user for temperature to be converted.
'''
import sys # to exit when user makes error.


# function to determine which temperature user wishes to convert from.
def FromTemp(user_temp):
    if user_temp1[-1] == 'C' or user_temp1[-1] == 'c':
        print ("You wish to convert from Celsius.")
    elif user_temp1[-1] == 'F' or user_temp1[-1] == 'f':
        print ("You wish to convert from Fahrenheit.")
    elif user_temp1[-1] == 'K' or user_temp1[-1] == 'k':
        print ("Ah! Yes, the elusive Kelvin!")
    else:
        print ("You must think me mad; I only allow C, F and K.")
        sys.exit() # exits when user makes mistake.

# function to make conversion from and to appropriate thermal unit.
def ToTemp(raw_temp):
    if destin_temp.lower() == 'c' and user_temp1[-1].lower() == 'f':
        f_to_c = round(float((raw_temp - 32) * 5/9), 2)
        print (real_temp, "degrees Fahrenheit is", f_to_c, "degrees Celsius.\n")
        print ("****Thank you for stopping by!****\n") #good
    elif destin_temp.lower() == 'f' and user_temp1[-1].lower() == 'c':
        c_to_f = round(float(raw_temp * (9/5) + 32), 2)
        print (real_temp, "degrees Celsius is", c_to_f, "degrees Fahrenheit.")
        print ("****Thank you for stopping by!****\n") #good
    elif destin_temp.lower() == 'c' and user_temp1[-1].lower() == 'k':
        k_to_c = round(float(raw_temp - 273.15), 2)
        print (real_temp, "degrees Kelvin is", k_to_c, "degrees Celsius.")
        print ("****Thank you for stopping by!****\n") # doesn't work
    elif destin_temp.lower() == 'k' and user_temp1[-1].lower() == 'c':
        c_to_k = round(float(raw_temp + 273.15), 2)
        print (real_temp, "degrees Celsius is", c_to_k, "degrees Kelvin.")
        print ("****Thank you for stopping by!****\n") # doesn't work
    elif destin_temp.lower() == 'f' and user_temp1[-1].lower() == 'k':
        k_to_f = round(float((raw_temp - 273.15) * (9/5) + 32), 2)
        print (real_temp, "degrees Kelvin is", k_to_f, "degrees Fahrenheit.")
        print ("****Thank you for stopping by!****\n") # doesn't work
    elif destin_temp.lower() == 'k' and user_temp1[-1].lower() == 'f':
        f_to_k = round(float(raw_temp - 32 *(5/9) + 273.15), 2)
        print (real_temp, "degrees Fahrenheit is", f_to_k, "degrees Kelvin.")
        print ("****Thank you for stopping by!****\n") # doesn't work
    else:
        print("You made a mistake somewhere. Try again later.")
        sys.exit()


if __name__ == "__main__":

    print ("\n****Welcome to your own advanced temperature conversion application!****\n")
    print ("^^^What would you like to convert?^^^")
    print ("Type 'C' for Celsius, 'F' for Fahrenheit and 'K' for Kelvin \
     after entering digits. (Ex: '34C')\n")
    user_temp1 = input('--> ')

    FromTemp(user_temp1)

    # asks user for desired conversion rate.
    print ("\n^^^What would you like to convert to? (Enter 'C', 'F' or 'K')^^^\n")
    destin_temp = input("--> ")

    # stripping the numbers from the temperature symbol.
    real_temp = user_temp1[:- 1]
    raw_temp = int(real_temp)

    ToTemp(raw_temp)
