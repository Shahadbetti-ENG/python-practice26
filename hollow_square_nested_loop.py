# Hollow Square
# This program prints a hollow square using nested loop

# Number of rows and colums in the square
rows = 5

# Outer loop controls the rows (y-coordinate) (so i means y)
for i in range(rows):
    
    # Inner loop controls the columns (x-coordinate) (so j means x )
    for j in range(rows):
        
        
        # Print a star if the current position is:
        # The top row (i == 0)              # means y=0 (x,y) i=0            (j,i) (0,0) (1,0) (2,0) (3,0) (4,0)
        # The bottom row ( i == rows - 1)   # since rows=5 so y=4 (x,y) i=4  (j,i) (0,4) (1,4) (2,4) (3,4) (4,4) 
        # The left column (j == 0)          # means x=0 (x,y) j=0            (j,i) (0,0) (0,1) (0,2) (0,3) (0,4)
        # The right column (j == rows - 1)  # since rows=5 so x=4 (x,y) j=4  (j,i) (4,0) (4,1) (4,2) (4,3) (4,4)
        
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            
            # Display a star and stay on the same line 
            print("*", end=" ")
            
        else:
            # Display a space for the inside of the square
            print(" ", end=" ")
    
    # Move to the next line after completing a row
    print()
              
          