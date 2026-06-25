# Tic-Tac-Toe Board
# Nested Loop
# Feature to build
# Print the game board

rows = 10

# Outer loop controls the rows
for i in range(rows):
    
    # Inner loop controls the columns
    for j in range(rows):
        
        # Print board lines:
        if i == 3 or i == rows - 4 or j == 3 or j == rows - 4:
        
            print("*", end=" ")
            
        else:
            print(" ", end=" ")
    # Move to the next row        
    print()
            