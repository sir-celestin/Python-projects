# Calander program 
# Celestin Nahimana
# April 2024

import math


def day_of_week(day, month, year):
    # Your code here 
    m = month
    
    if m in [1,2]:
        m+=12
        year-=1          
        first_day_of_week = (((day + math.floor(13*(m+1)/5)+year+math.floor(year/4)-math.floor(year/100)+math.floor(year/400)-2)%7)+1)
        
        #Zeller’s congruence to work out day of the week 
    else:
        first_day_of_week = (((day + math.floor(13*(m+1)/5)+year+math.floor(year/4)-math.floor(year/100)+math.floor(year/400)-2)%7)+1)
        
    return first_day_of_week


def is_leap(year):
    
    #A boolean to find if it is a leap year
    # Your code here
    if year % 400 == 0:
        return True
        
    elif (year % 4 == 0 and year % 100 != 0):
        return True
    
    else :
        return False
        
        
def month_num(month_name):
    # Your code here
    #Assigns each month a month number

    month_name = month_name.lower().capitalize()
    months = ("January","February","March","April","May","June","July","August","September","October","November","December")
    
    for I in range(len(months)):
        if month_name == months[I]:
            num = I + 1 
        
    return num
                
def num_days_in(month_num, year):
    # Your code here
    
    if (is_leap(year) == True ) and (month_num == 2):  # gives number of days in a year
        return 29
            
    elif month_num in [1,3,5,7,8,10,12]:
        return 31 
        
    elif month_num in [4,6,9,11]:
        return 30
        
    else:
        return 28      


def num_weeks(month_num, year):
    # Your code here
    # Determine the first day of the month
    
    return math.ceil((num_days_in(month_num, year)+day_of_week(1, month_num, year)-1)/7)  

def week(week_num, start_day, days_in_month):
    # Your code here
    string=""
    if week_num==1:
        string+="   "*(start_day-1) #ensures date starts in correct column
        
        for i in range (start_day,8):
            date_num = i - start_day+1  #calculates the date
            string+=" "+str(date_num)+" "
    else:
        for i in range (7):
            date_num=(week_num-1)*7+i+2-start_day #calculates the date
            if date_num>days_in_month: # stops program after the last day of the month
                return string
            elif date_num<10:   #ensures alignment when num<10 by adding a space
                string+=" "+str(date_num)+" "
            else:
                string+=str(date_num)+" "
    return string


def main():
    # Your code here
    month_name = input("Enter month:\n")
    year = int(input("Enter year:\n"))
    
    month = month_num(month_name) 
    is_leap(year)
    
    days_in_month = num_days_in(month , year)
    first_day = day_of_week(1,month,year)
    
    week_num=1       
    
    print(month_name.title(),"\nMo Tu We Th Fr Sa Su")
    
    calender_str=week(week_num, first_day, days_in_month)
    
    
    while calender_str!= "":   #prints calender_str until string is empty
        print (calender_str)
        week_num+=1
        calender_str=week(week_num, first_day, days_in_month)    
     
     

if __name__=='__main__':
    main()
   





