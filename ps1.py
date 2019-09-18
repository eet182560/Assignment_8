# Function Defintions
# Function which check validity of string if it is binary or not
def checkVal(String):
	# Convert string into list
	newList = list(String)
	# Check string character by character 
	for char in newList:
		if char == '0' or char == '1':
			continue
		else:
			return -1;

	# Return 0 if in case of valid string else -1
	return 0;


# Function to calculate parity of string
def calcParity(String):

	# Initialization of variables
	i = 0
	count = 0

	# Count numbers of 1's
	while i < len(String):
		if String[i] == '1':
			count += 1
		i += 1

	# Check number of 1's is odd or even
	if count % 2 == 0:
		count = 1
	else:
		count = 0

	# Return parity
	return count


# Function which generate transmission data after bit stuffing if required
def generateTransmissiondata(strParity):

	# Initialization of variables
	i = 0
	j = 0

	# Copying string into list to append
	newStr = list(strParity)

	# Check for pattern '010' in input data
	while i < len(strParity) - 3:

		# If pattern is found append it with 0
		if strParity[i : i + 3] == '010':
			newStr.insert(j + 3, '0')
			i += 2
			j += 3
		i += 1
		j += 1

	# Return string with flag appended '0101' 
	return ''.join(newStr) + '0101'




## Execution start from here
# Take input from user
String = input("Enter the binary String :")
print(String)
#Check validity of String
if checkVal(String) == -1:
	print("Invalid input")
	exit(0)

# Calculate parity of string and print the string with parity
count = calcParity(String)
strParity = String + str(count)
print("Parity bit data : " + strParity)

# Calculate data to be transmitted and print the same
outPut = generateTransmissiondata(strParity)
print("Transmitting data: " + outPut)

