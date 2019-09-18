import numpy as np


def display(mat):

	for i in range(3):
		for j in range(3):
			index = i + j
			print(index)
			print(mat[index])


mat = np.zeros(9)
vis = [False] * 9
numVis = [False] * 9
player1 = {1, 3, 5, 7, 9}
player2 = {2, 4, 6, 8}

print("Welcome to the Game!")

i = 1

while True:
	print()
	print("Player " + str(i) + "'s Chance")
	pos, num = input("Enter the position and number to be entered: ").split()

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

	if i == 1:
		i = 2
	else:
		i = 1
		break

	
