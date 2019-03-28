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

    print("Measuring Shunt Voltage & Current")
    print("Shunt Voltage (mV):")
    shunt_voltage_mv = testboard.ina219_getValue(INA219.SHUNT_VOLTAGE_MV)
    print(shunt_voltage_mv)

    print("Current consumption (mA):")
    shunt_resistor = 0.02
    current = (shunt_voltage_mv * 1000) /  shunt_resistor
    print(current)

    print("Current consumption (mA):")
    current_multiplier = 5
    current = testboard.ina219_getValue(INA219.CURRENT_MA) * current_multiplier
    print(current)
    time.sleep(1)

