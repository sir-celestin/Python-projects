# Shift cypher program
# Celestin Nahimana
# April 2024


cypher = str(input("Enter the message:\n"))
key = int(input("Enter the key:\n"))
result = ""

for char in cypher:
    if char.isalpha():
        if char.islower():
            pos = ord('a') + (ord(char) - ord('a') + key) % 26
        else:
            pos = ord('A') + (ord(char) - ord('A') + key) % 26
        result += chr(pos)
    else:
        result += char

print(f"Result: {result.lower()}")
