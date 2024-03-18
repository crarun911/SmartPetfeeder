from Phidget22.Phidget import *
from Phidget22.Devices.VoltageInput import *
from Phidget22.Devices.LCD import *
from Phidget22.Devices.VoltageRatioInput import *



import time
from Phidget22.Net import *


def onSensorChange(self, sensorValue, sensorUnit):
	print("SensorValue [" + str(self.getChannel()) + "]: " + str(sensorValue))
	print("SensorUnit [" + str(self.getChannel()) + "]: " + str(sensorUnit.symbol))
	print("----------")
	if(sensorValue==0):
		self.linkedLCD.writeText(LCDFont.FONT_5x8,0,0,"Pet is hungry!")
		self.linkedLCD.flush()
	else:
		self.linkedLCD.clear()
		self.linkedLCD.flush()

		 

def main():
	lcd0 = LCD()
	voltageInput7 = VoltageInput()
	voltageRatioInput7=VoltageRatioInput()


	voltageInput7.setDeviceSerialNumber(38480)
	voltageInput7.setChannel(7)
	voltageRatioInput7.setChannel(7)
	lcd0.setDeviceSerialNumber(38480)
	lcd0.setChannel(0)

	voltageRatioInput7.linkedLCD=lcd0

	# voltageInput7.setOnVoltageChangeHandler(onVoltageChange)
	voltageRatioInput7.setOnSensorChangeHandler(onSensorChange)
	

	voltageInput7.openWaitForAttachment(5000)
	voltageRatioInput7.openWaitForAttachment(5000)
	lcd0.openWaitForAttachment(5000)

	lcd0.setBacklight(1)
	

	voltageRatioInput7.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_1129)



	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass

	voltageInput7.close()

main()