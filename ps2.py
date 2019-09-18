import numpy as np

# Function Declarations and Definitions
# Display the matrix / board
def display(mat):
	print()
	print(mat[0: 3])
	print(mat[3 : 6])
	print(mat[6 : 9])


# Function to check sum is 15 or not and exit based on it
def sumCheck(sum, player):
	if sum == 15:		
		print("Winner is Player" + str(player) + "!!!")
		flag = input("Enter 1 to continue\n 0 to exit ")
		if flag == "1":
			Game()
		else:
			exit(0)


# Function to calculate sum rowwise based on pos
def rowSum(mat, pos, player, vis):

	#Initialization of variables
	sum = 0
	valid = False

	# Calculate sum for first row pos
	if pos in row1:
		sum = mat[0] + mat[1] + mat[2]
		if vis[0] and vis[1] and vis[2]:
			valid = True

	# Calculate sum for second row pos
	elif pos in row2:
		sum = mat[3] + mat[4] + mat[5]
		if vis[3] and vis[4] and vis[5]:
			valid = True

	# Calculate sum for third row pos
	else:
		sum = mat[6] + mat[7] + mat[8]
		if vis[6] and vis[7] and vis[8]:
			valid = True

	# Check validity of the sum and call sumCheck
	if valid:
		sumCheck(sum, player)


# Function to calculate sum column wise based on pos
def colSum(mat, pos, player, vis):

	#Initialization of variables
	sum = 0
	valid = False

	# Calculate sum for first column position
	if pos in col1:
		sum = mat[0] + mat[3] + mat[6]
		if vis[0] and vis[3] and vis[6]:
			valid = True

	# Calculate sum for second column position
	elif pos in col2:
		sum = mat[1] + mat[4] + mat[7]
		if vis[1] and vis[4] and vis[7]:
			valid = True

	# Calculate sum for third column position
	else:
		sum = mat[2] + mat[5] + mat[8]
		if vis[2] and vis[5] and vis[8]:
			valid = True

	# Check validity of the sum and call sumCheck
	if valid:
		sumCheck(sum, player)

# Function to calculate sum diagonally based on pos
def diagonal(mat, pos, player, vis):

	#Initialization of variables
	sum = 0
	valid = False

	# Calculate sum for second diagonal position
	if pos in diagonal1:
		sum = mat[0] + mat[4] + mat[8]
		if vis[0] and vis[4] and vis[8]:
			valid = True

	# Check validity of the sum and call sumCheck
	if valid:
		sumCheck(sum, player)

	# Calculate sum for second diagonal position
	if pos in diagonal2:
		sum = mat[2] + mat[4] + mat[6]
		if vis[2] and vis[4] and vis[6]:
			valid = True

	# Check validity of the sum and call sumCheck
	if valid:
		sumCheck(sum, player)


#Check for draw condition
def checkDraw(vis):
	flag = True
	for i in vis:
		if i == False:
			flag = False
			break

	# if draw then give user option to continue or exit
	if flag:
		print("Draw Condition!!!!!!!!!!!!!!!!!!!!!!")
		flag = input("Enter 1 to continue\n 0 to exit ")
		if flag == "1":
			Game()
		else:
			exit(0)


# Function to start a game
def Game():

	# Initialization of all variables
	mat = np.zeros(9, dtype=np.int32)
	vis = [False] * 9
	numVis = [False] * 9
	
	# Start of game with player1
	print("Welcome to the Game!")
	player = 1

	# Infinite to execute game
	while True:

		# take user input for position and number to be used
		print()
		print("Player " + str(player) + "'s Chance")
		pos, num = input("Enter the position and number to be entered: ").split(",")
		print(pos, num)

		# Check validity of position
		pos = int(pos)
		if pos < 1 or pos > 9:
			print("Invalid position")
			continue

		# Check validity of number
		num = int(num)
		if num < 1 or num > 9:
			print("Invalid number")
			continue

		# Check validity of number based on player's chance
		if player == 1 and num not in player1:
			print("Please enter odd number")
			continue
		elif player == 2 and num not in player2:
			print("Please enter even number")
			continue

		# Check validity of number and position 
		if vis[pos - 1] == True:
			print("Enter the position which is not used")
			continue
		if numVis[num - 1] == True:
			print("Enter the number which is not used yet")
			continue

		# update the variables for given input
		vis[pos - 1] = True
		numVis[num - 1] = True 
		mat[pos - 1] = num

		# Display current board status
		display(mat)

		# Check for winner if exists end the game else continue
		rowSum(mat, pos, player, vis)
		colSum(mat, pos, player, vis)
		diagonal(mat, pos, player, vis)	

		checkDraw(vis)

		# Switch the player
		if player == 1:
			player = 2
		else:
			player = 1


### Execution starts from here

player1 = {1, 3, 5, 7, 9}
player2 = {2, 4, 6, 8}
row1 = {1, 2, 3}
row2 = {4, 5, 6}
col1 = {1, 4, 7}
col2 = {2, 5, 8}
diagonal1 = {1, 5, 9}
diagonal2 = {3, 5, 7}
Game()