# Grid printing
# Celestin Nahimana
# March 2024

n = int(input("Enter a number between -6 and 2:\n"))     #Input received from the user
output = ""                                              #variable that will be used to display the outcome in grid form

if n < -6 or n > 2:                                      #Condition - if n is smaller than -6 or greater than 2 then it will display the message
    print("Invalid input! The value of 'n' should be between -6 and 2.")
else : 
    for i in range(6):                                    # For loop that will display outcome in rows
        for k in range(7):                                # For loop that will display outcome in columns
            if (n+k >= 0) and (n+k < 10):                                                                                                            #Condition - if n+ value of k is smaller than 10 or greater than/ equal to 2 then it will display the message 
                output = output + " " + str(n + k ) + " "    # Output is equal to previous output concated with a space and the sum of n and k
            else:
                output += str(n + k) + " "              # output is equal to previous output concated with the sum of n and k
        print(output)                                   # Print the output
        output = ""                                     # Clean and reset the output variable
        n = n + 7                                       # Add 7 to the input recieved from the user
        
      
   