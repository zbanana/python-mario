# Asks for a number and prints a Mario style pyramid

def main():
	height = int(getHeight())
	printPyramid(height)


def printPyramid(height):
	for i in range(1, height + 1):
		line = " " * (height - i) + "#" * i + "  " + "#" * i
		print(line)

# Prompt user for a number. Repeat until user input is actually a number
def getHeight():
	height = input("Height: ")
	while not height.isdigit():
		height = input("Height: ")
	return height

if __name__ == "__main__":
	main()