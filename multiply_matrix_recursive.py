# Recursive code for Matrix Multiplication 
# https://www.geeksforgeeks.org/matrix-multiplication-recursive/

# n*n matrix = (n/2)*(n/2)
# 9 multiply = (n/2)*(n/2) --> sub matrix
# 4 sum = (n/2)*(n/2)  --> sub matrix
# T(n)= 8T(n/2)+O(n^2)
# 8=submatrix count, n/2=submatrix size, n^2= submatrix sum 

MAX = 100
i = 0
j = 0
k = 0

def multiplyMatrixRec(row1, col1, A, 
					row2, col2, B, C): 

	global i 
	global j 
	global k 
	
	# If all rows traversed. 
	if (i >= row1): 
		return
		
	# If i < row1 
	if (j < col2): 
		if (k < col1): 
			C[i][j] += A[i][k] * B[k][j] 
			k += 1
			multiplyMatrixRec(row1, col1, A, 
							row2, col2,B, C) 

		k = 0
		j += 1
		multiplyMatrixRec(row1, col1, A, 
						row2, col2, B, C) 

	j = 0
	i += 1
	multiplyMatrixRec(row1, col1, A, 
					row2, col2, B, C) 

# Function to multiply two matrices 
# A[][] and B[][] 
def multiplyMatrix(row1, col1, A, row2, col2, B): 
	if (row2 != col1): 
		print("Not Possible") 
		return

	C = [[0 for i in range(MAX)] 
			for i in range(MAX)] 
	multiplyMatrixRec(row1, col1, A, 
					row2, col2, B, C) 
	
	# Print the result 
	for i in range(row1): 
		for j in range(col2): 
			print( C[i][j], end = " ") 
		print() 

# Driver Code 
A = [[1, 2], 
	[4, 5]] 

B = [[1, 2], 
	[4, 5]] 

row1 = 2
col1 = 2
row2 = 2
col2 = 2
multiplyMatrix(row1, col1, A, row2, col2, B) 


