# Message frame program
# Celestin Nahimana 
# April 2024

message = str(" " + input("Enter the message:\n") + " ")
m_repeat = int(input("Enter the message repeat count:\n"))
m_thickness = int(input("Enter the frame thickness:\n"))


#upper part of the frame
add_line = 0 
for I in range(m_thickness,0,-1):
    print("|"*add_line + "+" + "-"*(len(message) +(I - 1)*2) + "+" + "|"*add_line)
    add_line += 1

# middle part of the frame     
for i in range(m_repeat):
    print(m_thickness * "|" + message + m_thickness * "|")  

# bottom part of the frame 
m_thick = m_thickness
lines_2 = len(message) - 2

for i in range(m_thickness):
    m_thick -= 1
    lines_2 += 2 
    print( (m_thick) * "|" + "+" + (lines_2) * "-" + "+" + (m_thick) * "|")


