# Formulating a diagnosis
# Celestin Nahimana
# April 2024

print("--- Welcome to the Medical Diagnosis System ---")

print("Please answer the following questions with 'yes' or 'no'")

fever = input("Do you have a fever?\n")

if fever == "yes":
    cough = input("Do you have a cough?\n")
    if cough == "yes":
        headache = input("Do you have a headache?\n")
        if headache == "yes" : 
            rash = input("Do you have a rash?\n")
            if rash == "yes" :
                fatigued = input("Are you feeling fatigued?\n")
                if fatigued == "yes" : 
                    print("Based on your symptoms, you may have one of the following conditions: influenza, malaria, typhoid")
                else : 
                    print("Sorry, we could not diagnose your condition based on the information provided.")
            else:
                print("Sorry, we could not diagnose your condition based on the information provided.")
        else:
            print("Sorry, we could not diagnose your condition based on the information provided.")
    else:
        print("Sorry, we could not diagnose your condition based on the information provided.")
        
else:
    cough = input("Do you have a cough?\n")
    if cough == "yes" :
        headache = input("Do you have a headache?\n")
        if headache == "yes":
            rash = input("Do you have a rash?\n")
            if rash == "yes":
                fatigued = input("Are you feeling fatigued?\n")
                if fatigued == "yes":
                    print("Based on your symptoms, you may have one of the following conditions: pneumonia, tuberculosis, bronchitis")
                    
                else:
                    print("Sorry, we could not diagnose your condition based on the information provided.")
            else:
                print("Sorry, we could not diagnose your condition based on the information provided.")
        else:
            print("Sorry, we could not diagnose your condition based on the information provided.")
    else: 
        headache = input("Do you have a headache?\n")
        if headache == "yes":
            rash = input("Do you have a rash?\n")
            if rash == "yes":
                fatigued = input("Are you feeling fatigued?\n")
                if fatigued == "yes":
                    print("Based on your symptoms, you may have one of the following conditions:  migraine, meningitis, brain tumor")
                else:
                    print("Sorry, we could not diagnose your condition based on the information provided.")
                    
            else:
                print("Sorry, we could not diagnose your condition based on the information provided.")
        else:
            rash = input("Do you have a rash?\n")
            if rash == "yes":
                fatigued = input("Are you feeling fatigued?\n")
                if fatigued == "yes":
                    print("Based on your symptoms, you may have one of the following conditions:  measles, chickenpox, eczema")
                else:
                    print("Sorry, we could not diagnose your condition based on the information provided.")
            else: 
                fatigued = input("Are you feeling fatigued?\n")
                if fatigued == "yes":
                    print("Based on your symptoms, you may have one of the following conditions:  anemia, chronic fatigue syndrome, depression")
                else:
                    print("Sorry, we could not diagnose your condition based on the information provided.")
            
     
    
