from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import sys

global device

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
	device.touch(1350, 2470, MonkeyDevice.DOWN_AND_UP)
	sleep(0.3)
	return

def closeMenu():
	device.touch(1350, 1220, MonkeyDevice.DOWN_AND_UP)
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
		device.touch(defaulXPosition, Y, MonkeyDevice.DOWN_AND_UP)
		sleep(0.5)
		device.touch(defaulXPosition, Y, MonkeyDevice.DOWN_AND_UP)
		sleep(0.5)
	return

def buyCrabLevels():
	openMenu()

	move(2000, 'UP')

	#clique na posicao da tab de crab
	device.touch(crabTab, yMainTabPosition, MonkeyDevice.DOWN_AND_UP)
	sleep(0.2)
	#long press para comprar lvl do crab
	device.touch(defaulXPosition, 1560, MonkeyDevice.DOWN)
	sleep(1)
	device.touch(defaulXPosition, 1560, MonkeyDevice.UP)
	sleep(0.1)
	#fim long press

	#comprar os 4000 lvl
	for x in range(0, 4): 
		device.touch(740, 1560, MonkeyDevice.DOWN_AND_UP)	
		sleep(0.2)

	#comprar evo ametista
	buyCrabEvolution(2000)
	move(370, 'DOWN')
	#comprar evo esmeralda
	buyCrabEvolution(1900)
	move(370, 'DOWN')
	#comprar evo garnet
	buyCrabEvolution(1900)

	move(2000, 'UP')

	closeMenu()
	return

def buySkill(abilityLocation, talentLocation, starter):
	applyPosition = 1800

	if (starter):
		times = 50
	else:
		times = 5

	if (starter):
		for x in range (0, 4):
			device.touch(defaulXPosition, abilityLocation, MonkeyDevice.DOWN_AND_UP)
			sleep(0.2)

		device.touch(defaulXPosition, talentLocation, MonkeyDevice.DOWN_AND_UP)
		sleep(0.2)
		device.touch(defaulXPosition, applyPosition, MonkeyDevice.DOWN_AND_UP)
		sleep(0.2)

		#fecha janela
		device.touch(1330, 700, MonkeyDevice.DOWN_AND_UP)
		sleep(0.2)

	#comprar N levels
	for x in range(0, times):
		device.touch(defaulXPosition, abilityLocation, MonkeyDevice.DOWN_AND_UP)
		sleep(0.1)

	return


def buyAllSkills(starter):
	position1 = 1150
	position3 = 1550
	colossalYLocation = 1600
	shadowYLocation = 1850
	smokeYLocation = 2100
	frenzyYLocation = 2350
	geneticYLocation = 2150
	goldenYLocation = 2400

	openMenu()

	device.touch(abilityTab, yMainTabPosition, MonkeyDevice.DOWN_AND_UP)
	sleep(0.2)

	move(1000, 'DOWN')

	buySkill(goldenYLocation, position1, starter)
	buySkill(geneticYLocation, position3, starter)
	move(1000, 'UP')
	buySkill(shadowYLocation, position3, starter)
	buySkill(frenzyYLocation, position3, starter)
	buySkill(smokeYLocation, position3, starter)
	buySkill(colossalYLocation, position3, starter)

	closeMenu()
	return

def buyQueen(posicaoY):
	#long press para comprar lvl do crab
	device.touch(defaulXPosition, posicaoY, MonkeyDevice.DOWN)
	sleep(1)
	device.touch(defaulXPosition, posicaoY, MonkeyDevice.UP)
	sleep(0.1)
	#fim long press

	for i in range(0, 3):
		device.touch(730, posicaoY, MonkeyDevice.DOWN_AND_UP)
		sleep(0.1)

	for j in range(0, 10):
		device.touch(defaulXPosition, posicaoY, MonkeyDevice.DOWN_AND_UP)
		sleep(0.1)

	#long press para comprar lvl do crab
	device.touch(defaulXPosition, posicaoY, MonkeyDevice.DOWN)
	sleep(1)
	device.touch(defaulXPosition, posicaoY, MonkeyDevice.UP)
	sleep(0.1)
	#fim long press

	for i in range(0, 5):
		device.touch(730, posicaoY, MonkeyDevice.DOWN_AND_UP)
		sleep(0.1)

	for i in range(0, 5):
		device.touch(1000, posicaoY, MonkeyDevice.DOWN_AND_UP)
		sleep(0.1)

	for j in range(0, 10):
		device.touch(defaulXPosition, posicaoY, MonkeyDevice.DOWN_AND_UP)
		sleep(0.1)
	return

def buyLastQueens():
	openMenu()

	device.touch(queenTab, yMainTabPosition, MonkeyDevice.DOWN_AND_UP)
	sleep(0.2)

	move(10000, 'DOWN')
	sleep(0.2)

	buyQueen(2400)
	buyQueen(2100)

	if (len(sys.argv) > 1):
			if ((sys.argv[1] == "start") | (sys.argv[1] == "-i")):
				buyQueen(1850)
				buyQueen(1600)
	
	closeMenu()
	return

def buyAllQueens():
	openMenu()

	device.touch(queenTab, yMainTabPosition, MonkeyDevice.DOWN_AND_UP)
	sleep(0.2)

	move(10000, 'UP')
	sleep(0.2)

	for x in range(0, 30):
		buyQueen(1660)
		move(queenCellHeight, 'DOWN')
	
	closeMenu()
	return

def clickCancel():
	device.touch(450, 1450, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)
	return

def clickPowerUps():
	# Shadow Swarm
	device.touch(382, yPowerUpsPosition, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)
	# Smoke Screen
	device.touch(629, yPowerUpsPosition, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)
	# Queen Frenzy
	device.touch(846, yPowerUpsPosition, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)
	# Genetic Split
	device.touch(1080, yPowerUpsPosition, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)
	# Golden Leech
	device.touch(1250, yPowerUpsPosition, MonkeyDevice.DOWN_AND_UP)
	sleep(0.01)
	return

def click(times, loops):
	for n in range(0, loops):
		clickPowerUps()

		for x in range(0, times):
			device.touch(300, 600, MonkeyDevice.DOWN_AND_UP)
			sleep(0.01)
			device.touch(300, 500, MonkeyDevice.DOWN_AND_UP)
			sleep(0.01)
			clickCancel()
	return

def baseGame(clicks, times):
	while True:
		click(clicks, times)
		buyLastQueens()
		click(clicks, times)
		buyLastQueens()
		buyAllSkills(False)

	return

try:
    device = MonkeyRunner.waitForConnection(2)
except:
    device = None

def startGame():
	if device:
		print 'connected!'

		closeMenu()

		if (len(sys.argv) > 1):
			if ((sys.argv[1] == "start") | (sys.argv[1] == "-i")):
				buyCrabLevels()
				buyAllSkills(True)
				buyLastQueens()
				buyAllQueens()

		if (len(sys.argv) == 3):
			baseGame(int(sys.argv[1]), int(sys.argv[2]))
		elif (len(sys.argv) == 4):
			baseGame(int(sys.argv[2]), int(sys.argv[3]))
		else:
			baseGame(1000, 5)

	else:
		print 'could not connect'

startGame()