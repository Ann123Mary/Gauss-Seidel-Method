n=int(input("Enter number of rows in your matrix:"))

#MATRIX A
matrix_A=[]
for i in range(n):
    row_A=input("Enter the value matrix A separted by commas:")
    row_A=[float(value) for value in row_A.split(",")]#row_A.split(",") Gives you strings (eg:["1","2","3"]).
                        #row_A=[float(value) for value in row_A.split(",")] Gives turns those strings into float.    
    matrix_A.append(row_A)
print("Matrix A:",matrix_A)

#MATRIX B
matrix_B=[]
for i in range(n):
    row_B=[]
    row_B=input("Enter the values of matrix B:")
    matrix_B.append(float(row_B)) #Converts the string values in row_B to float.
print("Matrix B:",matrix_B)

#EXPECTED ANSWER BY THE USER
row_ea=input("Enter expected answer(x,y,z):")#matrix of expected answer.

#INTIAL APPROXIMATION
x=int(input("Enter the initial approximation value of x:"))
y=int(input("Enter the initial approximation value of y:"))
z=int(input("Enter the initial approximation value of z:"))

iterations=int(input("Enter the number of iterations:"))

#ITERATIONS
for i in range(iterations):
    print("INTERATION:",i+1)
    # Calculate x
    x=(matrix_B[0] - matrix_A[0][1]*y - matrix_A[0][2]*z)/matrix_A[0][0]
    # Calculate y using NEW x
    y=(matrix_B[1] - matrix_A[1][0]*x - matrix_A[1][2]*z)/matrix_A[1][1]
    # Calculate z using NEW x and NEW y
    z=(matrix_B[2] - matrix_A[2][0]*x - matrix_A[2][1]*y)/matrix_A[2][2]

    print("The value of (x,y,z) is:",(x,y,z))

    
