import time
import pytest
from SpannerTestboard import SpannerTestboard

testboard = SpannerTestboard("xenonEthDev3")


CHARGER_RELAY_PIN = "D2"
LOAD_RELAY_PIN = "D6"

GREEN_LED_PIN = "A4"
RED_LED_PIN = "A5"


TEMP_PIN = "A3"

def test_measure_power_consumption():
    print("")
    testboard.digitalWrite(CHARGER_RELAY_PIN, 'LOW')
    testboard.digitalWrite(LOAD_RELAY_PIN, 'LOW')
    testboard.digitalWrite(GREEN_LED_PIN, 'LOW')
    testboard.digitalWrite(RED_LED_PIN, 'LOW')
    time.sleep(5)

    INA219 = SpannerTestboard.INA219

    print("Measuring Shunt Voltage & Current")
    shunt_voltage_mv = testboard.ina219_getValue(INA219.SHUNT_VOLTAGE_MV)
    current_multiplier = 5
    current = testboard.ina219_getValue(INA219.CURRENT_MA) * current_multiplier

    print("Current consumption (mA):")
    print(current)

    print("Shunt Voltage (mV):")
    print(shunt_voltage_mv)

    print("Shunt Current consumption (mA):")
    shunt_resistor = 0.02
    current = (shunt_voltage_mv) /  shunt_resistor
    print(current)

    testboard.digitalWrite(CHARGER_RELAY_PIN, 'HIGH')
    testboard.digitalWrite(LOAD_RELAY_PIN, 'HIGH')
    testboard.digitalWrite(GREEN_LED_PIN, 'HIGH')
    testboard.digitalWrite(RED_LED_PIN, 'HIGH')

    temperature = get_temperature(TEMP_PIN)
    print("Temperature: " + str(temperature))

    time.sleep(10)

    testboard.digitalWrite(CHARGER_RELAY_PIN, 'LOW')
    testboard.digitalWrite(LOAD_RELAY_PIN, 'LOW')
    testboard.digitalWrite(GREEN_LED_PIN, 'LOW')
    testboard.digitalWrite(RED_LED_PIN, 'LOW')


#get the current temperature.
def get_temperature(tmp_pin):
  value = testboard.analogRead(tmp_pin)
  print(value)
  voltage = (3.3 * value) / 4096
  print(voltage)
  return (voltage - 0.5) * 100


