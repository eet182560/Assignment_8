all: ps1 ps2

ps1: ps1.py
	python3 ps1.py < input1.txt
	python3 ps1.py < input1_1.txt

ps2: ps2.py
	python3 ps2.py < input2.txt
	python3 ps2.py < input2_1.txt
	python3 ps2.py < input2_2.txt
