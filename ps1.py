def checkVal(String):
	newList = list(String)
	for char in newList:
		if char == '0' or char == '1':
			continue
		else:
			return -1;

	return 0;


def calcParity(String):
	i = 0
	count = 0
	while i < len(String):
		if String[i] == '1':
			count += 1
		i += 1

	if count % 2 == 0:
		count = 1
	else:
		count = 0

	return count


String = input("Enter the binary String :")
print(String)

if checkVal(String) == -1:
	print("Invalid input")
	exit(0)

count = calcParity(String)

# print(count)
strParity = String + str(count)
print(strParity)

i = 0
newStr = ""
while i < len(strParity) - 3:
	if strParity[i : i + 4] == '010':
		newStr += strParity[i : i + 4] + '0'
	i += 1

print(newStr)


