from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
print("Start")
device = MonkeyRunner.waitForConnection()
device.press("KEYCODE_HOME", MonkeyDevice.DOWN_AND_UP)
print("Finish")
