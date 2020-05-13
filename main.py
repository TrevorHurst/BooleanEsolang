Instructions = open('Test.bb','r').readlines() #Open file
chars = [i for i in "[]+<>,."] # Make a list of allowed chars (You can comment your code)
step = [] # Used to keep track of your instructions
ram = [False for i in range(512)] # Initialize the RAM to 512 bits 64bytes
pointer = 0 #Points to a location in RAM
for line in Instructions: #Iterate through the line(s) of your program
    for c in line: #Iterates through each character
        if c in chars: #Checks if character is code or comment
            step+=c # Adds code instructions to step list

los = [] #Loop Open Statements keeps track of open loops
lcs = [] #Loop Close Statements keeps track of close loops
if step.count('[') != step.count(']'): #Ensures you have balanced []
    raise Exception("Unbalanced []'s")

for i in range(len(step)):
    if step[i] == '[': 
        los.append(i) #Add the index of open lists to los
    if step[i] == ']':
        lcs.append(i) #Add the index of close lists to lcs
lcs = lcs[::-1] #Invert lcs so the [ and ] have the same index on every loop

i = 0
while i < len(step): #Step through the instructions    
    if step[i] == '>':
        pointer+=1 #Moves pointer up through ram
        if pointer < 0:
          raise Exception('Null Pointer')    
    if step[i] == '<':
        pointer-=1 #Moves pointer down through ram
        if pointer < 0:
          raise Exception('Null Pointer')
    
    if step[i] == '+':
        ram[pointer] = not ram[pointer] #Inverts ram state RAM can only be 1 or 0
    
    if step[i] == ',':
        ram[pointer] = bool(input()) #Takes user input, 1 or 0
    
    if step[i] == '.':
        print(int(ram[pointer]),end='') #Prints current bit
    
    if step[i] == ']': #The ] Does all the work in a loop
        if ram[pointer] == 1: #If selected bit is a 1, go to start of loop
            _ = lcs.index(i) #Temp variable that holds the index of the loop
            i = los[_] #This allows for nested loops
    i += 1

def b2b(l): #This function returns the ram in blocks of 8
    for i in range(0,len(l),8): # blocks of 8 result in a stack of 64 bytes
        yield list(map(int,l[i:i + 8])) #A byte can store values up to 255
byts = list(b2b(ram)) #Alltogether you can represent 2^512 that's over a googol


print()
for i in byts: #Display all the bytes this can be commented out
    print(i)