from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys, thread

S8yPositionCorrection = 0

yMainTabPosition = 1380
yPowerUpsPosition = 2250

defaulXPosition = 1270

queenCellHeight = 290

crabTab = 120
queenTab = 450
abilityTab = 750

def sleep(time):
	MonkeyRunner.sleep(time)
	return

def openMenu():
	device.touch(1350, 2470 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.3)
	return

def closeMenu():
	device.touch(1350, 1220 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.3)
	return

def move(dY, direction):
	if (direction == 'UP'):
		device.drag((defaulXPosition, 2000), (defaulXPosition, 2000 + dY), 1.0, 10)
	else:
		device.drag((defaulXPosition, 2000), (defaulXPosition, 2000 - dY), 1.0, 10)
	
	sleep(0.2)
	return

def buyCrabEvolution(Y):
	for x in range(0, 10):
		device.touch(defaulXPosition, Y + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.5)
		device.touch(defaulXPosition, Y + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
		sleep(0.5)
	return

def buyCrabLevels():
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

	#buy evo ametist
	buyCrabEvolution(2000)
	move(370, 'DOWN')
	#buy evo emerald
	buyCrabEvolution(2000)
	move(370, 'DOWN')
	#buy evo garnet
	buyCrabEvolution(2000)

	move(2000, 'UP')

	closeMenu()
	return

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

	return


def buyAllSkills():
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
	return

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
	return

def buyLastQueens():
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
	return

def buyAllQueens():
	openMenu()

	device.touch(queenTab, yMainTabPosition + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.2)

	move(10000, 'UP')
	sleep(0.2)

	for x in range(0, 30):
		buyQueen(1610)
		move(queenCellHeight, 'DOWN')
	
	closeMenu()
	return

def clickCancel():
	device.touch(450, 1450 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)
	return

def clickPowerUps():
	# Shadow Swarm
	device.touch(382, yPowerUpsPosition + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)
	# Smoke Screen
	device.touch(629, yPowerUpsPosition + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)
	# Queen Frenzy
	device.touch(846, yPowerUpsPosition + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)
	# Genetic Split
	device.touch(1080, yPowerUpsPosition + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)
	# Golden Leech
	device.touch(1250, yPowerUpsPosition + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)
	return

def click(times, loops):
	for n in range(0, loops):
		clickPowerUps()

		for x in range(0, times):
			device.touch(300, 600 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
			sleep(0.01)
			device.touch(300, 500 + S8yPositionCorrection, MonkeyDevice.DOWN_AND_UP)
			sleep(0.01)
			clickCancel()
	return

def baseGame(clicks, times):
	while True:
		click(clicks, times)
		buyLastQueens()
		click(clicks, times)
		buyLastQueens()
		buyAllSkills()

	return

try:
	global device
	device = MonkeyRunner.waitForConnection(2)
except:
	global device
	device = None

initialGame = False
clickTimes = 1000
loopTimes = 5

def startGame():
	if device:
		global initialGame, clickTimes, loopTimes, S8yPositionCorrection

		for x in sys.argv:
			if ((x == "s8") | (x == "S8")):
				S8yPositionCorrection = 200

		if (len(sys.argv) > 1):
			if ((sys.argv[1] == "start") | (sys.argv[1] == "-i")):
				initialGame = True
			if (len(sys.argv) == 3):
				clickTimes = int(sys.argv[1])
				loopTimes = int(sys.argv[2])
			if (len(sys.argv) == 4):
				clickTimes = int(sys.argv[2])
				loopTimes = int(sys.argv[3])

		print "Start script with parameters"
		print "Starter game: %r" % (initialGame)
		print "Click times: %i" % (clickTimes)
		print "Loops: %i" % (loopTimes)

		closeMenu()

		if (initialGame):
			buyCrabLevels()
			buyAllSkills()
			buyLastQueens()
			buyAllQueens()
			initialGame = False
			print "Initial setup ended."

		baseGame(clickTimes, loopTimes)

	else:
		print 'could not connect'

startGame()