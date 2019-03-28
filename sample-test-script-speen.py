import time
import pytest
from SpannerTestboard import SpannerTestboard

testboard = SpannerTestboard("xenonEthDev3")


# BATTERY_RELAY_PIN = "D2"
# MAINS_RELAY_PIN = "D6"


def test_measure_power_consumption():
    print("")
    # testboard.digitalWrite(MAINS_RELAY_PIN, 'HIGH')
    # testboard.digitalWrite(BATTERY_RELAY_PIN, 'HIGH')
    # time.sleep(5)

    INA219 = SpannerTestboard.INA219
    time.sleep(1)

    print("Measuring Shunt Voltage & Current")
    print("Shunt Voltage (mV):")
    voltage = testboard.ina219_getValue(INA219.SHUNT_VOLTAGE_MV)
    print(voltage)
    time.sleep(1)


    print("Current consumption (mA):")
    current = testboard.ina219_getValue(INA219.CURRENT_MA)
    print(current)
    time.sleep(1)

