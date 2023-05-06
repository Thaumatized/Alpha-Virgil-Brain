import pyautogui;
import time;

pyautogui.PAUSE = 0

#sleep to allow people to resume to game
time.sleep(5)


#Solution in a relatively human readable form
rawsolution = '''
121 3 121 4 121 3 121 5

121 3 121 4 121 3 121 6

121 3 121 4 121 3 121 5 121 3 121 4 121 3 121 7

121 3 121 4 121 3 121 5 121 3 121 4 121 3 121 6 121 3 121 4 121 3 121 5 121 3 121 4 121 3 121 8

121 3 121 4 121 3 121 5 121 3 121 4 121 3 121 6 121 3 121 4 12
'''

#Spaces reset the level and new lines waste time
rawsolution = rawsolution.replace(" ", "").replace("\n", "")

# space to clear the level before beginning
cleansolution = [" "]
i = 0
while(i < len(rawsolution)):
	printstring = ""
	last = "0"
	#The game evaluates all keys in the same frame from small to big.
	#so we can input all keys which are in sequence bigger than the last on the same frame.
	while i < len(rawsolution) and rawsolution[i] > last:
		printstring += rawsolution[i]
		last = rawsolution[i]
		i += 1
	cleansolution.append(printstring)

for move in cleansolution:
	pyautogui.PAUSE = 0.0325
	pyautogui.write(move)
	print(move)
