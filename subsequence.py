# Sequence program
# Celestin Nahimana 
# April 2024

seq_1 = str(input("Enter the full string:\n"))
seq_2 = str(input("Enter the subsequence to check for:\n"))

# Check if seq_2 is empty or contains no alphanumeric characters
if not seq_2 or not any(char.isalnum() for char in seq_2):
    print("The given substring is not a subsequence of the full string.")
else:
    counter = 0 
    start_index = 0

    while counter < len(seq_2):
        index = seq_1.find(seq_2[counter], start_index)
        if index == -1:
            print("The given substring is not a subsequence of the full string.")
            break
        start_index = index + 1
        counter += 1

    if counter == len(seq_2):
        print("The given substring is a subsequence of the full string.")
