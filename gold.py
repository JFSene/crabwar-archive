from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

try:
    device = MonkeyRunner.waitForConnection(10)
except:
    device = None
    
if device:
	print 'connected!'

	while True:
		device.touch(300, 500, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(400, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 500, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(600, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(300, 500, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(400, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 500, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(600, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		device.touch(500, 600, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		
		device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(0.01)
		
		device.touch(1280, 2243, MonkeyDevice.DOWN_AND_UP) #gold
		MonkeyRunner.sleep(0.01)
		
		device.touch(1250, 2123, MonkeyDevice.DOWN_AND_UP) #ok
		MonkeyRunner.sleep(0.01)
		device.touch(1080, 2243, MonkeyDevice.DOWN_AND_UP) #genectic split
		MonkeyRunner.sleep(0.01)
		device.touch(382, 2243, MonkeyDevice.DOWN_AND_UP) #shadow swarm
		MonkeyRunner.sleep(0.01)		
		device.touch(629, 2243, MonkeyDevice.DOWN_AND_UP) #smokescreen
		MonkeyRunner.sleep(0.01)		
		device.touch(846, 2243, MonkeyDevice.DOWN_AND_UP) #queen frenzy
		MonkeyRunner.sleep(0.01)		
		
else:
	print 'could not connect'