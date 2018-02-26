from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys

S8yPositionCorrection = 0

yMainTabPosition = 1380
yPowerUpsPosition = 2250

defaulXPosition = 1270

queenCellHeight = 290

crabTab = 120
queenTab = 450
abilityTab = 750

def log(message):
	if DEBUG:
		print("CRABWAR:: " + message)

def sleep(time):
	MonkeyRunner.sleep(time)

def openMenu():
	device.touch(1350, 2470 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.3)

def closeMenu():
	device.touch(1350, 1220 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.3)

def move(dY, direction):
	if (direction == 'UP'):
		device.drag((defaulXPosition, 2000), (defaulXPosition, 2000 + dY), 1.0, 10)
	else:
		device.drag((defaulXPosition, 2000), (defaulXPosition, 2000 - dY), 1.0, 10)
	
	sleep(0.2)

def buyCrabEvolution(Y):
	for x in range(0, 10):
		device.touch(defaulXPosition, Y + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.5)
		device.touch(defaulXPosition, Y + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.5)

def buyCrabEvolutionWithPattern(listOfPatterns):
	for x in range(0, 10):
		device.touch(defaulXPosition, 2000 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.5)

		if listOfPatterns[x] == "R":
			device.touch(defaulXPosition, 2000 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		else:
			device.touch(420, 2000 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)

		sleep(0.5)	

def buyCrabLevels():
	log("Buying crab levels")
	openMenu()

	#click on crab lvl tav
	device.touch(crabTab, yMainTabPosition + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.2)
	#move to top position on carb lvl tab
	move(2000, 'UP')
	#long press on crab lvl
	device.touch(defaulXPosition, 1560 + S8yPositionCorrection, MonkeyDevice.DOWN)
	sleep(1)
	device.touch(defaulXPosition, 1560 + S8yPositionCorrection, MonkeyDevice.UP)
	sleep(0.1)
	#end long press

	#buy 4k crab lvls
	for x in range(0, 4): 
		device.touch(740, 1560 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)	
		sleep(0.2)

	log("Buying ametist evolution")
	buyCrabEvolutionWithPattern(["R","R","L","R","R","L","L","L","R","R"])
	# buyCrabEvolution(2000)
	move(370, 'DOWN')
	log("Buying emerald evolution")
	buyCrabEvolutionWithPattern(["R","R","L","R","R","R","L","L","R","R"])
	# buyCrabEvolution(2000)
	move(370, 'DOWN')
	log("Buying garnet evolution")
	buyCrabEvolutionWithPattern(["R","R","R","L","R","L","R","R","L","R"])
	# buyCrabEvolution(2000)

	move(2000, 'UP')

	closeMenu()

def buySkill(abilityLocation, talentLocation):
	applyPosition = 1800

	if (initialGame):
		times = 50
	else:
		times = 5

	if (initialGame):
		for x in range (0, 4):
			device.touch(defaulXPosition, abilityLocation + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
			sleep(0.2)

		device.touch(defaulXPosition, talentLocation + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.2)
		device.touch(defaulXPosition, applyPosition + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.2)

		#close window
		device.touch(1330, 700 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.2)

	#buy lvls
	for x in range(0, times):
		device.touch(defaulXPosition, abilityLocation + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.1)


def buyAllSkills():
	log("Buying all skills")
	position1 = 1150
	position3 = 1550
	colossalYLocation = 1600
	shadowYLocation = 1850
	smokeYLocation = 2100
	frenzyYLocation = 2350
	geneticYLocation = 2150
	goldenYLocation = 2400

	openMenu()

	device.touch(abilityTab, yMainTabPosition + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.2)

	move(1000, 'DOWN')

	buySkill(goldenYLocation, position1)
	buySkill(geneticYLocation, position3)
	move(1000, 'UP')
	buySkill(shadowYLocation, position3)
	buySkill(frenzyYLocation, position3)
	buySkill(smokeYLocation, position3)
	buySkill(colossalYLocation, position3)

	closeMenu()

def buyQueen(posicaoY):
	#long press
	device.touch(defaulXPosition, posicaoY + S8yPositionCorrection, MonkeyDevice.DOWN)
	sleep(1)
	device.touch(defaulXPosition, posicaoY + S8yPositionCorrection, MonkeyDevice.UP)
	sleep(0.1)
	#end long press

	for i in range(0, 3):
		device.touch(730, posicaoY + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.1)

	for j in range(0, 10):
		device.touch(defaulXPosition, posicaoY + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.1)

	#long press
	device.touch(defaulXPosition, posicaoY + S8yPositionCorrection, MonkeyDevice.DOWN)
	sleep(1)
	device.touch(defaulXPosition, posicaoY + S8yPositionCorrection, MonkeyDevice.UP)
	sleep(0.1)
	#end long press

	for i in range(0, 5):
		device.touch(730, posicaoY + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.1)

	for i in range(0, 5):
		device.touch(1000, posicaoY + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.1)

	for j in range(0, 10):
		device.touch(defaulXPosition, posicaoY + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.1)

def buyLastQueens():
	log("Buying last queens")
	openMenu()

	device.touch(queenTab, yMainTabPosition + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.2)

	move(10000, 'DOWN')
	sleep(0.2)

	buyQueen(2400)
	buyQueen(2100)

	if (initialGame):
		buyQueen(1850)
		buyQueen(1600)
	
	closeMenu()

def buyAllQueens():
	log("Buying all queens")
	openMenu()

	device.touch(queenTab, yMainTabPosition + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.2)

	move(10000, 'UP')
	sleep(0.2)

	for x in range(0, 30):
		buyQueen(1610)
		move(queenCellHeight, 'DOWN')
	
	closeMenu()

def clickCancel():
	device.touch(450, 1450 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)

def clickPowerUps():
	log("Click PowerUps")
	device.touch(382, yPowerUpsPosition + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)
	device.touch(629, yPowerUpsPosition + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)
	device.touch(846, yPowerUpsPosition + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)
	device.touch(1080, yPowerUpsPosition + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)
	device.touch(1250, yPowerUpsPosition + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)

def click(times, loops):
	for n in range(0, loops):
		clickPowerUps()

		for x in range(0, times):
			device.touch(300, 600 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
			sleep(0.01)
			device.touch(300, 500 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
			sleep(0.01)
			clickCancel()

def baseGame(clicks, times):
	global initialGame
	clicksCounter = 0

	while True:
		click(clicks, times)
		buyLastQueens()
		click(clicks, times)
		buyLastQueens()
		buyAllSkills()

		if (buyStarters > -1):
			if clicksCounter >= 0:
				clicksCounter = clicksCounter + clicks

			if clicksCounter > buyStarters:
				initialGame = True
				initial()
				clicksCounter = -1
				initialGame = False

def miniGame():
	log("Starting Mini Game")
	for n in range(0, miniGameTimes):
		log("Ciclo: %i" % ( n + 1 )) 
		device.touch(1300, 600 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.5)
		device.touch(1000, 2450 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.5)
		device.touch(1100, 1500 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.5)
		device.touch(1000, 2300 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.5)
		device.touch(1000, 2300 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(3)
		click(400, 1)
		sleep(3)
		device.touch(1000, 2300 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(35)
		device.press('KEYCODE_BACK','DOWN_AND_UP')
		sleep(3)
		click(400, 1)
		sleep(3)
		device.touch(500, 2300 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(3)

	device.press('KEYCODE_BACK','DOWN_AND_UP')

def printHelp():
	print("Usage: setup.py [-h | -help] [-i | start] [-s8] [-buy=<count>] [-clicks=<count>] [-loops=<count>] [-miniGame=<count>]")
	print("")
	print("")
	print("-h | -help 		Start help")
	print("-i | -start 		Buy the first levels of everything when distance skiped after ECD")
	print("-s8 			Adjustment to improve accuracy on Galaxy S8")
	print("-allQueens 		Buy all available queen levels (already included on start game)")
	print("-buy			Buy all first levels after <count> clicks delay (overrides -start|-i argument)")
	print("-loops 			Defines number of interactions")
	print("-clicks 		Defines number of clicks per interaction")
	print("-miniGame		Start miniGame with <count> iteractions")
	print("")
	print("")
	print("The precedence order is: initial or allQueens, minigame and base game")
	print("")
	print("")

showHelp = False
initialGame = False
runAllQueens = False
miniGameTimes = 0
buyStarters = -1
clickTimes = 1000
loopTimes = 5

DEBUG = True

def setParameters():
	global showHelp, initialGame, miniGameTimes, buyStarters, clickTimes, loopTimes, runAllQueens, S8yPositionCorrection, DEBUG

	for arg in sys.argv:
		if ((arg.lower() == "-help") | (arg.lower() == "-h")):
			showHelp = True
			break

	for x in sys.argv:
		if x.lower() == "-s8":
			S8yPositionCorrection = 200
			continue

		if ((x.lower() == "-start") | (x.lower() == "-i")):
			initialGame = True
			continue

		if x.lower() == "-allqueens":
			runAllQueens = True
			continue

		if ((x.lower() == "-debug") | (x.lower() == "-d")):
			DEBUG = False
			continue

		if x.find("=") > -1:
			if x.find("clicks") > -1:
				try:
					clickTimes = int(x.split("=")[1])
				except:
					log("Clicks without value")
				continue
			if x.find("loops") > -1:
				try:
					loopTimes = int(x.split("=")[1])
				except:
					log("Loops without value")
				continue
			if x.find("buy") > -1:
				try:
					buyStarters = int(x.split("=")[1])
				except:
					log("Buy starters without value")
				continue
			if x.find("miniGame") > -1:
				try:
					miniGameTimes = int(x.split("=")[1])
				except:
					log("Minigame without value")
				continue

	if (runAllQueens and initialGame):
		runAllQueens = False

	if (buyStarters > -1):
		initialGame = False

	log("")
	log("Start with:")
	log("Apply S8 correction: %r" % (S8yPositionCorrection > 0))
	log("AllQueens: %r" % runAllQueens)
	log("Starter game: %r" % initialGame)
	log("Buy delay: %i" % buyStarters)
	log("Click times: %i" % clickTimes)
	log("Loops: %i" % loopTimes)
	log("MiniGame: %i vezes" % miniGameTimes)
	log("")

def initial():
	global initialGame

	log("")
	log("Initial setup start")
	buyCrabLevels()
	buyAllSkills()
	buyLastQueens()
	buyAllQueens()
	initialGame = False
	log("Initial setup ended")
	log("")

def startGame():
	connect()
	setParameters()

	if showHelp:
		printHelp()
		return

	if device:
		closeMenu()

		if (initialGame):
			initial()

		if (runAllQueens):
			buyAllQueens()

		if miniGameTimes > 0:
			miniGame()

		baseGame(clickTimes, loopTimes)

	else:
		print "could not connect"

def connect():
	global device
	try:
		device = MonkeyRunner.waitForConnection(2)
	except:
		device = None

startGame()