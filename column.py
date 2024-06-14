# Column printing
# Celestin Nahimana
# March 2024


n = int(input("Enter a number between -6 and 2:\n"))     #Input received from the user
current_number=0                                         #Initialises the variable used

if n < -6 or n > 2:                                      #Condition - if n is smaller than -6 or greater than 2 then it will display the message
    print("Invalid input! The value of 'n' should be between -6 and 2.")
else : 
    for i in range(6):                                  #For loop to display in columns
        current_number = n + i*7        #The current variable will inherit the sum of the input number and the product of i*7(adding seven to n)
        if current_number >= 0 and current_number < 10:   #Conditiion - if current_number is greater than/equal to zero or less than 10
            print(" " + str(current_number))              #Display the current number with a space in front
        else:
            print(str(current_number))                    # Display the number normally
