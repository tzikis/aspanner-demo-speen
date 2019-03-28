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
    shunt_voltage_mv = testboard.ina219_getValue(INA219.SHUNT_VOLTAGE_MV)
    current = testboard.ina219_getValue(INA219.CURRENT_MA) * current_multiplier

    print("Current consumption (mA):")
    current_multiplier = 5
    print(current)

    print("Shunt Voltage (mV):")
    print(shunt_voltage_mv)

    print("Shunt Current consumption (mA):")
    shunt_resistor = 0.02
    current = (shunt_voltage_mv) /  shunt_resistor
    print(current)

    time.sleep(1)

