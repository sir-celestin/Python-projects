# Row printing
# Celestin Nahimana 
# March 2024


n = int(input("Enter a number between -6 and 93:\n"))        #Input received from the user
output = ""                                                  #variable that will be used to display the outcome in grid form


if n < -6 or n > 93:                                       #Condition - if n is smaller than -6 or greater than 93 then it will display the message
    print("Invalid input! The value of 'n' should be between -6 and 93.")
else : 
    for i in range(7):                                     #For loop to display in rows
        if (n + i >= 0) and (n + i < 10):                  #Condition - if n is greater than/equal to zero or less than 10
            output += " " + str(n + i) + " "               #Output will have a space in front of it and be one more than previous output
        else:
            output += str(n + i) + " "                     #Output will be one more than previous output
    print(output)                                            # Display the number normally

        