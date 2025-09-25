rows = 7
cols = 9

for i in range(rows):
    for j in range(cols):
        # Conditions to print stars for smiley face features
        
        # Outer circle
        if (i == 0 or i == rows-1) and (2 <= j <= 6):
            print("*", end="")
        elif (i == 1 or i == rows-2) and (1 <= j <= 7):
            print("*", end="")
        
        # Eyes
        elif (i == 2 and (j == 2 or j == 6)):
            print("*", end="")
        
        # Mouth
        elif (i == 4 and (3 <= j <= 5)):
            print("*", end="")
        
        # Face border sides
        elif (1 < i < rows-1) and (j == 1 or j == cols-2):
            print("*", end="")
        
        else:
            print(" ", end="")
    print()  # New line
