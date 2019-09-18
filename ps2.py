import numpy as np


def display(mat):

	print(mat[0: 3])
	print(mat[3 : 6])
	print(mat[6 : 9])


def sumCheck(sum, i):
	if sum == 15:		
		print("Winner is Player" + str(i) + "!!!")
		exit(0)


def rowSum(mat, pos, i, vis):
	sum = 0
	valid = False

	if pos in row1:
		sum = mat[0] + mat[1] + mat[2]
		if vis[0] and vis[1] and vis[2]:
			valid = True

	elif pos in row2:
		sum = mat[3] + mat[4] + mat[5]
		if vis[3] and vis[4] and vis[5]:
			valid = True

	else:
		sum = mat[6] + mat[7] + mat[8]
		if vis[6] and vis[7] and vis[8]:
			valid = True

	if valid:
		sumCheck(sum, i)


def colSum(mat, pos, i, vis):

	sum = 0
	valid = False

	if pos in col1:
		sum = mat[0] + mat[3] + mat[6]
		if vis[0] and vis[3] and vis[6]:
			valid = True

	elif pos in col2:
		sum = mat[1] + mat[4] + mat[7]
		if vis[1] and vis[4] and vis[7]:
			valid = True

	else:
		sum = mat[2] + mat[5] + mat[8]
		if vis[2] and vis[5] and vis[8]:
			valid = True

	if valid:
		sumCheck(sum, i)


def diagonal(mat, pos, i, vis):

	sum = 0
	valid = False

	if pos in diagonal1:
		sum = mat[0] + mat[4] + mat[8]
		if vis[0] and vis[4] and vis[8]:
			valid = True


	if valid:
		sumCheck(sum, i)

	if pos in diagonal2:
		sum = mat[2] + mat[4] + mat[6]
		if vis[2] and vis[4] and vis[6]:
			valid = True

	
	if valid:
		sumCheck(sum, i)


mat = np.zeros(9, dtype=np.int32)
vis = [False] * 9
numVis = [False] * 9
player1 = {1, 3, 5, 7, 9}
player2 = {2, 4, 6, 8}

row1 = {1, 2, 3}
row2 = {4, 5, 6}
col1 = {1, 4, 7}
col2 = {2, 5, 8}
diagonal1 = {1, 5, 9}
diagonal2 = {3, 5, 7}

print("Welcome to the Game!")
i = 1
while True:
	print()
	print("Player " + str(i) + "'s Chance")
	pos, num = input("Enter the position and number to be entered: ").split(",")

	pos = int(pos)
	if pos < 1 or pos > 9:
		print("Invalid position")
		continue

	num = int(num)
	if num < 1 or num > 9:
		print("Invalid number")
		continue

	if i == 1 and num not in player1:
		print("Please enter odd number")
		continue
	elif i == 2 and num not in player2:
		print("Please enter even number")
		continue

	if vis[pos - 1] == True:
		print("Enter the position which is not used")
		continue
	if numVis[num - 1] == True:
		print("Enter the number which is not used yet")
		continue

	vis[pos - 1] = True
	numVis[num - 1] = True 
	mat[pos - 1] = num

	display(mat)
	rowSum(mat, pos, i)
	colSum(mat, pos, i)
	diagonal(mat, pos, i)	

	if i == 1:
		i = 2
	else:
		i = 1
