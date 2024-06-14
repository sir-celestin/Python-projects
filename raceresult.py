# Race result programm
# Celestin Nahimana
# April 2024

r_name = input("Enter runner's name:\n") # Recieves name from user
r_time = float(input("Enter completion time (in mins):\n")) #  Recieves the completion time from user
r_prize = (input("Enter prize money (in rand):\n")) #Recieves the prize money amount from user
r_average = round( r_time/42.195 , 5)

print(f"\n{r_name} completed the race in {r_time} minutes and wins R{r_prize}.")
print(f"Their average time per kilometer was {r_average} minutes.")